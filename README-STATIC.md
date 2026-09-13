<a href="https://wicker.life">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/hero-dark.png">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/hero-light.png">
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.png">
    <img src="assets/hero-light.png" width="1200" alt="David Wicker — making complex information useful to people. A rotating network connects legal research, language, and knowledge.">
  </picture>
</a>

<p align="center">
  <a href="https://wicker.life"><b>Portfolio ↗</b></a> &nbsp; / &nbsp;
  <a href="#selected-work">Selected work</a> &nbsp; / &nbsp;
  <a href="#public-code">Public code</a> &nbsp; / &nbsp;
  <a href="#beyond-software">Beyond software</a> &nbsp; / &nbsp;
  <a href="https://wicker.life/collaborate">Get in touch ↗</a>
</p>

# I'm David.

Full-stack developer and researcher in **Maastricht, the Netherlands**. I build software for working with complex information: court decisions, Armenian texts, and personal knowledge.

At the [Brightlands Institute for Smart Society](https://www.biss-institute.com/en/team/david-wicker), I work on legal research infrastructure with the Maastricht research and engineering teams. Independently, I design and build language-learning tools, knowledge systems, and client websites.

[CV](https://wicker.life/cv) · [Research](https://wicker.life/research) · [LinkedIn](https://www.linkedin.com/in/davidwickerhf/)

## Selected work

<a href="https://wicker.life/research/case-law-explorer">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/case-law-dark.png">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/case-law-light.png">
    <source media="(prefers-color-scheme: dark)" srcset="assets/case-law-dark.png">
    <img src="assets/case-law-light.png" width="1200" alt="01 — Case Law Explorer. From legal corpora to citations and discovery. Explore the architecture.">
  </picture>
</a>

Research software connecting Dutch and European case law through search and citation networks. I contribute across ingestion, data normalization, APIs, authentication, the research interface, and deployment.

`Python` · `Airflow` · `PostgreSQL` · `SvelteKit` · `Docker`

<details>
<summary><b>Inside the system</b> — from court records to a research workspace</summary>

Rechtspraak, HUDOC, and CELLAR enter through separate ingestion paths and converge on a shared legal-data model. Source-specific records and citation relationships remain traceable. The work is part of a wider BISS and Maastricht research programme.

```mermaid
flowchart LR
  A[Rechtspraak] --> D[Ingest & normalize]
  B[HUDOC] --> D
  C[CELLAR] --> D
  D --> E[(PostgreSQL)]
  E --> F[Search & citation APIs]
  F --> G[Research workspace]
```

[Read the architecture](https://wicker.life/research/case-law-explorer) · [Explore the ingestion code](https://github.com/maastrichtlawtech/cellar-extractor)

</details>

<br>

<a href="https://wicker.life/projects/hayeren">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/hayeren-dark.png">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/hayeren-light.png">
    <source media="(prefers-color-scheme: dark)" srcset="assets/hayeren-dark.png">
    <img src="assets/hayeren-light.png" width="1200" alt="02 — Hayeren. Eastern Armenian: read, understand, remember. Explore the architecture.">
  </picture>
</a>

An Eastern Armenian learning platform, shaped by my own experience learning the language. A graded course, grammar, a dictionary that recognizes inflected words, reading, spaced repetition, and shared notebooks all draw on the same language data.

`TypeScript` · `React` · `Neon Postgres` · `Liveblocks` · `Yjs`

<details>
<summary><b>Inside the system</b> — one word, across every learning surface</summary>

A word encountered in a text resolves to a stable dictionary entry. That same record supports lookup, study, and review. Shared packages hold the language and learning logic; Postgres preserves learner progress and notes.

```mermaid
flowchart LR
  A[Word in a text] --> B[Dictionary entry]
  B --> C[Reader]
  B --> D[Course & grammar]
  B --> E[Spaced repetition]
  C --> F[(Progress & notes)]
  D --> F
  E --> F
```

[Read the architecture](https://wicker.life/projects/hayeren) · [Try Hayeren](https://hayeren.io)

</details>

<br>

<a href="https://wicker.life/projects/commonfold">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/commonfold-dark.png">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/commonfold-light.png">
    <source media="(prefers-color-scheme: dark)" srcset="assets/commonfold-dark.png">
    <img src="assets/commonfold-light.png" width="1200" alt="03 — Commonfold. Personal knowledge: capture, review, recall. Explore the architecture.">
  </picture>
</a>

A private knowledge system in active development. AI proposes changes for review and answers questions with links to their sources. Notes support collaborative editing, version history, and portable Markdown export.

`Next.js` · `PostgreSQL / pgvector` · `Claude` · `TipTap` · `Yjs`

<details>
<summary><b>Inside the system</b> — review what enters, trace what comes back</summary>

Capture starts with a proposal. After review, the note becomes part of a Postgres archive. Keyword and semantic retrieval supply evidence for answers; version history and Markdown export keep the archive recoverable.

```mermaid
flowchart LR
  A[Thought or source] --> B[Proposed change]
  B --> C[Human review]
  C --> D[(Note archive)]
  D --> E[Retrieval]
  E --> F[Answer with sources]
  D --> G[Markdown export]
```

[Read the architecture](https://wicker.life/projects/commonfold) · [Visit Commonfold](https://commonfold.space)

</details>

## Public code

A few entry points into my research software and contributions:

| Repository | What it does |
| --- | --- |
| [cellar-extractor](https://github.com/maastrichtlawtech/cellar-extractor) | Extracts and enriches EU case law with full text, metadata, and citation relationships. |
| [cjeu-migration](https://github.com/davidwickerhf/cjeu-migration) | Runs resumable case-law extraction and publishes research datasets to Hugging Face. |
| [metricanalysis](https://github.com/davidwickerhf/metricanalysis) | Compares graph centrality measures against reference data. |

[More projects and architecture notes ↗](https://wicker.life/projects)

## Beyond software

I photograph places and everyday life, study Eastern Armenian, and work on educational access for students affected by conflict. Earlier chapters include UWC Dilijan in Armenia and climate organising in Turin.

[Photography](https://wicker.life/photography) · [Humanitarian work](https://wicker.life/humanitarian-work) · [Earlier work](https://wicker.life/archive)

---

**Have a difficult system to make usable?** [Let's talk ↗](https://wicker.life/collaborate)

<sub>Original artwork, rendered from code. [Animated version](README.md) · [How this README works](DESIGN.md)</sub>
