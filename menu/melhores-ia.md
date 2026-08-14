---
layout: page
title: Melhores IA
permalink: /melhores-ia
---

Aqui listamos as melhores IAs para código, ranqueadas por critérios internos como eficiência e custo — priorizando modelos com bom desempenho em coding e melhor relação preço por ponto de capacidade.

Atualizado em: {{ site.data.leaderboard.updated_at }}
- [Fonte]({{ site.data.leaderboard.source_url }}){% endif %}

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
