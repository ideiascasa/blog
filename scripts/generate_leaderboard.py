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
SAO_PAULO = ZoneInfo("America/Sao_Paulo")

API_URL = "https://openrouter.ai/api/v1/benchmarks"
PARAMS = {
    "source": "artificial-analysis",
    "task_type": "coding",
    "max_results": 100,
}


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


def _creator_from_slug(slug: str | None) -> str:
    if not slug or "/" not in slug:
        return ""
    return slug.split("/", 1)[0]


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
    ]
    scored.sort(key=lambda row: float(row["coding_index"]), reverse=True)

    items: list[dict[str, Any]] = []
    for rank, row in enumerate(scored, start=1):
        pricing = row.get("pricing") or {}
        slug = row.get("model_permaslug") or ""
        items.append(
            {
                "rank": rank,
                "model": row.get("display_name") or slug,
                "creator": _creator_from_slug(slug),
                "model_id": slug,
                "coding_index": float(row["coding_index"]),
                "intelligence_index": row.get("intelligence_index"),
                "agentic_index": row.get("agentic_index"),
                "price_input": _price_per_million(pricing.get("prompt")),
                "price_output": _price_per_million(pricing.get("completion")),
            }
        )
    return items


def main() -> None:
    api_key = _require_api_key()
    rows, meta = fetch_benchmarks(api_key)
    items = to_items(rows)

    now_sp = datetime.now(SAO_PAULO)
    payload = {
        "updated_at": now_sp.strftime("America/Sao Paulo - %H:%M"),
        "source": "artificial-analysis",
        "task_type": "coding",
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

    print(f"Gravados {len(items)} modelos em {OUTPUT}")


if __name__ == "__main__":
    main()
