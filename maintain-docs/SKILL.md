---
name: maintain-docs
description: Create, organize, maintain, or audit repository documentation as a coherent system. Use when the user asks to add or revise docs, reorganize documentation, improve structure or flow, fix references or formatting, reduce duplication, reconcile docs with code, or audit stale/inconsistent documentation. Determine the authoritative home for information before writing, prefer updating existing docs over creating new ones, and preserve project-specific documentation architecture.
---

# Maintain Docs

## Goal

Keep repository documentation coherent, useful, current, and easy to navigate.

Documentation is a system, not a collection of Markdown files. Before creating or changing anything, understand the repository's existing documentation architecture, the intended reader, and the authoritative home for the information.

Minimize documentation surface area while preserving the information future readers actually need.

## 1. Inspect Before Writing

Before creating or modifying documentation:

- inspect existing documentation structure,
- read any documentation policy or repository guidance,
- identify related authoritative documents,
- check README or index files that provide navigation,
- inspect relevant code/configuration when documentation accuracy depends on implementation,
- determine whether the requested information already exists elsewhere.

Do not create a new document merely because the requested content is new to the current file.

Prefer extending an existing authoritative document when responsibilities overlap.

## 2. Determine the Document's Responsibility

Before writing, identify what role the content serves.

Common document roles include:

- **Tutorial** — teaches a beginner through a guided learning experience.
- **How-to** — helps a reader complete a specific task.
- **Reference** — provides precise facts, interfaces, schemas, commands, or configuration.
- **Explanation** — provides rationale, concepts, architecture, or background.
- **Operating rules** — concise mandatory instructions for active work.
- **Roadmap/planning** — future work, sequencing, milestones, or status.
- **Contract/specification** — binding requirements or interfaces.
- **Decision/history** — records why a consequential choice was made.
- **Navigation** — points readers to authoritative sources without duplicating them.

Do not mix roles unnecessarily.

When content belongs to a different document type than the target file, move or reference it rather than forcing it into the wrong place.

## 3. Choose the Authoritative Home

One concept should have one authoritative home whenever practical.

Before adding information, decide:

- where the canonical version should live,
- which other documents should reference it,
- whether existing duplicate content should be removed or replaced with links.

Do not copy the same rule, explanation, command, schema, or decision into multiple docs unless duplication is intentionally required for usability.

If duplication is necessary, keep one source authoritative and make the relationship explicit.

For repository-wide audits or reorganizations, record the result as a source-of-truth matrix before making broad changes. At minimum, include the topic, its authoritative document, and any documents that should link to it rather than duplicate it.

Example:

| Topic | Authoritative document | Other docs |
|---|---|---|
| Fly ingest operations | `scripts/ingest/README.md` | Link only |
| Data refresh workflow | `docs/core/runbook.md` | Link only |
| Local data processing | `data_pipeline/README.md` | Link only |
| Database import commands | `backend/README.md` | Link only |

Use the matrix to identify conflicting sources, guide edits, and verify that each affected topic still has one canonical home after the audit.

## 4. Use the Existing Documentation Architecture

Follow the repository's established documentation structure.

Do not impose a generic `/docs/core`, `/docs/reference`, Diátaxis, ADR, or other structure when the repository already defines a different system.

Use external documentation frameworks as decision aids, not as mandatory folder layouts.

If the existing architecture is unclear or materially dysfunctional, explain the issue and propose a structure before broadly reorganizing files.

## 5. Create or Extend Documentation

When the task is to create or expand documentation:

1. identify the reader and purpose,
2. determine the correct document type,
3. choose the authoritative home,
4. inspect related docs to avoid duplication,
5. write only the information needed for that responsibility,
6. add references to related authoritative material,
7. update navigation when necessary.

Prefer concise documents with clear boundaries over catch-all files.

Do not create supporting documents, indexes, examples, or reference pages unless they materially improve usability.

## 6. Maintain or Audit Documentation

When the task is to maintain or audit existing docs, check for:

- stale behavior descriptions,
- commands that no longer match the repository,
- outdated architecture,
- broken or stale links,
- orphaned documents,
- duplicated authoritative content,
- contradictory instructions,
- obsolete terminology,
- incorrect file paths,
- references to renamed or removed files,
- content that belongs in a different document,
- README navigation that no longer matches the docs,
- project rules or agent instructions that reference obsolete docs.

Verify important claims against the current code, configuration, schemas, or contracts when practical.

Do not infer that a recently modified document is current merely because its timestamp is recent.

## 7. Keep Operating Docs Small

Documents loaded routinely by agents or developers should contain only information needed during active work.

Prefer:

- short mandatory rules,
- direct constraints,
- clear references to deeper material.

Move long explanations, examples, historical discussion, rationale, or detailed guidance into reference material when they are not needed for routine execution.

Do not force verbose roadmaps, contracts, specifications, or reference guides into active agent context unless the task requires them.

## 8. Organize for Reader Flow

Organize content according to what the reader needs to understand or accomplish, not the chronology in which the content was written.

Use:

- descriptive headings,
- consistent hierarchy,
- short introductory context where needed,
- sections with clear responsibilities,
- logical progression,
- links to prerequisite or deeper material.

Avoid:

- heading structures that merely partition unrelated bullets,
- long documents without navigation,
- repeated context at the start of every section,
- unexplained jumps between concepts,
- buried prerequisites or warnings.

For workflow documents, distinguish the document's structure from the
execution sequence. Use headings to identify major phases and meaningful
alternative paths, and use descriptive unnumbered headings for steps,
subprocedures, operations, and reference material. Numbering every subsection
usually adds noise rather than navigation value.

When a workflow map is useful, populate it with distinct user goals and link
to the relevant phases or paths. Do not enumerate every internal handoff or
subprocedure in the map; readers can follow those within the selected path.
If a summary table is removed, preserve any distinct goals it contained in the
primary workflow map rather than deleting useful navigation.

Use consistent role labels when they improve scanning, such as `Required`,
`Optional`, `Operations`, and `Reference`. Make the labels and terminology in
the map match the corresponding headings and links.

For long reference documents, add a table of contents when it materially improves navigation.

## 9. Maintain Cross-References

When creating, renaming, moving, consolidating, or deleting documentation:

- find inbound references,
- update relative links,
- update README/index navigation,
- update agent instructions when applicable,
- update references in related docs,
- remove references to deleted files.

Do not leave redirects or compatibility files merely to preserve old documentation paths unless there is a real external dependency.

For solo or early-stage repositories, prefer updating references cleanly over preserving unnecessary legacy documentation paths.

## 10. Keep Formatting Consistent

Follow the repository's existing Markdown and documentation conventions when present.

Keep formatting consistent for:

- heading levels,
- lists,
- code blocks,
- tables,
- links,
- file paths,
- command examples,
- terminology.

Use fenced code blocks with appropriate language identifiers.

Use relative links for repository-local documentation when practical.

Do not make broad formatting-only changes outside the requested scope unless they are necessary to restore consistency.

## 11. Keep Examples and Commands Trustworthy

Examples should reflect current repository behavior.

When documenting commands:

- use the project's actual package manager and tooling,
- use established environment-variable names,
- avoid placeholders when the repository already defines real configuration conventions,
- distinguish destructive or expensive commands,
- prefer the narrowest command that accomplishes the documented task.

Do not document broad validation or execution commands merely because they are more comprehensive.

If a command may take significant time, cost money, mutate data, or require external infrastructure, say so.

## 12. Separate Facts, Guidance, and History

Make clear whether content represents:

- current required behavior,
- recommended practice,
- explanatory rationale,
- historical context,
- future work.

Do not leave obsolete decisions written as though they are current.

When historical information remains useful, label it as historical rather than mixing it with active instructions.

Roadmaps should describe planned work; they should not silently become architecture specifications.

## 13. Reconcile Documentation After Changes

After modifying documentation, check whether the change requires updates elsewhere.

Look for:

- renamed concepts,
- changed paths,
- altered commands,
- moved sections,
- duplicated content that is now obsolete,
- navigation that points to the wrong place,
- agent instructions that reference old files,
- contracts or specs that now conflict with descriptive docs.

Do not assume a documentation change is complete because the target file reads well in isolation.

## 14. Avoid Documentation Bloat

Every document creates maintenance cost.

Before creating a new file, ask:

- does this information already have an authoritative home?
- is the content substantial enough to justify a separate file?
- does a distinct reader or workflow need it?
- will future readers know when to use it?
- can the same goal be achieved with a concise section or reference?

Do not create documentation for obvious implementation details, transient work, or hypothetical future needs.

Prefer fewer, better-organized documents over exhaustive coverage.

## 15. Respect Scope and Authorization

Documentation work does not authorize unrelated code or configuration changes.

If the user asks a documentation question, answer it without editing files unless the same message explicitly requests changes.

If documentation reveals a code defect, stale implementation, or architecture problem:

- report it,
- identify the affected documentation,
- do not fix the code unless separately authorized.

Do not silently broaden a documentation task into repository cleanup.

## 16. Audit Output

When performing a documentation audit rather than making edits, prioritize findings by impact.

Focus on:

- incorrect or misleading information,
- contradictions,
- stale instructions,
- broken navigation,
- duplicated sources of truth,
- missing prerequisites,
- references to nonexistent files or behavior.

De-emphasize purely stylistic preferences unless they materially harm readability or consistency.

Do not invent findings to make the audit appear thorough.

## Completion Standard

Before considering documentation work complete, verify that:

- the content has a clear purpose and reader,
- information lives in the appropriate authoritative document,
- duplicate sources of truth were avoided,
- related references and links remain valid,
- headings and flow are coherent,
- commands/examples match current project behavior,
- stale or historical material is clearly distinguished,
- documentation architecture remains consistent,
- no unnecessary new documents were introduced.

## Key Principle

Put each piece of information in the one place where future readers will expect to find and maintain it.

## Attribution

This skill was adapted from concepts and workflow patterns in:

- `technical-documentation` from `magnus919/agent-skills`: https://github.com/magnus919/agent-skills/tree/main/technical-documentation
- `maintaining-core-documentation` from `derailed-dash/dazbo-agent-skills`: https://github.com/derailed-dash/dazbo-agent-skills/tree/main/skills/maintaining-core-documentation
- Diátaxis documentation framework: https://github.com/evildmp/diataxis-documentation-framework
- `technical-documentation` from `JPeetz/agent-skills`: https://github.com/JPeetz/agent-skills/tree/main/technical-documentation
- Agent Skill authoring and progressive-disclosure patterns from OpenAI and Superpowers.

See each upstream source for its complete license terms and notices before redistributing copied or derivative material.

This version has been substantially modified to focus on repository-wide documentation architecture, authoritative-source management, cross-reference integrity, documentation compression, project-sensitive maintenance, and explicit separation between documentation work and implementation.
