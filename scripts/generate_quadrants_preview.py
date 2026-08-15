#!/usr/bin/env python3
"""Gera preview do gráfico de quadrantes com Chart.js."""

from __future__ import annotations

import json
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "_data" / "leaderboard.json"
OUTPUT = ROOT / "teste_quadrants.html"

SPLIT_PRICE = 4.0      # Eixo X invertido (Preço)
SPLIT_CODING = 60.0    # Eixo Y (Coding Index)


def main() -> None:
    with DATA.open(encoding="utf-8") as handle:
        payload = json.load(handle)

    points = [
        {
            "model": it.get("model", ""),
            "slug": it.get("model_id", ""),
            "x": float(it["price"]),
            "y": float(it["coding_index"]),
            "gasto": it.get("gasto_por_coding", ""),
            "eficiencia": it.get("eficiencia", ""),
        }
        for it in payload["items"]
        if it.get("price") not in (None, "—")
        and it.get("coding_index") not in (None, "—")
        and float(it["price"]) <= 20.0
    ]

    data_json = json.dumps(points, ensure_ascii=False)

    template = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Matriz de Eficiência — Coding Index vs Preço</title>
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
  <h2 style="margin-top: 0; margin-bottom: 6px;">Matriz de Eficiência de Modelos (Até $20.00)</h2>
  <p style="color: #666; margin-top: 0; font-size: 14px;">
    Coding Index (Y) × Preço por milhão de tokens (X, invertido). Quanto mais ao topo e à direita, melhor a relação benefício/custo.
  </p>

  <div class="chart-wrapper">
    <canvas id="quadrantsChart"></canvas>
  </div>

  <div class="legend-quadrants">
    <div class="legend-item q-top-left">
      <strong>Superior Esquerdo:</strong> Alta Capacidade / Alto Custo (Top de linha)
    </div>
    <div class="legend-item q-top-right">
      <strong>Superior Direito:</strong> 🏆 Melhor Custo-Benefício (Alta Capacidade + Baixo Custo)
    </div>
    <div class="legend-item q-bottom-left">
      <strong>Inferior Esquerdo:</strong> Baixa Eficiência (Custo Alto p/ capacidade)
    </div>
    <div class="legend-item q-bottom-right">
      <strong>Inferior Direito:</strong> Econômico (Entrada / Baixo Custo)
    </div>
  </div>
</div>

<script>
const DATA = __DATA_JSON__;
const SPLIT_PRICE = __SPLIT_PRICE__;
const SPLIT_CODING = __SPLIT_CODING__;

// Plugin de quadrantes (baseado em https://www.chartjs.org/docs/latest/samples/plugins/quadrants.html)
const quadrantsPlugin = {
  id: 'quadrants',
  beforeDraw(chart, args, options) {
    const { ctx, chartArea: { left, top, right, bottom }, scales: { x, y } } = chart;
    const splitX = x.getPixelForValue(options.splitX);
    const splitY = y.getPixelForValue(options.splitY);

    ctx.save();
    
    // Top Left (X > splitX, ou seja, mais caro pois é invertido, Y > splitY)
    ctx.fillStyle = options.topLeft || 'rgba(54, 162, 235, 0.08)';
    ctx.fillRect(left, top, splitX - left, splitY - top);

    // Top Right (X < splitX, ou seja, mais barato, Y > splitY)
    ctx.fillStyle = options.topRight || 'rgba(75, 192, 192, 0.16)';
    ctx.fillRect(splitX, top, right - splitX, splitY - top);

    // Bottom Left
    ctx.fillStyle = options.bottomLeft || 'rgba(255, 99, 132, 0.08)';
    ctx.fillRect(left, splitY, splitX - left, bottom - splitY);

    // Bottom Right
    ctx.fillStyle = options.bottomRight || 'rgba(255, 205, 86, 0.14)';
    ctx.fillRect(splitX, splitY, right - splitX, bottom - splitY);

    // Linhas pontilhadas divisórias
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

const ctx = document.getElementById('quadrantsChart').getContext('2d');
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
        coding: item.y,
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
        reverse: true, // ESCALA X INVERTIDA (menor preço fica à direita!)
        min: 0,
        max: 20,
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
        min: 35,
        max: 85,
        title: {
          display: true,
          text: 'Coding Index (Capacidade)',
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
              `Coding Index: ${raw.coding.toFixed(2)}`,
              `Preço: $${raw.price.toFixed(2)} / 1M tokens`,
              `Eficiência: ${raw.eficiencia}`,
              `Gasto por coding: ${raw.gasto}`
            ];
          }
        }
      },
      quadrants: {
        splitX: SPLIT_PRICE,
        splitY: SPLIT_CODING,
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
    html = html.replace("__SPLIT_CODING__", str(SPLIT_CODING))

    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Preview gerado em {OUTPUT}")


if __name__ == "__main__":
    main()
