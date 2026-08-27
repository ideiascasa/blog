---
layout: page
title: Melhores IA
permalink: /melhores-ia
---

- Atualizado em: {{ site.data.leaderboard.updated_at }}
- {{ site.data.leaderboard.citation }}

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<div markdown="0" style="position: relative; background: #ffffff; border: 1px solid #e1e4e8; border-radius: 8px; padding: 16px; margin: 24px 0; box-shadow: 0 2px 8px rgba(0,0,0,0.04); color: #222;">
<h3 style="margin-top: 0; margin-bottom: 6px; font-size: 18px; font-weight: bold; border-bottom: none;">Matriz de Custo-Benefício dos Modelos</h3>
<p style="color: #666; margin-top: 0; font-size: 14px; line-height: 1.4;">
Coding Index (Y) × Preço por milhão de tokens (X, invertido). Quanto mais ao topo e à direita, melhor a relação capacidade/preço. A matriz usa valores factuais sem nenhum cálculo. O corte de 60 pontos vs 4$ é empirico.
</p>
<div style="position: relative; height: 500px; width: 100%;">
<canvas id="quadrantsChart"></canvas>
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin-top: 15px; font-size: 13px;">
<div style="padding: 8px 12px; border-radius: 6px; background: rgba(54, 162, 235, 0.12); border-left: 4px solid rgb(54, 162, 235); display: flex; align-items: center; gap: 8px;">
<strong>Superior Esquerdo:</strong> Alta Capacidade / Alto Custo (Top de linha / Premium)
</div>
<div style="padding: 8px 12px; border-radius: 6px; background: rgba(75, 192, 192, 0.15); border-left: 4px solid rgb(75, 192, 192); display: flex; align-items: center; gap: 8px;">
<strong>Superior Direito:</strong> 🏆 Melhor Custo-Benefício (Alta Capacidade + Baixo Custo)
</div>
<div style="padding: 8px 12px; border-radius: 6px; background: rgba(255, 99, 132, 0.12); border-left: 4px solid rgb(255, 99, 132); display: flex; align-items: center; gap: 8px;">
<strong>Inferior Esquerdo:</strong> Baixa Eficiência (Custo Alto para a capacidade oferecida)
</div>
<div style="padding: 8px 12px; border-radius: 6px; background: rgba(255, 205, 86, 0.18); border-left: 4px solid rgb(255, 205, 86); display: flex; align-items: center; gap: 8px;">
<strong>Inferior Direito:</strong> Econômico (Entrada / Baixo Custo)
</div>
</div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
const rawItems = {{ site.data.leaderboard.items | jsonify }};
const DATA = rawItems
.filter(item => item.price && item.price !== "—" && item.coding_index && item.coding_index !== "—" && parseFloat(item.price) <= 20.0)
.map(item => ({
model: item.model,
slug: item.model_id,
x: parseFloat(item.price),
y: parseFloat(item.coding_index),
gasto: item.gasto_por_coding,
eficiencia: item.eficiencia
}));

const SPLIT_PRICE = 4.0;
const SPLIT_CODING = 60.0;

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
reverse: true,
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
});
</script>

<table>
  <thead>
    <tr>
      <th>Rank</th>
      <th>Modelo</th>
      <th>Slug</th>
      <th>Coding</th>
      <th>Preço</th>
      <th>Gasto</th>
      <th>Eficiencia</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.leaderboard.items %}
    <tr>
      <td>{{ item.rank }}</td>
      <td>{{ item.model }}</td>
      <td><code>{{ item.model_id }}</code></td>
      <td>{{ item.coding_index }}</td>
      <td>{% if item.price %}${{ item.price }}{% else %}—{% endif %}</td>
      <td>{{ item.gasto_por_coding }}</td>
      <td>{{ item.eficiencia }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

Aqui listamos as melhores IAs para código, ranqueadas por critérios internos como eficiência e custo — priorizando modelos com bom desempenho em coding e melhor relação preço por ponto de capacidade.

Só entram modelos com índice de coding ≥ {{ site.data.leaderboard.min_coding_index }}. O ranking usa a **eficiência**:

```text
eficiencia = coding − {{ site.data.leaderboard.points_per_dollar }} × preço

+$1.00 de preço vale +{{ site.data.leaderboard.points_per_dollar }} pontos de coding. Em caso de empate no score, vence o menor gasto (preço / coding).
```

- **Coding**: índice de coding da Artificial Analysis via OpenRouter.
- **Preço**: soma de input + output por milhão de tokens.
- **Gasto**: preço dividido pelo índice de coding (desempate; menor = melhor).
- **Eficiência**: a fórmula acima; maior valor = melhor posição.
