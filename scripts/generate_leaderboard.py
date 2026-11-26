#!/usr/bin/env python3
"""Consulta OpenRouter Benchmarks e grava _data/leaderboard.yml."""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

# Estas dependências existem no CI (instaladas pelo workflow). No ambiente local
# evitamos exigir instalação: se faltarem, usamos a stdlib (urllib) e um
# emissor YAML mínimo que reproduz a saída usada no projeto.
try:
    import requests
except ImportError:  # pragma: no cover - ambiente local sem requests
    requests = None  # type: ignore[assignment]

try:
    import yaml
except ImportError:  # pragma: no cover - ambiente local sem PyYAML
    yaml = None  # type: ignore[assignment]

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "_data" / "leaderboard.yml"
OUTPUT_JSON = ROOT / "_data" / "leaderboard.json"
PREVIEW = ROOT / "teste.md"
SAO_PAULO = ZoneInfo("America/Sao_Paulo")

API_URL = "https://openrouter.ai/api/v1/benchmarks"
# Design Arena (codecategories) devolve todos os modelos avaliados em geração
# de código (Website, UI Component, Data Viz, Game Dev e 3D Design).
PARAMS = {
    "source": "design-arena",
    "task_type": "coding",
}
ELO_MIN = 831.0
ELO_MAX = 1460.0
MIN_CODING_INDEX = 40.0
# eficiencia = coding - POINTS_PER_DOLLAR * price
# +$1.00 de preço ⇔ +5 pontos de coding. Empate: menor gasto (price/coding).
POINTS_PER_DOLLAR = 5


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
    return round((price_input or 0.0) + (price_output or 0.0), 3)


def _elo_to_coding_index(elo: float) -> float:
    return round(((elo - ELO_MIN) / (ELO_MAX - ELO_MIN)) * 100.0, 1)


def _fmt_index(value: Any) -> str:
    if value is None or value == "" or value == "—":
        return "—"
    return f"{float(value):.1f}"


def _fmt_elo(value: Any) -> str:
    if value is None or value == "" or value == "—":
        return "—"
    return f"{round(float(value))}"


def _fmt_price(value: Any) -> str:
    if value is None or value == "":
        return "—"
    return f"${float(value):.3f}"


def _fmt_gasto(value: Any) -> str:
    if value is None or value == "":
        return "—"
    return f"{float(value):.3f}"


def _fmt_eficiencia(value: Any) -> str:
    if value is None or value == "":
        return "—"
    return f"{float(value):.3f}"


def fetch_benchmarks(api_key: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    headers = {"Authorization": f"Bearer {api_key}"}
    if requests is not None:
        response = requests.get(API_URL, headers=headers, params=PARAMS, timeout=60)
        response.raise_for_status()
        payload = response.json()
    else:
        url = f"{API_URL}?{urllib.parse.urlencode(PARAMS)}"
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = json.loads(response.read().decode("utf-8"))
    data = payload.get("data") or []
    meta = payload.get("meta") or {}
    if not isinstance(data, list):
        raise RuntimeError("Resposta inesperada: 'data' não é uma lista")
    return data, meta


def to_items(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    # Deduplica por model_permaslug mantendo a variante com maior Elo
    # (desempate por total de batalhas e win_rate).
    best_by_slug: dict[str, tuple[tuple[float, int, float], dict[str, Any], float]] = {}
    for row in rows:
        elo_raw = row.get("elo")
        slug = (row.get("model_permaslug") or "").strip()
        if elo_raw is None or not slug:
            continue
        elo = float(elo_raw)
        if _elo_to_coding_index(elo) < MIN_CODING_INDEX:
            continue
        pricing = row.get("pricing") or {}
        price_input = _price_per_million(pricing.get("prompt"))
        price_output = _price_per_million(pricing.get("completion"))
        price = _sum_price(price_input, price_output)
        if price is None or price <= 0:
            continue

        battles = int((row.get("tournament_stats") or {}).get("total") or 0)
        win_rate = float(row.get("win_rate") or 0.0)
        quality_key = (elo, battles, win_rate)
        current = best_by_slug.get(slug)
        if current is None or quality_key > current[0]:
            best_by_slug[slug] = (quality_key, row, price)

    items: list[dict[str, Any]] = []
    for slug, (_, row, price) in best_by_slug.items():
        elo = float(row["elo"])
        coding_index = _elo_to_coding_index(elo)
        if coding_index <= 0:
            continue
        gasto = round(price / coding_index, 3)
        eficiencia = round(coding_index - POINTS_PER_DOLLAR * price, 3)
        items.append(
            {
                "rank": 0,
                "model": row.get("display_name") or slug,
                "model_id": slug,
                "coding_index": f"{coding_index:.1f}",
                "coding_elo": _fmt_elo(elo),
                "win_rate": _fmt_index(row.get("win_rate")),
                "price": f"{price:.3f}",
                "gasto_por_coding": f"{gasto:.3f}",
                "eficiencia": f"{eficiencia:.3f}",
            }
        )

    items.sort(
        key=lambda item: (
            -float(item["eficiencia"]),
            float(item["gasto_por_coding"]),
        ),
    )
    for rank, item in enumerate(items, start=1):
        item["rank"] = rank
    return items


_NUMERIC_RE = re.compile(r"^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$")
_TIMESTAMP_RE = re.compile(r"^\d{4}-\d{2}-\d{2}([Tt ].*)?$")
_BOOL_NULL = {"true", "false", "null", "yes", "no", "on", "off", "~", ""}


def _yaml_scalar(value: Any) -> str:
    """Emissor mínimo de escalares YAML compatível com a saída do PyYAML aqui."""
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        return repr(value)
    text = str(value)
    needs_quote = (
        text == ""
        or text != text.strip()
        or _NUMERIC_RE.match(text) is not None
        or _TIMESTAMP_RE.match(text) is not None
        or text.lower() in _BOOL_NULL
        or text[0] in "-?:,[]{}#&*!|>'\"%@`"
        or ": " in text
        or text.endswith(":")
        or " #" in text
    )
    if needs_quote:
        return "'" + text.replace("'", "''") + "'"
    return text


def _dump_yaml(payload: dict[str, Any]) -> str:
    """Fallback de serialização usado apenas quando PyYAML não está disponível."""
    lines: list[str] = []
    for key, value in payload.items():
        if key == "items":
            continue
        lines.append(f"{key}: {_yaml_scalar(value)}")
    lines.append("items:")
    for item in payload.get("items") or []:
        for index, (key, value) in enumerate(item.items()):
            prefix = "- " if index == 0 else "  "
            lines.append(f"{prefix}{key}: {_yaml_scalar(value)}")
    return "\n".join(lines) + "\n"


def write_preview(payload: dict[str, Any]) -> None:
    lines = [
        "# Melhores IA — preview local",
        "",
        f"Atualizado em: {payload.get('updated_at')}",
        f"as_of: {payload.get('as_of')}",
        f"source: {payload.get('source')} / {payload.get('task_type')}",
        f"escala: {ELO_MIN:.0f} Elo = 0.0% .. {ELO_MAX:.0f} Elo = 100.0% (regra de 3)",
        f"filtro: coding_index >= {MIN_CODING_INDEX} (deduplicado por model_permaslug)",
        f"eficiencia: coding - {POINTS_PER_DOLLAR} * price (empate: menor gasto)",
        "",
        "| Rank | Modelo | Slug | Coding Index | Coding Elo | Win Rate (%) | Price | Gasto por Coding | Eficiencia |",
        "| ---: | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for item in payload.get("items") or []:
        lines.append(
            "| {rank} | {model} | `{slug}` | {coding} | {elo} | {win_rate} | {price} | {gasto} | {eficiencia} |".format(
                rank=item.get("rank"),
                model=item.get("model"),
                slug=item.get("model_id"),
                coding=_fmt_index(item.get("coding_index")),
                elo=_fmt_elo(item.get("coding_elo")),
                win_rate=_fmt_index(item.get("win_rate")),
                price=_fmt_price(item.get("price")),
                gasto=_fmt_gasto(item.get("gasto_por_coding")),
                eficiencia=_fmt_eficiencia(item.get("eficiencia")),
            )
        )
    PREVIEW.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    api_key = _require_api_key()
    rows, meta = fetch_benchmarks(api_key)
    items = to_items(rows)

    if not items:
        print(
            f"Erro: API retornou {len(rows)} linhas, mas 0 modelos válidos após filtro (coding_index >= {MIN_CODING_INDEX}). "
            "Arquivos _data/leaderboard.* preservados sem alteração.",
            file=sys.stderr,
        )
        sys.exit(1)

    now_sp = datetime.now(SAO_PAULO)
    payload = {
        "updated_at": now_sp.strftime("America/Sao Paulo - %d/%m/%Y %H:%M"),
        "source": "design-arena",
        "task_type": "coding",
        "elo_min": int(ELO_MIN),
        "elo_max": int(ELO_MAX),
        "min_coding_index": MIN_CODING_INDEX,
        "points_per_dollar": POINTS_PER_DOLLAR,
        "as_of": meta.get("as_of"),
        "citation": meta.get("citation") or "Source: Design Arena (www.designarena.ai) via OpenRouter (openrouter.ai/rankings).",
        "source_url": meta.get("source_url") or "https://www.designarena.ai",
        "items": items,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as handle:
        if yaml is not None:
            yaml.dump(
                payload,
                handle,
                allow_unicode=True,
                default_flow_style=False,
                sort_keys=False,
            )
        else:
            handle.write(_dump_yaml(payload))

    with OUTPUT_JSON.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)

    write_preview(payload)

    with_score = [r for r in rows if r.get("elo") is not None]
    scores = [_elo_to_coding_index(float(r["elo"])) for r in with_score]
    print(f"API retornou: {len(rows)} linhas (com elo: {len(with_score)})")
    if scores:
        print(f"Faixa coding_index na API: {min(scores)} .. {max(scores)}")
    print(f"Após filtro coding_index >= {MIN_CODING_INDEX} e deduplicação: {len(items)} modelos")
    if items:
        print(
            f"Faixa eficiencia: {items[0]['eficiencia']} .. {items[-1]['eficiencia']}"
        )
    print(f"Gravados em {OUTPUT} e {OUTPUT_JSON}")
    print(f"Preview em {PREVIEW}")


if __name__ == "__main__":
    main()
