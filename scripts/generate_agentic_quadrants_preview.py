#!/usr/bin/env python3
"""Gera preview local do gráfico de quadrantes usando o Agentic Index.

Espelha scripts/generate_quadrants_preview.py, mas o eixo Y passa a ser o
`agentic_index` (em vez do `coding_index`). Lê _data/leaderboard.json.

Saídas (ambas ignoradas pelo git, para revisão antes de publicar):
  - teste.md ............ chave OR_KEY + nota + imagem renderizada do gráfico
  - teste_agentic.html .. a mesma página, abrível direto no navegador

O .md embute um PNG (renderizado via Chrome headless) porque um arquivo .md
aberto no navegador/preview não executa <script> — só mostra o HTML cru.
"""

from __future__ import annotations

import base64
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data" / "leaderboard.json"
OUTPUT_MD = ROOT / "teste.md"
OUTPUT_HTML = ROOT / "teste_agentic.html"
OUTPUT_PNG = ROOT / ".teste_agentic.png"

# Guardamos a chave de teste no arquivo gitignored para não vazá-la.
OR_KEY_LINE = (
)

SPLIT_PRICE = 4.0         # Eixo X invertido (Preço)
SPLIT_AGENTIC = 30.0      # Eixo Y (Agentic Index)
PRICE_MAX = 20.0          # limite de preço incluído no gráfico
X_MIN = 0.0
X_MAX = 20.0
Y_MIN = 0.0
Y_MAX = 60.0

CHROME_CANDIDATES = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
)


def _find_chrome() -> str | None:
    for path in CHROME_CANDIDATES:
        if Path(path).exists():
            return path
    return shutil.which("chromium") or shutil.which("google-chrome")


def _render_png() -> bytes | None:
    """Renderiza o HTML standalone em PNG via Chrome headless (sem instalar nada)."""
    chrome = _find_chrome()
    if chrome is None:
        return None
    subprocess.run(
        [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--hide-scrollbars",
            "--window-size=1080,860",
            "--virtual-time-budget=12000",
            f"--screenshot={OUTPUT_PNG}",
            OUTPUT_HTML.resolve().as_uri(),
        ],
        capture_output=True,
        check=False,
    )
    if not OUTPUT_PNG.exists():
        return None
    data = OUTPUT_PNG.read_bytes()
    OUTPUT_PNG.unlink(missing_ok=True)
    return data


def _read_points() -> list[dict[str, object]]:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    points: list[dict[str, object]] = []
    for item in payload.get("items", []):
        price = item.get("price")
        agentic = item.get("agentic_index")
        coding = item.get("coding_index")
        if price in (None, "—") or agentic in (None, "—"):
            continue
        if float(price) > PRICE_MAX:
            continue
        points.append(
            {
                "model": item.get("model", ""),
                "slug": item.get("model_id", ""),
                "x": float(price),
                "y": float(agentic),
                "coding": coding,
                "gasto": item.get("gasto_por_coding", ""),
                "eficiencia": item.get("eficiencia", ""),
            }
        )
    points.sort(key=lambda p: -float(p["y"]))
    return points


def _build_html(points: list[dict[str, object]]) -> str:
    data_json = json.dumps(points, ensure_ascii=False)
    template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Matriz de Custo-Benefício — Agentic Index vs Preço</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<style>
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    margin: 20px auto;
    max-width: 960px;
    background: #fdfdfd;
    color: #222;
  }
  .chart-container {
    position: relative;
    background: #ffffff;
    border: 1px solid #e1e4e8;
    border-radius: 8px;
    padding: 16px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  }
  .chart-wrapper {
    position: relative;
    height: 560px;
    width: 100%;
  }
  .legend-quadrants {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    margin-top: 15px;
    font-size: 13px;
  }
  .legend-item {
    padding: 8px 12px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .q-top-right { background: rgba(75, 192, 192, 0.15); border-left: 4px solid rgb(75, 192, 192); }
  .q-top-left { background: rgba(54, 162, 235, 0.15); border-left: 4px solid rgb(54, 162, 235); }
  .q-bottom-right { background: rgba(255, 205, 86, 0.18); border-left: 4px solid rgb(255, 205, 86); }
  .q-bottom-left { background: rgba(255, 99, 132, 0.15); border-left: 4px solid rgb(255, 99, 132); }
</style>
</head>
<body>

<div class="chart-container">
  <h2 style="margin-top: 0; margin-bottom: 6px;">Matriz de Custo-Benefício dos Modelos — Agentic Index</h2>
  <p style="color: #666; margin-top: 0; font-size: 14px;">
    Agentic Index (Y) × Preço por milhão de tokens (X, invertido). Quanto mais ao topo e à direita, melhor a relação capacidade/preço.
  </p>

  <div class="chart-wrapper">
    <canvas id="agenticQuadrantsChart"></canvas>
  </div>

  <div class="legend-quadrants">
    <div class="legend-item q-top-left">
      <strong>Superior Esquerdo:</strong> Alta Capacidade / Alto Custo (Top de linha / Premium)
    </div>
    <div class="legend-item q-top-right">
      <strong>Superior Direito:</strong> 🏆 Melhor Custo-Benefício (Alta Capacidade + Baixo Custo)
    </div>
    <div class="legend-item q-bottom-left">
      <strong>Inferior Esquerdo:</strong> Baixa Eficiência (Custo Alto para a capacidade oferecida)
    </div>
    <div class="legend-item q-bottom-right">
      <strong>Inferior Direito:</strong> Econômico (Entrada / Baixo Custo)
    </div>
  </div>
</div>

<script>
const DATA = __DATA_JSON__;
const SPLIT_PRICE = __SPLIT_PRICE__;
const SPLIT_AGENTIC = __SPLIT_AGENTIC__;

const quadrantsPlugin = {
  id: 'quadrants',
  beforeDraw(chart, args, options) {
    const { ctx, chartArea: { left, top, right, bottom }, scales: { x, y } } = chart;
    const splitX = x.getPixelForValue(options.splitX);
    const splitY = y.getPixelForValue(options.splitY);

    ctx.save();
    ctx.fillStyle = options.topLeft || 'rgba(54, 162, 235, 0.08)';
    ctx.fillRect(left, top, splitX - left, splitY - top);

    ctx.fillStyle = options.topRight || 'rgba(75, 192, 192, 0.16)';
    ctx.fillRect(splitX, top, right - splitX, splitY - top);

    ctx.fillStyle = options.bottomLeft || 'rgba(255, 99, 132, 0.08)';
    ctx.fillRect(left, splitY, splitX - left, bottom - splitY);

    ctx.fillStyle = options.bottomRight || 'rgba(255, 205, 86, 0.12)';
    ctx.fillRect(splitX, splitY, right - splitX, bottom - splitY);

    ctx.strokeStyle = 'rgba(0, 0, 0, 0.25)';
    ctx.lineWidth = 1;
    ctx.setLineDash([5, 5]);

    ctx.beginPath();
    ctx.moveTo(splitX, top);
    ctx.lineTo(splitX, bottom);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(left, splitY);
    ctx.lineTo(right, splitY);
    ctx.stroke();

    ctx.restore();
  }
};

const ctx = document.getElementById('agenticQuadrantsChart').getContext('2d');
new Chart(ctx, {
  type: 'scatter',
  data: {
    datasets: [{
      label: 'Modelos',
      data: DATA.map(item => ({
        x: item.x,
        y: item.y,
        model: item.model,
        slug: item.slug,
        price: item.x,
        agentic: item.y,
        coding: item.coding,
        eficiencia: item.eficiencia,
        gasto: item.gasto
      })),
      backgroundColor: 'rgba(37, 99, 235, 0.85)',
      borderColor: '#1e40af',
      borderWidth: 1,
      pointRadius: 6,
      pointHoverRadius: 9,
      pointHoverBackgroundColor: '#dc2626'
    }]
  },
  options: {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      x: {
        type: 'linear',
        reverse: true,
        min: __X_MIN__,
        max: __X_MAX__,
        title: {
          display: true,
          text: '← Mais Caro | Preço ($ por 1M tokens) | Mais Barato →',
          font: { weight: 'bold', size: 13 }
        },
        ticks: {
          callback: function(value) {
            return '$' + Number(value).toFixed(2);
          }
        }
      },
      y: {
        min: __Y_MIN__,
        max: __Y_MAX__,
        title: {
          display: true,
          text: 'Agentic Index (Capacidade)',
          font: { weight: 'bold', size: 13 }
        },
        ticks: {
          stepSize: 5,
          callback: function(value) {
            return Number(value).toFixed(2);
          }
        }
      }
    },
    plugins: {
      legend: {
        display: false
      },
      tooltip: {
        backgroundColor: 'rgba(17, 24, 39, 0.95)',
        titleFont: { size: 14, weight: 'bold' },
        bodyFont: { size: 12 },
        padding: 10,
        callbacks: {
          title: function(context) {
            const raw = context[0].raw;
            return raw.model;
          },
          label: function(context) {
            const raw = context.raw;
            return [
              `Agentic Index: ${raw.agentic.toFixed(2)}`,
              `Coding Index: ${raw.coding}`,
              `Preço: $${raw.price.toFixed(2)} / 1M tokens`,
              `Eficiência: ${raw.eficiencia}`,
              `Gasto por coding: ${raw.gasto}`
            ];
          }
        }
      },
      quadrants: {
        splitX: SPLIT_PRICE,
        splitY: SPLIT_AGENTIC,
        topLeft: 'rgba(54, 162, 235, 0.08)',
        topRight: 'rgba(75, 192, 192, 0.16)',
        bottomLeft: 'rgba(255, 99, 132, 0.08)',
        bottomRight: 'rgba(255, 205, 86, 0.12)'
      }
    }
  },
  plugins: [quadrantsPlugin]
});
</script>
</body>
</html>
"""
    html = template.replace("__DATA_JSON__", data_json)
    html = html.replace("__SPLIT_PRICE__", str(SPLIT_PRICE))
    html = html.replace("__SPLIT_AGENTIC__", str(SPLIT_AGENTIC))
    html = html.replace("__X_MIN__", str(X_MIN))
    html = html.replace("__X_MAX__", str(X_MAX))
    html = html.replace("__Y_MIN__", str(Y_MIN))
    html = html.replace("__Y_MAX__", str(Y_MAX))
    return html


def main() -> None:
    points = _read_points()
    html = _build_html(points)

    OUTPUT_HTML.write_text(html, encoding="utf-8")

    png = _render_png()

    lines = [
        "<!-- Arquivo de teste local. Ignorado pelo git (ver .gitignore). -->",
        f"`{OR_KEY_LINE}`",
        "",
        f"Pontos plotados: {len(points)} (preço ≤ ${PRICE_MAX:.2f} por 1M tokens).",
        f"Corte: Agentic {SPLIT_AGENTIC:g} × Preço ${SPLIT_PRICE:g}.",
        "",
    ]
    if png is not None:
        # Imagem embutida: um .md aberto no navegador (ou em qualquer preview
        # de markdown) mostra o gráfico renderizado — <script> não roda em .md.
        b64 = base64.b64encode(png).decode("ascii")
        lines += [
            f"![Matriz de custo-benefício — Agentic Index](data:image/png;base64,{b64})",
            "",
        ]
    else:
        lines += [
            "Chrome não encontrado para gerar a imagem — abra o HTML standalone:",
            "",
        ]
    lines += [
        f"Gráfico interativo (hover/tooltip): abra `{OUTPUT_HTML.name}` no navegador.",
        "",
    ]
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"Preview (markdown) em {OUTPUT_MD} ({len(points)} pontos)")
    print(f"Preview (HTML)     em {OUTPUT_HTML}")
    print(f"Imagem embutida: {'sim' if png is not None else 'não (Chrome não encontrado)'}")


if __name__ == "__main__":
    main()
