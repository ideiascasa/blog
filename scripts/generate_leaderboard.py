#!/usr/bin/env python3
"""Consulta BenchLM (API oficial ou fallback público) e grava _data/leaderboard.yml."""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
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

DATA_API_BASE = "https://data.benchlm.ai/v1"
PUBLIC_API_URL = "https://benchlm.ai/api/data/leaderboard"
USER_AGENT = "blog-leaderboard-updater/1.0"

MIN_CODING_INDEX = 40.0
# eficiencia = coding - POINTS_PER_DOLLAR * price
# +$1.00 de preço ⇔ +5 pontos de coding. Empate: menor gasto (price/coding).
POINTS_PER_DOLLAR = 5


def _slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def _sum_price(price_input: Any, price_output: Any) -> float | None:
    if (price_input is None or price_input == "") and (
        price_output is None or price_output == ""
    ):
        return None
    try:
        inp = float(price_input or 0.0)
        out = float(price_output or 0.0)
    except (TypeError, ValueError):
        return None
    return round(inp + out, 3)


def _fmt_index(value: Any) -> str:
    if value is None or value == "" or value == "—":
        return "—"
    return f"{float(value):.1f}"


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


def _http_get_json(url: str, headers: dict[str, str] | None = None) -> dict[str, Any]:
    req_headers = {"User-Agent": USER_AGENT}
    if headers:
        req_headers.update(headers)
    if requests is not None:
        response = requests.get(url, headers=req_headers, timeout=60)
        response.raise_for_status()
        payload = response.json()
    else:
        request = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(request, timeout=60) as response:
            payload = json.loads(response.read().decode("utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError(f"Resposta inesperada de {url}: objeto JSON esperado")
    return payload


def fetch_from_data_api(api_key: str) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    headers = {"Authorization": f"Bearer {api_key}"}

    rankings: list[dict[str, Any]] = []
    meta: dict[str, Any] = {}
    offset = 0
    while True:
        url = (
            f"{DATA_API_BASE}/rankings/current?"
            + urllib.parse.urlencode(
                {"surface": "coding", "limit": 100, "offset": offset}
            )
        )
        payload = _http_get_json(url, headers=headers)
        if not meta:
            methodology = payload.get("methodology") or {}
            meta = {
                "as_of": payload.get("dataAsOf"),
                "methodology_version": methodology.get("version"),
                "source_mode": payload.get("rankingMode"),
            }
        rankings.extend(payload.get("items") or [])
        nxt = (payload.get("pagination") or {}).get("nextOffset")
        if nxt is None:
            break
        offset = int(nxt)

    pricing_by_key: dict[str, dict[str, Any]] = {}
    offset = 0
    while True:
        url = (
            f"{DATA_API_BASE}/pricing?"
            + urllib.parse.urlencode({"limit": 100, "offset": offset})
        )
        payload = _http_get_json(url, headers=headers)
        for entry in payload.get("items") or []:
            cur = entry.get("current") or {}
            if cur.get("unit") != "per-1m-tokens":
                continue
            key = (entry.get("modelKey") or "").strip()
            if key:
                pricing_by_key[key] = cur
        nxt = (payload.get("pagination") or {}).get("nextOffset")
        if nxt is None:
            break
        offset = int(nxt)

    rows: list[dict[str, Any]] = []
    for item in rankings:
        slug = (item.get("modelKey") or item.get("slug") or "").strip()
        cur = pricing_by_key.get(slug) or {}
        rows.append(
            {
                "model": item.get("name") or slug,
                "creator": item.get("creator") or "",
                "model_id": slug,
                "coding_index": item.get("score"),
                "evidence_status": item.get("evidenceStatus") or "",
                "input_price": cur.get("input"),
                "output_price": cur.get("output"),
            }
        )
    return rows, meta


def fetch_from_public_api() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    url = (
        f"{PUBLIC_API_URL}?"
        + urllib.parse.urlencode({"format": "json", "category": "coding", "limit": 1000})
    )
    payload = _http_get_json(url)
    meta = {
        "as_of": payload.get("lastUpdated"),
        "methodology_version": payload.get("methodologyVersion"),
        "source_mode": payload.get("mode"),
    }
    rows: list[dict[str, Any]] = []
    for item in payload.get("models") or []:
        name = (item.get("model") or "").strip()
        if not name:
            continue
        scores = item.get("categoryScores") or {}
        rows.append(
            {
                "model": name,
                "creator": item.get("creator") or "",
                "model_id": _slugify(name),
                "coding_index": scores.get("coding"),
                "evidence_status": item.get("evidenceStatus") or "",
                "input_price": item.get("inputPrice"),
                "output_price": item.get("outputPrice"),
            }
        )
    return rows, meta


def to_items(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    for row in rows:
        raw_score = row.get("coding_index")
        if raw_score is None or raw_score == "":
            continue
        coding_index = round(float(raw_score), 1)
        if coding_index < MIN_CODING_INDEX or coding_index <= 0:
            continue

        price = _sum_price(row.get("input_price"), row.get("output_price"))
        if price is None or price <= 0:
            continue

        model_id = (row.get("model_id") or "").strip()
        if not model_id or model_id in seen_ids:
            continue
        seen_ids.add(model_id)

        gasto = round(price / coding_index, 3)
        eficiencia = round(coding_index - POINTS_PER_DOLLAR * price, 3)
        items.append(
            {
                "rank": 0,
                "model": row.get("model") or model_id,
                "creator": row.get("creator") or "",
                "model_id": model_id,
                "coding_index": f"{coding_index:.1f}",
                "evidence_status": row.get("evidence_status") or "",
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
        f"source: {payload.get('source')} / {payload.get('task_type')} ({payload.get('methodology_version')})",
        f"filtro: coding_index >= {MIN_CODING_INDEX}",
        f"eficiencia: coding - {POINTS_PER_DOLLAR} * price (empate: menor gasto)",
        "",
        "| Rank | Modelo | Criador | Slug | Coding Index | Evidência | Price | Gasto por Coding | Eficiencia |",
        "| ---: | --- | --- | --- | ---: | --- | ---: | ---: | ---: |",
    ]
    for item in payload.get("items") or []:
        lines.append(
            "| {rank} | {model} | {creator} | `{slug}` | {coding} | {evidence} | {price} | {gasto} | {eficiencia} |".format(
                rank=item.get("rank"),
                model=item.get("model"),
                creator=item.get("creator") or "—",
                slug=item.get("model_id"),
                coding=_fmt_index(item.get("coding_index")),
                evidence=item.get("evidence_status") or "—",
                price=_fmt_price(item.get("price")),
                gasto=_fmt_gasto(item.get("gasto_por_coding")),
                eficiencia=_fmt_eficiencia(item.get("eficiencia")),
            )
        )
    PREVIEW.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    api_key = os.environ.get("BENCHLM_KEY", "").strip()
    rows: list[dict[str, Any]]
    meta: dict[str, Any]
    if api_key:
        try:
            rows, meta = fetch_from_data_api(api_key)
            endpoint_used = "data.benchlm.ai/v1"
        except Exception as exc:
            status = getattr(getattr(exc, "response", None), "status_code", None) or getattr(exc, "code", None)
            if status in (401, 403, 429):
                print(
                    f"Aviso: data.benchlm.ai/v1 retornou HTTP {status}; usando endpoint público sem chave.",
                    file=sys.stderr,
                )
                rows, meta = fetch_from_public_api()
                endpoint_used = "benchlm.ai/api/data/leaderboard"
            else:
                raise
    else:
        print(
            "Aviso: BENCHLM_KEY não definida; usando endpoint público sem chave (benchlm.ai/api/data/leaderboard).",
            file=sys.stderr,
        )
        rows, meta = fetch_from_public_api()
        endpoint_used = "benchlm.ai/api/data/leaderboard"

    items = to_items(rows)

    if not items:
        print(
            f"Erro: API ({endpoint_used}) retornou {len(rows)} linhas, mas 0 modelos válidos após filtro (coding_index >= {MIN_CODING_INDEX}). "
            "Arquivos _data/leaderboard.* preservados sem alteração.",
            file=sys.stderr,
        )
        sys.exit(1)

    now_sp = datetime.now(SAO_PAULO)
    payload = {
        "updated_at": now_sp.strftime("America/Sao Paulo - %d/%m/%Y %H:%M"),
        "source": "benchlm",
        "task_type": "coding",
        "min_coding_index": MIN_CODING_INDEX,
        "points_per_dollar": POINTS_PER_DOLLAR,
        "as_of": meta.get("as_of"),
        "methodology_version": meta.get("methodology_version"),
        "citation": "Data from BenchLM.ai (benchlm.ai/coding), CC BY-NC 4.0.",
        "source_url": "https://benchlm.ai/coding",
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

    with_score = [r for r in rows if r.get("coding_index") is not None]
    scores = [float(r["coding_index"]) for r in with_score]
    print(f"Fonte ({endpoint_used}) retornou: {len(rows)} modelos (com coding_index: {len(with_score)})")
    if scores:
        print(f"Faixa coding_index na API: {min(scores)} .. {max(scores)}")
    print(f"Após filtro coding_index >= {MIN_CODING_INDEX} e preço > 0: {len(items)} modelos")
    if items:
        print(
            f"Faixa eficiencia: {items[0]['eficiencia']} .. {items[-1]['eficiencia']}"
        )
    print(f"Gravados em {OUTPUT} e {OUTPUT_JSON}")
    print(f"Preview em {PREVIEW}")


if __name__ == "__main__":
    main()
