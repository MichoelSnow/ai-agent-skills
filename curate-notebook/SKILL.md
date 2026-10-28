---
name: curate-notebook
description: Perform an editorial and structural refactor of an existing Jupyter notebook so it becomes a clear, maintainable, reader-facing analytical artifact. Use when a notebook is messy, out of order, repetitive, poorly documented, difficult to rerun, or hard to understand after exploratory work. Reorganize cells, remove redundant content, improve formatting, add explanatory narrative, distinguish current analysis from retained experimental history, and preserve analytical meaning. Do not change analytical conclusions, methods, or source data unless separately authorized.
---

# Curate Notebook

## Goal

Transform an existing exploratory notebook into a durable, understandable analytical artifact.

Preserve the analysis, not the notebook's accidental editing history.

`curate-notebook` owns deliberate editorial restructuring and cleanup. Analytical experimentation belongs to `explore-data`; generic verification procedure belongs to `verify`; productionization belongs to implementation work.

A future reader should be able to understand the notebook's purpose, data, current analytical path, important findings, useful experimental history, unresolved questions, and intended execution order without reconstructing the notebook from scratch.

## 1. Create a Backup Before Modification

Before making changes:

- create a clearly identifiable backup of the original notebook;
- do not overwrite that backup during curation;
- treat it as the recovery source for accidentally removed material.

Do not begin notebook modification until the backup exists.

Keep the backup until the curated notebook has been reviewed and the user explicitly approves deleting it.

Deleting the backup is a separate authorization event.

## 2. Inspect the Notebook as a Whole

Before editing, inspect the complete notebook and reconstruct its current state.

Determine, as relevant:

- purpose and analytical questions;
- data sources and setup;
- dependencies and external services;
- current analyses supporting conclusions;
- exploratory, rejected, or superseded branches;
- important outputs and findings;
- repeated or redundant work;
- unresolved questions;
- hidden-state or execution-order dependencies.
- structural complexity, including total code volume, number and size of code cells, helper functions or classes, and substantial custom infrastructure;

Use these indicators to identify where complexity has accumulated, not as hard limits or optimization targets.

Do not begin with mechanical cleanup before understanding what the notebook is trying to do.

If the meaning of a cell or branch is materially ambiguous, preserve it and flag the ambiguity rather than guessing.

## 3. Define the Target Notebook Standard

Reorganize the notebook around a clear analytical story appropriate to the work.

A curated notebook should make clear:

- what the notebook is for;
- what data and external dependencies it uses;
- what setup is required;
- which analysis represents the current conclusions;
- which exploratory, rejected, or superseded work is retained and why;
- what the important findings are;
- what remains unresolved;
- what should be run, and in what order, for the analysis a reader wants to reproduce.

Use a structure that fits the notebook rather than a mandatory template.

A common pattern is:

`question -> analysis/experiment -> result -> interpretation -> next decision`

Do not force genuinely branching analysis into an artificial linear narrative.

Always Keep section and subsection headings in their own Markdown cells.

Write for a competent data scientist who understands standard analytical concepts but does not know this project.

Header and explanatory content should be proportional to notebook complexity. Do not turn the notebook header into a project README.

Document cells or groups of cells when their purpose or analytical role would not otherwise be obvious.

Summarize important findings and decisions; do not mechanically add prose after every output-producing section.

## 4. Distinguish Current Analysis from Experimental History

Classify meaningful analytical branches as appropriate:

- **Current** — contributes to present conclusions or the current analytical approach;
- **Exploratory** — investigates an alternative or open question;
- **Rejected** — tested and intentionally abandoned;
- **Superseded** — replaced by a later approach.

Make these distinctions obvious through structure and Markdown.

For retained historical experiments, preserve enough context to explain:

- what question was tested;
- what approach was tried;
- what was observed;
- why the approach was rejected, superseded, or not pursued.

Do not assume the full implementation must remain.

When an experiment no longer contributes to the current executable analysis, prefer a concise Markdown summary unless its code is necessary to reproduce an important finding, understand a consequential methodological decision, or support ongoing work.

The backup preserves the complete pre-curation notebook. The curated notebook should prioritize the current analytical narrative and the evidence necessary to support it.

## 5. Reorder Cells When Needed

Move cells into a logical analytical structure when the current order mainly reflects interactive editing history.

Preserve chronology only when it materially helps explain an analytical decision.

Before moving cells, account for:

- variable dependencies;
- object mutation;
- files read or written;
- data loading;
- random state;
- model state;
- downstream assumptions.

Ensure variables are defined before use and preserve a valid execution order.

Do not preserve confusing order merely because that is how the notebook evolved.

## 6. Remove Redundant and Obsolete Content

Remove or consolidate content that provides neither current analytical value nor useful historical context, including:

- exact duplicates;
- repeated setup;
- abandoned approaches with no useful evidence or decision history;
- obsolete versions of later code;
- temporary debugging;
- unused intermediate calculations;
- stale inspection cells;
- obsolete plots or redundant outputs;
- repeated source loads or database queries when shared inputs can be loaded once and reused;
- explanatory text that merely repeats nearby headings or obvious code.

Preserve exploratory, rejected, or superseded work when it documents useful evidence, explains an important change in direction, or prevents future repetition of an unproductive approach.

When retaining historical work, label its status and summarize the outcome.

Remove redundant experimentation, not useful analytical history.

If removal could alter analytical meaning or erase valuable evidence, keep or summarize the material explicitly.

## 7. Simplify and Format Code Without Changing the Analysis

Improve code quality without changing analytical semantics.

When appropriate:

- normalize formatting;
- remove unused or duplicate imports;
- clean obvious dead code;
- improve clear variable names;
- split overly dense cells;
- combine unnecessarily fragmented cells;
- prefer established library functionality over equivalent custom implementations;
- remove unused functions, obsolete options, and unnecessary abstraction;
- preserve helpers that genuinely simplify repeated or complex logic.

Review substantive cells for responsibility as well as length. A cell should normally have one coherent analytical purpose and one primary result. Flag cells that exceed roughly 75 physical lines or 50 executable lines, contain three or more analytical phases, combine multiple expensive operations, or mix substantial computation with presentation.

When a cell is flagged, split it by analytical phase—such as data preparation, transformation, model calculation, or result presentation—while preserving execution order and analytical semantics. These thresholds are review triggers, not rigid requirements.

Do not hide notebook complexity by moving large amounts of code into external modules solely to shorten the notebook.

Do not refactor analytical logic merely for stylistic preference.

If a simplification could change results, treat it as a separate analytical or implementation change and do not make it without explicit authorization.

Use the project's established formatter/linter conventions when useful.

## 8. Document Code Cells Selectively

Every substantive code cell should make its purpose clear to a future reader. Trivial cells may omit a separate explanation when their purpose is obvious from the surrounding section and code.

For substantive cells, prefer a short, cell-specific comment at the beginning of the code cell or concise markdown immediately before it. The explanation should identify the operation, its meaningful inputs, and its output or analytical role.

Use inline comments inside code for non-obvious implementation details.

Do not mechanically prepend the same `Purpose:` label or generic prose to every cell. Do not add comments that merely translate obvious code into English, and do not retain stale labels such as `Cell 2:` after cells have been moved or removed.

The reader should be able to answer:

- why this cell exists,
- what it consumes,
- what it produces,
- how it contributes to the current analysis.

For experimental sections, document the outcome as well as the purpose. When an approach was rejected or superseded, explain why. For repeated experiments, state at the top of each variation what differs from the other cells in the group.

For sections representing the current analysis, make that status clear enough that a reader seeking only the final analytical path can identify them quickly.

## 9. Document Every Major Section

Each major section should begin with concise markdown explaining:

- what question or task the section addresses,
- why it is being performed,
- what result or decision the reader should expect.

After important analytical sections, add concise interpretation describing:

- the key result,
- what it means,
- whether it changes the next step.

Do not leave major blocks of analysis separated only by code.

At the end of every section that produces an analytical output, add a concise markdown result summary in the most natural location. Base it on the notebook's existing outputs and conclusions unless execution has been explicitly authorized and is practical. State the observation, interpretation, and resulting decision or next step. Include exploratory and model-comparison sections; omit setup-only sections that produce no analytical result. Avoid adding a summary when an existing, sufficiently specific conclusion already serves that purpose—improve or relocate the existing text instead.

Documentation should explain necessary analytical complexity, not compensate for unnecessary complexity. When a section requires extensive explanation because it contains redundant experiments, obsolete machinery, or avoidable abstraction, simplify the underlying notebook first rather than documenting the complexity in place.


## 10. Reconcile Markdown, Code, and Outputs

After restructuring:

- update Markdown that describes old behavior;
- remove or revise stale conclusions;
- ensure headings match the actual analysis;
- remove references to deleted cells;
- make sure retained findings correspond to the current code;
- clear or regenerate stale outputs only when appropriate and authorized.

Do not preserve an output merely because it exists.

## 11. Preserve Analytical Meaning

Curation must not silently change:

- formulas;
- filters;
- cohorts;
- statistical methods;
- feature definitions;
- model choices;
- evaluation metrics;
- data-source semantics;
- domain assumptions;
- analytical conclusions.

If a substantive analytical error is discovered, report it separately.

Do not fix analytical logic unless the user separately authorizes analysis or implementation changes.

## 12. Improve Reproducibility Without Productionizing

Make the curated notebook as reproducible as practical.

When useful:

- centralize imports and setup;
- expose important parameters;
- preserve random seeds;
- make data-loading assumptions explicit;
- reduce accidental dependence on prior interactive execution;
- keep the intended run order clear.

Do not introduce orchestration frameworks, package architecture, deployment systems, or other production abstractions merely to improve notebook organization.

Productionization is a separate task.

## 13. Verify Proportionally

Perform structural/static validation first.

Check, as relevant:

- notebook structure and cell ordering;
- variable dependencies;
- obvious undefined references;
- setup placement;
- stale-output indicators;
- hidden execution-state assumptions.

Execute notebook code only when execution is separately authorized and materially increases confidence.

Prefer targeted execution over a full top-to-bottom run when it is sufficient.

Use the `verify` skill for broader verification procedure or when deciding what evidence is sufficient.

Do not launch long-running, expensive, destructive, or externally consequential operations solely for notebook curation without explicit authorization.

At completion, report what was structurally validated, what was executed, what was not executed, and any remaining reproducibility risks.

For notebooks with substantive code cells, verify that oversized or multi-phase cells were either split by responsibility or intentionally retained with a clear justification. Use lightweight AST or Radon metrics as supporting evidence, not as a substitute for reviewing the notebook's sequential readability.

## 14. Completion Standard

Curation is complete when a future reader can determine, without code archaeology:

- the notebook's purpose;
- the data and required setup;
- the current analytical path;
- the status of important experimental branches;
- the important findings and decisions;
- what remains unresolved;
- the intended execution path;
- what was and was not verified.

The final notebook should feel deliberately authored rather than merely cleaned.

## Authorization Boundary

Curation authorizes structural, formatting, explanatory, and organizational edits to the notebook only when the user's request explicitly asks for modification.

It does not authorize:

- changing analytical logic;
- fixing newly discovered analytical defects;
- expanding the analysis;
- productionizing notebook code;
- destructive changes to source data;
- modifying application code;
- deleting the original backup.

When a discovered issue crosses from curation into analysis, debugging, verification, or implementation, report it and stop at that boundary.

## Key Principle

Preserve the analysis while removing accidental complexity. Make the current analytical path easy to follow and retain only the experimental history that still carries useful evidence or decision context.

## Supporting Files

Use supporting resources when present:

- `references/curation_standard.md` for the detailed target quality standard;
- `scripts/notebook_tools.py` for deterministic notebook inspection and structural edits.

Do not read or use supporting files unnecessarily. Use them when they materially improve reliability or reduce direct manipulation of notebook JSON.

## Attribution

This skill was adapted from concepts and workflow patterns in:

- `jupyter-notebook-assistant` from `Dexploarer/claudius-skills`: https://github.com/Dexploarer/claudius-skills
- `jupyter-notebook` from OpenAI's `openai/skills`: https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook
- `jupyter-notebooks` from OpenAI's `role-specific-plugins`: https://github.com/openai/role-specific-plugins/tree/main/plugins/data-analytics/skills/jupyter-notebooks
- `notebook-for-experiment` from JetBrains `intellij-community`: https://github.com/JetBrains/intellij-community/tree/master/.agents/skills/notebook-for-experiment
- `lab-notes` from `eins78/agent-skills`: https://github.com/eins78/agent-skills/tree/main/skills/lab-notes
- notebook editing patterns from `narang99/jupyter-notebook-editor-skill`: https://github.com/narang99/jupyter-notebook-editor-skill
- Jupyter notebook style guidance from STScI: https://github.com/spacetelescope/style-guides/blob/master/guides/jupyter-notebooks.md

See each upstream source for its complete license terms and notices before redistributing copied or derivative material.

This version has been substantially modified to support aggressive notebook editorial restructuring, preservation of analytical meaning, selective retention of experimental history, and proportional verification without turning curation into analysis or production engineering.
