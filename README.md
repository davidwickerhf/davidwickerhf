<a href="https://wicker.life">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/hero-dark-still.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/hero-light-still.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/hero-dark.svg">
    <img src="assets/hero-light.svg" width="1200" alt="David Wicker — developer and researcher in Maastricht, the Netherlands. Animated network artwork.">
  </picture>
</a>

<p align="center">
  <a href="https://wicker.life"><b>Portfolio ↗</b></a> &nbsp; / &nbsp;
  <a href="#selected-work">Selected work</a> &nbsp; / &nbsp;
  <a href="#research-contributions">Research code</a> &nbsp; / &nbsp;
  <a href="#datasets">Datasets</a> &nbsp; / &nbsp;
  <a href="#beyond-software">Beyond software</a> &nbsp; / &nbsp;
  <a href="https://wicker.life/collaborate">Get in touch ↗</a>
</p>

# I'm David.

Full-stack developer and researcher in **Maastricht, the Netherlands**. I build software for working with complex information: court decisions, Armenian texts, and personal knowledge.

At the [Brightlands Institute for Smart Society](https://www.biss-institute.com/en/team/david-wicker), I work on legal research infrastructure with the Maastricht research and engineering teams. Independently, I design and build language-learning tools, knowledge systems, and client websites.

<p>
  <a href="https://wicker.life/cv"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/button-cv-dark.svg"><img src="assets/button-cv-light.svg" width="90" height="42" alt="CV"></picture></a>
  <a href="https://wicker.life/research"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/button-research-dark.svg"><img src="assets/button-research-light.svg" width="132" height="42" alt="Research"></picture></a>
  <a href="https://www.linkedin.com/in/davidwickerhf/"><picture><source media="(prefers-color-scheme: dark)" srcset="assets/button-linkedin-dark.svg"><img src="assets/button-linkedin-light.svg" width="132" height="42" alt="LinkedIn"></picture></a>
</p>

## Selected work

<a href="https://wicker.life/research/case-law-explorer">
  <picture>
    <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/case-law-dark-still.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/case-law-light-still.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/case-law-dark.svg">
    <img src="assets/case-law-light.svg" width="1200" alt="01 — Case Law Explorer. From legal corpora to citations and discovery. Explore the architecture.">
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
    <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/hayeren-dark-still.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/hayeren-light-still.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/hayeren-dark.svg">
    <img src="assets/hayeren-light.svg" width="1200" alt="02 — Hayeren. Eastern Armenian: read, understand, remember. Explore the architecture.">
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
    <source media="(prefers-reduced-motion: reduce) and (prefers-color-scheme: dark)" srcset="assets/commonfold-dark-still.svg">
    <source media="(prefers-reduced-motion: reduce)" srcset="assets/commonfold-light-still.svg">
    <source media="(prefers-color-scheme: dark)" srcset="assets/commonfold-dark.svg">
    <img src="assets/commonfold-light.svg" width="1200" alt="03 — Commonfold. Personal knowledge: capture, review, recall. Explore the architecture.">
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

## Research contributions

- **[cellar-extractor](https://github.com/maastrichtlawtech/cellar-extractor)** — EU case-law extraction, multilingual full text, and citation relationships from CELLAR and EUR-Lex.
- **[echr-extractor](https://github.com/maastrichtlawtech/echr-extractor)** — European Court of Human Rights data from HUDOC, including full text, legal sections, and citation networks.
- **[ECtHR citation rankings](https://github.com/davidwickerhf/rankings)** — Code, data, and reproducible analyses for my research on how network centrality relates to the importance of court judgments.

The extraction libraries are developed with the [Maastricht Law & Tech Lab](https://github.com/maastrichtlawtech).

## Datasets

Legal data I publish on [Hugging Face](https://huggingface.co/davidwickerhf):

| Dataset | Contents |
| --- | --- |
| [CJEU / CELLAR](https://huggingface.co/datasets/davidwickerhf/cjeu-opendata) | EU case-law metadata, multilingual full text, and citation links. |
| [Rechtspraak OpenData](https://huggingface.co/datasets/davidwickerhf/rechtspraak-opendata) | Raw Dutch court-data snapshots and pipeline export archives. |
| [ECLI → BWB references](https://huggingface.co/datasets/davidwickerhf/ecli-bwb-id) | Links between Dutch court decisions and the legislation they cite. |
| **ECHR · coming soon** | European Court of Human Rights case law. |

[More projects and architecture notes ↗](https://wicker.life/projects)

## Beyond software

I photograph places and everyday life, study Eastern Armenian, and work on educational access for students affected by conflict. Earlier chapters include UWC Dilijan in Armenia and climate organising in Turin.

[Photography](https://wicker.life/photography) · [Humanitarian work](https://wicker.life/humanitarian-work) · [Earlier work](https://wicker.life/archive)

---

**Have a difficult system to make usable?** [Let's talk ↗](https://wicker.life/collaborate)

<sub>Original artwork, rendered from code. [Still version](README-STATIC.md) · [How this README works](DESIGN.md)</sub>
