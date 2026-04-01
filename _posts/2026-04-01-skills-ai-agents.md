---
layout: post
title: "Desenvolvimento de Aplicações Java Assistido por IA com Agent Skills"
author: "Siva Katamreddy"
categories: blog
tags: [blog,ai,ai-agents,junie,spring-boot]
image: skills-ai-agents-featured.png
---

O desenvolvimento assistido por agentes está rapidamente se tornando um modo comum de desenvolvimento de software. Novas técnicas estão surgindo para ajudar os LLMs a gerar código que corresponda às suas preferências e padrões.

Uma abordagem comum é criar um arquivo `AGENTS.md`, `CLAUDE.md` ou `GEMINI.md` com detalhes do projeto, instruções de build e diretrizes de codificação. O agente de IA carrega esse arquivo no contexto em cada solicitação.

Isso tem duas desvantagens:

- Consome tokens em cada solicitação, aumentando o custo.
- Carregar muito contexto em um LLM degrada sua eficácia.

[Agent Skills](https://agentskills.io/) é uma nova iniciativa que resolve ambos os problemas gerenciando o contexto progressivamente e estendendo as capacidades do agente de IA sob demanda.

---

## O que são Agent Skills?

Agent Skills é um padrão aberto introduzido pela Anthropic para estender as capacidades dos agentes de IA com conhecimento especializado e fluxos de trabalho.

Considere um caso de uso em que você deseja que uma IA gere apresentações usando o modelo de slides e as diretrizes de design da sua empresa. Você pode empacotar esses ativos (o modelo PPT, arquivos de fontes e regras de design) em uma skill. O agente então usa essa skill para gerar slides que correspondem aos seus padrões automaticamente.

Uma skill é uma pasta contendo um arquivo `SKILL.md`. Este arquivo inclui metadados (`name` e `description` no mínimo) e instruções que dizem ao agente como executar uma tarefa específica. Skills também podem incluir scripts, templates e materiais de referência.

```
skill-name/
├── SKILL.md          # Obrigatório: instruções + metadados
├── scripts/          # Opcional: código executável
├── references/       # Opcional: documentação
└── assets/           # Opcional: templates, recursos
```

O formato de um arquivo `SKILL.md` é:

```yaml
---
name: nome-da-skill
description: Descrição da skill.
license: Apache-2.0
metadata:
  author: autor/org
  version: "1.0"
compatibility: Requer git, docker, jq e acesso à internet
---
Conteúdo da Skill
```

Em um arquivo `SKILL.md`, `name` e `description` são campos obrigatórios, e você pode adicionar campos opcionais como `licence`, `metadata`, `compatibility`, etc. Você pode explorar mais sobre a especificação de Skills [aqui](https://agentskills.io/specification).

---

## Como as Agent Skills gerenciam o contexto?

Na inicialização, os agentes carregam apenas os metadados (`name` e `description`) das skills instaladas. Quando você pede ao agente para executar uma tarefa, ele encontra a skill relevante e carrega apenas aquele `SKILL.md` no contexto.

Esse carregamento progressivo mantém o contexto mínimo e traz informações adicionais apenas quando necessário, diferente de um `CLAUDE.md` monolítico que carrega tudo de uma vez.

---

## O que pode ser uma skill?

Skills estendem as capacidades da IA em uma ampla variedade: desde diretrizes de codificação para uma biblioteca específica, até fluxos de trabalho passo a passo com documentos de referência e scripts auxiliares.

Por exemplo, você pode criar uma skill que:

- Especifica quais APIs de biblioteca usar e quais anti-patterns evitar.
- Inclui documentação de referência em um diretório `references/`.
- Inclui scripts auxiliares em um diretório `scripts/`.

---

## Estudo de Caso: Implementando Paginação com Spring Data JPA

Suponha que você peça a um agente de IA para implementar um endpoint de API REST Spring Boot que retorne uma lista paginada de entidades `Post` juntamente com suas coleções de `Comment`.

Sem orientação, o agente provavelmente produzirá um destes erros comuns:

- **Problema N+1 SELECT** — o carregamento lento (lazy loading) dos comentários dispara uma consulta separada por post.
- **Paginação em memória** — usar `JOIN FETCH` com paginação carrega todas as linhas na memória e depois pagina na camada da aplicação.

Você pode conferir o código de exemplo no repositório do GitHub [https://github.com/sivaprasadreddy/agent-skills-demo](https://github.com/sivaprasadreddy/agent-skills-demo)

Vamos ver como um Agente de IA pode gerar código quando solicitado a implementar um endpoint de API REST para retornar posts paginados com comentários.

Sem diretrizes ou skills específicas, o Agente de IA gerou a seguinte implementação:

```java
@RestController
@RequestMapping("/api/posts")
class PostController {
    private final PostService postService;

    PostController(PostService postService) {
        this.postService = postService;
    }

    @GetMapping
    PagedResult<PostDto> getPosts(
            @RequestParam(name = "page", defaultValue = "1") int pageNo,
            @RequestParam(name = "size", defaultValue = "10") int pageSize) {
        return postService.getPosts(pageNo, pageSize);
    }
}

@Service
@Transactional(readOnly = true)
public class PostService {
    private final PostRepository postRepository;

    public PostService(PostRepository postRepository) {
        this.postRepository = postRepository;
    }

    public PagedResult<PostDto> getPosts(int pageNo, int pageSize) {
        Sort sort = Sort.by(Sort.Direction.ASC, "id");
        Pageable pageable = PageRequest.of(
                pageNo <= 0 ? 0 : pageNo - 1, pageSize, sort);
        Page<PostDto> postPage = postRepository
                .findAllWithComments(pageable).map(PostDto::from);
        return PagedResult.from(postPage);
    }
}
```

Se você executar a aplicação e invocar o endpoint `GET /api/posts`, você obterá os resultados, mas nos logs encontrará o seguinte WARNING:

```
HHH000104: firstResult/maxResults specified with collection fetch; applying in memory
```

Isso essencialmente significa que o Hibernate carregará todas as entidades na memória e depois aplicará a paginação. Isso resultará em baixo desempenho e até exceções `OutOfMemory` se houver um grande número de linhas na tabela `posts`.

<video src="/assets/img/skills-ai-junie-without.webm" width="740" autoplay loop muted playsinline></video>

Uma skill de Spring Data JPA previne ambos os problemas fornecendo ao agente diretrizes explícitas e um exemplo de código funcional.

---

## Agent Skill para Spring Data JPA

Crie um arquivo `spring-data-jpa/SKILL.md` com o seguinte conteúdo:

```markdown
---
name: spring-data-jpa-skill
description: Implementar a camada de persistência usando Spring Data JPA
  em aplicações Spring Boot.
---

Siga os princípios abaixo ao usar Spring Data JPA:

1. Desabilite o filtro Open Session in View (OSIV):
   spring.jpa.open-in-view=false

2. Desabilite a paginação em memória:
   spring.jpa.properties.hibernate.query.fail_on_pagination_over_collection_fetch=true

3. Evite o problema N+1 SELECT: use JOIN FETCH para carregar
   coleções filhas associadas em uma única consulta.

4. Evite paginação em memória: ao carregar uma lista paginada
   de entidades pai com coleções filhas:
   * Primeiro, carregue apenas os IDs das entidades pai usando paginação
   * Depois, carregue as entidades completas com suas coleções filhas
     usando JOIN FETCH para esses IDs
   * Monte a Page final a partir dos IDs paginados e das entidades carregadas

## Exemplo de paginação com coleções filhas:

PostRepository.java

public interface PostRepository extends JpaRepository<Post, Long> {

    @Query("select p.id from Post p order by p.id")
    Page<Long> findPostIds(Pageable pageable);

    @Query("select distinct p from Post p left join fetch p.comments where p.id in :ids")
    List<Post> findAllByIdInWithComments(@Param("ids") Collection<Long> ids);
}

PostService.java

@Service
public class PostService {
    private final PostRepository postRepository;

    public PostService(PostRepository postRepository) {
        this.postRepository = postRepository;
    }

    @Transactional(readOnly = true)
    public Page<Post> findPosts(Pageable pageable) {
        Page<Long> idsPage = postRepository.findPostIds(pageable);
        if (idsPage.isEmpty()) {
            return Page.empty(pageable);
        }
        List<Post> posts = postRepository
                .findAllByIdInWithComments(idsPage.getContent());
        return new PageImpl<>(posts, pageable, idsPage.getTotalElements());
    }
}
```

---

## Como usar Agent Skills?

Agent Skills funcionam com Claude Code, Codex, Gemini CLI, JetBrains Junie e outros agentes. Instale uma skill no nível do projeto ou no nível do usuário, dependendo da sua preferência.

| Agente | Nível do Projeto | Nível do Usuário |
|--------|-------------------|-------------------|
| Junie | `.junie/skills/` | `~/.junie/skills/` |
| Claude | `.claude/skills/` | `~/.claude/skills/` |
| Codex / Outros | `.agents/skills/` | `~/.agents/skills/` |
| Gemini | `.gemini/skills/` | `~/.gemini/skills/` |

Para usar a skill de Spring Data JPA com Claude Code:

1. Copie o diretório `spring-data-jpa/` para `{raiz-do-projeto}/.claude/skills/`.
2. Peça ao Claude Code para implementar um endpoint de API REST paginado.
3. O Claude Code descobre a skill automaticamente e segue as diretrizes.

Como você pode ver, o Claude Code descobriu automaticamente a skill de Spring Data JPA e gerou a seguinte implementação seguindo as diretrizes fornecidas na skill.

```java
@Service
public class PostService {
    private final PostRepository postRepository;

    public PostService(PostRepository postRepository) {
        this.postRepository = postRepository;
    }

    @Transactional(readOnly = true)
    public Page<Post> findPosts(Pageable pageable) {
        Page<Long> idPage = postRepository.findPostIds(pageable);
        if (idPage.isEmpty()) {
            return Page.empty(pageable);
        }
        List<Post> posts = postRepository
                .findAllByIdInWithComments(idPage.getContent());
        return new PageImpl<>(posts, pageable, idPage.getTotalElements());
    }
}
```

<video src="/assets/img/skills-ai-claude-demo.webm" width="740" autoplay loop muted playsinline></video>

Com esta implementação, apenas os IDs dos Posts da página desejada serão carregados primeiro, e depois uma lista de posts junto com seus comentários será buscada em uma consulta separada. Isso corrigirá o problema de paginação em memória.

---

## Usando Agent Skills com Junie

Você pode usar o agente [JetBrains Junie](https://junie.jetbrains.com/) para gerar código que carrega automaticamente as skills necessárias do diretório `.junie/skills`.

O agente Junie carregou a skill `spring-data-jpa` com base na tarefa fornecida e aplicou as diretrizes. Você também pode observar que o Junie executa automaticamente os testes relevantes para verificar se o código gerado está funcionando ou não e itera até que os testes sejam aprovados.

<video src="/assets/img/skills-ai-junie-with.webm" width="740" autoplay loop muted playsinline></video>

No repositório de exemplo [https://github.com/sivaprasadreddy/agent-skills-demo](https://github.com/sivaprasadreddy/agent-skills-demo), você pode encontrar as seguintes branches para experimentar a Agent Skill `spring-data-jpa`:

- **main**: Ponto de partida para tentar implementar o caso de uso mencionado sem nenhuma skill.
- **in-memory-pagination-issue**: Implementação do caso de uso gerada por IA que resulta no problema de paginação em memória.
- **skills**: Com a skill `spring-data-jpa` para tentar implementar o caso de uso mencionado.

---

## Resumo

Se o agente de IA está gerando código com anti-patterns ou não seguindo os padrões e convenções de codificação da equipe, em vez de corrigir problemas um a um com prompts de acompanhamento, considere criar uma skill para fornecer essas orientações como diretrizes.

Para explorar mais sobre Agent Skills, consulte os seguintes recursos:

- [https://agentskills.io/](https://agentskills.io/)
- [Documentação Claude - Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)
- [OpenAI Codex - Skills](https://developers.openai.com/codex/skills/)
- [Gemini CLI - Skills](https://geminicli.com/docs/cli/skills/)
- [JetBrains Junie - Agent Skills](https://junie.jetbrains.com/docs/agent-skills.html)

---

> **Fonte original:** [AI-Assisted Java Application Development with Agent Skills](https://blog.jetbrains.com/idea/2026/03/ai-assisted-java-application-development-with-agent-skills/) - JetBrains Blog, por Siva Katamreddy.
