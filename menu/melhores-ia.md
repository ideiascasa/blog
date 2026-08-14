---
layout: page
title: Melhores IA
permalink: /melhores-ia
---

Ranking de modelos de IA para coding (Artificial Analysis via OpenRouter), ordenado por Coding Index.

Atualizado em: {{ site.data.leaderboard.updated_at }}
{% if site.data.leaderboard.as_of %} · Dados em: {{ site.data.leaderboard.as_of }}{% endif %}
{% if site.data.leaderboard.source_url %} · [Fonte]({{ site.data.leaderboard.source_url }}){% endif %}

<table>
  <thead>
    <tr>
      <th>Rank</th>
      <th>Modelo</th>
      <th>Slug</th>
      <th>Coding Index</th>
      <th>Intelligence</th>
      <th>Agentic</th>
      <th>Input/1M</th>
      <th>Output/1M</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.leaderboard.items %}
    <tr>
      <td>{{ item.rank }}</td>
      <td>{{ item.model }}</td>
      <td><code>{{ item.model_id }}</code></td>
      <td>{{ item.coding_index }}</td>
      <td>{% if item.intelligence_index %}{{ item.intelligence_index }}{% else %}—{% endif %}</td>
      <td>{% if item.agentic_index %}{{ item.agentic_index }}{% else %}—{% endif %}</td>
      <td>{% if item.price_input %}${{ item.price_input }}{% else %}—{% endif %}</td>
      <td>{% if item.price_output %}${{ item.price_output }}{% else %}—{% endif %}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>
