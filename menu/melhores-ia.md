---
layout: page
title: Melhores IA
permalink: /melhores-ia
---

Aqui listamos as melhores IAs para código, ranqueadas por critérios internos como eficiência e custo — priorizando modelos com bom desempenho em coding e melhor relação preço por ponto de capacidade.

Atualizado em: {{ site.data.leaderboard.updated_at }}
- [Fonte]({{ site.data.leaderboard.source_url }})

Só entram modelos com índice de coding ≥ {{ site.data.leaderboard.min_coding_index }}. O ranking usa a **eficiência**:

`eficiencia = coding − {{ site.data.leaderboard.points_per_dollar }} × preço`

```text
+$1.00 de preço vale +{{ site.data.leaderboard.points_per_dollar }} pontos de coding. Em caso de empate no score, vence o menor gasto (preço / coding).
```

- **Coding**: índice de coding da Artificial Analysis via OpenRouter.
- **Preço**: soma de input + output por milhão de tokens.
- **Gasto**: preço dividido pelo índice de coding (desempate; menor = melhor).
- **Eficiência**: a fórmula acima; maior valor = melhor posição.

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
