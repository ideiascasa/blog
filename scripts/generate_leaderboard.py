#!/usr/bin/env python3
"""Consulta OpenRouter Benchmarks e grava _data/leaderboard.yml."""

from __future__ import annotations

import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_data" / "leaderboard.yml"
PREVIEW = ROOT / "teste.md"
SAO_PAULO = ZoneInfo("America/Sao_Paulo")

API_URL = "https://openrouter.ai/api/v1/benchmarks"
# Sem max_results: a API devolve todos os modelos com score de coding.
# Não há parâmetro de nota mínima nem de ordenação — filtro/ordem ficam no Python.
PARAMS = {
    "source": "artificial-analysis",
    "task_type": "coding",
}
MIN_CODING_INDEX = 40.0
# eficiencia = coding^α / price^β
# Calibrado para: +3 pontos de coding ≈ +$0.50 de preço
# (razão α/β ≈ 14.5). Mantém Luna (71@$0.70) acima de Gemini (76@$2.25).
PRICE_BETA = 0.11
CODING_ALPHA = 1.6


def _require_api_key() -> str:
    key = os.environ.get("OR_KEY", "").strip()
    if not key:
        print("OR_KEY não definida. Configure o secret/env OR_KEY.", file=sys.stderr)
        sys.exit(1)
    return key


def _price_per_million(value: Any) -> float | None:
    if value is None or value == "":
        return None
    try:
        return round(float(value) * 1_000_000, 4)
    except (TypeError, ValueError):
        return None


def _sum_price(price_input: float | None, price_output: float | None) -> float | None:
    if price_input is None and price_output is None:
        return None
    return round((price_input or 0.0) + (price_output or 0.0), 2)


def _fmt_index(value: Any) -> str:
    if value is None or value == "":
        return "—"
    return str(int(round(float(value))))


def _fmt_price(value: Any) -> str:
    if value is None or value == "":
        return "—"
    return f"${float(value):.2f}"


def _fmt_gasto(value: Any) -> str:
    if value is None or value == "":
        return "—"
    return f"{float(value):.2f}"


def fetch_benchmarks(api_key: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    response = requests.get(
        API_URL,
        headers={"Authorization": f"Bearer {api_key}"},
        params=PARAMS,
        timeout=60,
    )
    response.raise_for_status()
    payload = response.json()
    data = payload.get("data") or []
    meta = payload.get("meta") or {}
    if not isinstance(data, list):
        raise RuntimeError("Resposta inesperada: 'data' não é uma lista")
    return data, meta


def to_items(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    scored = [
        row
        for row in rows
        if row.get("coding_index") is not None
        and float(row["coding_index"]) >= MIN_CODING_INDEX
    ]

    items: list[dict[str, Any]] = []
    for row in scored:
        pricing = row.get("pricing") or {}
        slug = row.get("model_permaslug") or ""
        price_input = _price_per_million(pricing.get("prompt"))
        price_output = _price_per_million(pricing.get("completion"))
        price = _sum_price(price_input, price_output)
        if price is None or price <= 0:
            continue
        coding_index = round(float(row["coding_index"]))
        if coding_index <= 0:
            continue
        gasto = round(price / coding_index, 2)
        eficiencia = round(coding_index**CODING_ALPHA / price**PRICE_BETA)
        items.append(
            {
                "rank": 0,
                "model": row.get("display_name") or slug,
                "model_id": slug,
                "coding_index": coding_index,
                "price": f"{price:.2f}",
                "gasto_por_coding": f"{gasto:.2f}",
                "eficiencia": eficiencia,
            }
        )

    items.sort(
        key=lambda item: (item["eficiencia"], item["coding_index"]),
        reverse=True,
    )
    for rank, item in enumerate(items, start=1):
        item["rank"] = rank
    return items


def write_preview(payload: dict[str, Any]) -> None:
    lines = [
        "# Melhores IA — preview local",
        "",
        f"Atualizado em: {payload.get('updated_at')}",
        f"as_of: {payload.get('as_of')}",
        f"source: {payload.get('source')} / {payload.get('task_type')}",
        f"filtro: coding_index >= {MIN_CODING_INDEX}",
        f"eficiencia: coding^{CODING_ALPHA} / price^{PRICE_BETA}",
        "",
        "| Rank | Modelo | Slug | Coding Index | Price | Gasto por Coding | Eficiencia |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: |",
    ]
    for item in payload.get("items") or []:
        lines.append(
            "| {rank} | {model} | `{slug}` | {coding} | {price} | {gasto} | {eficiencia} |".format(
                rank=item.get("rank"),
                model=item.get("model"),
                slug=item.get("model_id"),
                coding=_fmt_index(item.get("coding_index")),
                price=_fmt_price(item.get("price")),
                gasto=_fmt_gasto(item.get("gasto_por_coding")),
                eficiencia=item.get("eficiencia"),
            )
        )
    PREVIEW.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    api_key = _require_api_key()
    rows, meta = fetch_benchmarks(api_key)
    items = to_items(rows)

    now_sp = datetime.now(SAO_PAULO)
    payload = {
        "updated_at": now_sp.strftime("America/Sao Paulo - %H:%M"),
        "source": "artificial-analysis",
        "task_type": "coding",
        "min_coding_index": MIN_CODING_INDEX,
        "price_beta": PRICE_BETA,
        "coding_alpha": CODING_ALPHA,
        "as_of": meta.get("as_of"),
        "citation": meta.get("citation"),
        "source_url": meta.get("source_url") or "https://openrouter.ai/rankings",
        "items": items,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as handle:
        yaml.dump(
            payload,
            handle,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
        )

    write_preview(payload)

    with_score = [r for r in rows if r.get("coding_index") is not None]
    scores = [float(r["coding_index"]) for r in with_score]
    print(f"API retornou: {len(rows)} modelos (com coding_index: {len(with_score)})")
    if scores:
        print(f"Faixa na API: {min(scores)} .. {max(scores)}")
    print(f"Após filtro coding_index >= {MIN_CODING_INDEX}: {len(items)} modelos")
    if items:
        print(
            f"Faixa eficiencia: {items[0]['eficiencia']} .. {items[-1]['eficiencia']}"
        )
    print(f"Gravados em {OUTPUT}")
    print(f"Preview em {PREVIEW}")


if __name__ == "__main__":
    main()
