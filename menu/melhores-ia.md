---
layout: page
title: Melhores IA
permalink: /melhores-ia
---

Aqui listamos as melhores IAs para código, ranqueadas por critérios internos como eficiência e custo — priorizando modelos com bom desempenho em coding e melhor relação preço por ponto de capacidade.

Atualizado em: {{ site.data.leaderboard.updated_at }}
- [Fonte]({{ site.data.leaderboard.source_url }})

Só entram modelos com índice de coding ≥ {{ site.data.leaderboard.min_coding_index }}. O ranking usa a **eficiência**:

`eficiencia = coding^α / preço^β`

```text
com α = {{ site.data.leaderboard.coding_alpha }} e β = {{ site.data.leaderboard.price_beta }} (razão α/β ≈ 14.5). A calibração faz com que +3 pontos de coding equivalam a cerca de +$0.50 de preço — assim um modelo como Luna (71 @ $0.70) fica acima de Gemini (76 @ $2.25).
```

- **Coding**: índice de coding da Artificial Analysis via OpenRouter.
- **Preço**: soma de input + output por milhão de tokens.
- **Gasto**: preço dividido pelo índice de coding.
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
