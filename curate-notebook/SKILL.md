---
name: curate-notebook
description: Reorganize and clean an existing Jupyter notebook so its analytical narrative, canonical execution path, findings, and conclusions are understandable and reproducible. Use when a notebook has become messy, out of order, repetitive, stale, difficult to rerun, or hard to understand after exploratory work. Do not use to change analytical conclusions, redesign the analysis, or productionize notebook code unless explicitly requested.
---

# Curate Notebook

## Goal

Turn an exploratory notebook into a durable analytical artifact without changing what the analysis means.

A curated notebook should let a future reader understand:

- what problem the notebook addresses,
- what data it uses,
- how the analysis progressed,
- which path is canonical,
- what was learned,
- what was rejected or superseded,
- what remains unresolved,
- which cells should be run and in what order.

Preserve analytical intent. Improve organization, continuity, and reproducibility.

## 1. Read Before Editing

Inspect the notebook as a whole before restructuring it.

Infer:

- the notebook's objective,
- major analytical questions,
- data sources and setup,
- important experiments or branches,
- current/canonical analyses,
- superseded or abandoned approaches,
- key findings and conclusions,
- unresolved questions.

Do not begin by mechanically deleting or reordering cells.

When meaning is ambiguous and the choice could alter the analysis, ask the user rather than guessing.

## 2. Backup Before Modification

Before making any changes to the notebook:

- create a backup copy of the original notebook,
- use a clearly identifiable backup name,
- do not overwrite the original backup during the curation process,
- treat the backup as the reference version for comparing analytical content and restoring anything removed accidentally.

Do not begin notebook modification until the backup exists.

Keep the backup until:

- the curated notebook has been reviewed,
- the user is satisfied with the outcome,
- and the user explicitly approves removing the backup.

Do not delete the backup automatically at the end of the curation workflow.

## 3. Reconstruct the Analytical Narrative

Identify the logical story the notebook should tell.

Prefer a structure such as:

1. purpose and scope,
2. setup and data,
3. data understanding or preparation needed for the analysis,
4. analytical questions or experiments,
5. results and interpretation,
6. conclusions,
7. unresolved questions or next steps.

This is a default narrative, not a mandatory pipeline. Omit sections that do not serve the notebook.

For substantial analytical blocks, preserve the lightweight pattern:

`question -> experiment -> result -> conclusion/next step`

Do not force every trivial cell into this structure.

## 4. Identify the Canonical Path

Distinguish cells that belong to the current analysis from cells that are:

- scratch work,
- duplicated,
- obsolete,
- superseded,
- exploratory dead ends,
- debugging artifacts,
- temporary inspection,
- old versions of later code.

The canonical path should be obvious.

When an old experiment explains an important analytical decision, preserve it only if that history adds value. Otherwise remove it or summarize the relevant conclusion in markdown.

Do not keep multiple unexplained versions of the same analysis.

## 5. Reorder Safely

Reorder cells when necessary to create a coherent top-to-bottom execution path.

Before moving a cell, account for:

- variables it depends on,
- state created by earlier cells,
- mutations to shared objects,
- files or queries it produces,
- randomness,
- later cells that depend on its outputs.

Do not reorder solely for visual neatness if doing so changes semantics.

Prefer explicit setup over hidden dependence on execution history.

## 6. Add Lightweight Narrative

Use concise markdown cells to explain what a future reader cannot reliably infer from code alone.

Add or improve, when useful:

- notebook purpose and scope,
- section headings,
- why an important experiment is being run,
- interpretation of consequential results,
- why one approach replaced another,
- final findings,
- caveats,
- unresolved questions,
- next logical step.

Do not narrate obvious mechanics or turn the notebook into a report unless requested.

## 7. Remove Noise

Remove or consolidate material that obscures the canonical analysis, including:

- empty cells,
- exact duplicates,
- abandoned scratch cells with no enduring value,
- debug prints or temporary inspections,
- stale commentary contradicted by later work,
- repeated imports or setup,
- redundant outputs.

Be conservative when deletion could remove analytical evidence or intent.

If uncertain whether a cell is obsolete, preserve it and flag the ambiguity rather than silently deleting it.

## 8. Reconcile Code, Markdown, and Outputs

After restructuring:

- make markdown match the current code,
- make conclusions match the current results,
- remove references to deleted or superseded steps,
- identify stale outputs created by older code,
- ensure section headings match the actual analysis.

Do not preserve output merely because it exists.

If code changed materially, stale output should be cleared or regenerated when execution is authorized and practical.

## 9. Improve Reproducibility Without Productionizing

Prefer a clean canonical execution path from top to bottom.

Where material:

- centralize imports and basic setup,
- make important parameters visible,
- preserve random seeds,
- avoid hidden state,
- make data-loading assumptions understandable,
- avoid relying on variables created only by an accidental earlier execution order.

Do not introduce frameworks, orchestration, package structure, configuration systems, or production abstractions merely to clean the notebook.

Reusable helpers may be extracted within the notebook when they materially improve readability. Moving logic into application modules is a separate task unless explicitly requested.

## 10. Preserve Analytical Meaning

Curation must not silently change:

- formulas,
- filters,
- cohorts,
- statistical methods,
- model choices,
- feature definitions,
- evaluation metrics,
- business/domain assumptions,
- analytical conclusions.

If a substantive analytical problem is discovered, flag it separately.

Do not "fix" analytical logic as part of notebook curation unless the user explicitly authorizes that work.

## 11. Verify the Curated Notebook

When execution is available and authorized, prefer restarting the kernel and running the canonical notebook top-to-bottom.

Check that:

- cells execute in intended order,
- required state is created explicitly,
- outputs correspond to current code,
- major results remain consistent with the original analysis,
- the notebook reaches its stated conclusions without relying on hidden execution history.

If full execution is expensive, unsafe, or unavailable, perform the strongest proportionate validation possible and state what was not verified.

Do not claim the notebook is reproducible unless that was actually checked.

## 12. Completion Check

Before considering curation complete, confirm that a future reader can quickly determine:

- **Purpose:** Why does this notebook exist?
- **Data:** What is being analyzed?
- **Flow:** What is the canonical execution path?
- **Reasoning:** Why were important analytical steps taken?
- **Findings:** What did the analysis show?
- **Status:** Which paths are current versus superseded?
- **Open questions:** What remains unresolved?
- **Execution:** Can the intended cells be run in a coherent order?
- **Backup:** Has the original notebook backup been retained pending user approval?

If any of these remain unclear, improve only the missing part rather than adding documentation everywhere.

## Authorization Boundary

Curation authorizes structural and explanatory notebook edits only when the user's request explicitly asks for notebook modification.

It does not authorize:

- changing analytical logic,
- fixing newly discovered analytical defects,
- productionizing the notebook,
- modifying source application code,
- destructive changes to source data,
- expanding the analysis into new questions or models.

Deleting the backup requires explicit user approval and is not implied by approval of the curated notebook itself.

When a discovered issue crosses from curation into analysis or implementation, report it and stop at that boundary.

## Key Principle

Preserve the analysis, remove the archaeology. The final notebook should expose one understandable analytical story and one clear canonical path.

## Attribution

This skill was adapted from concepts and workflow patterns in:

- `jupyter-notebook-assistant` from `Dexploarer/claudius-skills`: https://github.com/Dexploarer/claudius-skills
- `jupyter-notebook` from OpenAI's `openai/skills`: https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook
- `notebook-for-experiment` from JetBrains `intellij-community`: https://github.com/JetBrains/intellij-community/tree/master/.agents/skills/notebook-for-experiment
- `lab-notes` from `eins78/agent-skills`: https://github.com/eins78/agent-skills/tree/main/skills/lab-notes

The OpenAI skill is distributed under the license terms of the upstream `openai/skills` repository. JetBrains IntelliJ Community source is governed by Apache 2.0 licensing terms for applicable open-source code. `eins78/agent-skills` is distributed under the MIT License. See each upstream repository for complete license texts and notices.

No license assertion is made here for `Dexploarer/claudius-skills`; verify and preserve its upstream license terms before distributing copied or derivative material beyond conceptual adaptation.

This version has been substantially modified to focus on reconstructing analytical narrative, distinguishing canonical from superseded notebook state, preserving analytical meaning, and supporting lightweight reproducibility without forcing production architecture.
