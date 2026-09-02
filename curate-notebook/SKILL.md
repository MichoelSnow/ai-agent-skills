---
name: curate-notebook
description: Perform a full editorial and structural refactor of an existing Jupyter notebook so it becomes a clear, maintainable, reader-facing analytical artifact. Use when a notebook is messy, out of order, repetitive, poorly documented, difficult to rerun, or hard to understand after exploratory work. Reorganize cells, remove redundant content, improve formatting, add explanatory narrative, distinguish current analysis from retained experimental history, and preserve analytical meaning. Do not change analytical conclusions, methods, or source data unless separately authorized.
---

# Curate Notebook

## Goal

Transform an exploratory notebook into a durable, understandable analytical artifact.

The goal is not to preserve the notebook's original structure. The goal is to preserve the analysis while making the notebook substantially easier to understand, navigate, and rerun.

A knowledgeable future reader should be able to open the notebook and quickly determine:

- what the notebook is for,
- what data and dependencies it uses,
- how to run it,
- which analyses represent the current conclusions,
- which analyses are retained as exploratory or historical work,
- what each major section does,
- what the important findings are,
- what was superseded or rejected and why,
- what remains unresolved.

## 1. Create a Backup Before Modification

Before making any changes:

- create a backup copy of the original notebook,
- use a clearly identifiable backup name,
- do not overwrite that backup during the curation process,
- treat the backup as the reference version for recovering accidentally removed material.

Do not begin notebook modification until the backup exists.

Keep the backup until:

- the curated notebook has been reviewed,
- the user is satisfied with the result,
- and the user explicitly approves deleting the backup.

Deleting the backup is a separate authorization event.

## 2. Inspect the Notebook as a Whole

Before editing, inspect the complete notebook and reconstruct its current state.

Determine:

- the notebook's purpose,
- major analytical questions,
- data sources and setup,
- dependencies and external services,
- important experiments,
- current analyses supporting the final conclusions,
- exploratory experiments and alternative approaches,
- rejected or superseded branches and why they were abandoned,
- repeated or redundant work,
- important outputs and findings,
- unresolved questions,
- hidden-state or execution-order dependencies.

Do not begin with mechanical cleanup before understanding what the notebook is trying to do.

If the meaning of a cell or branch is materially ambiguous, preserve it and flag the ambiguity rather than guessing.

## 3. Design the Target Narrative

Reorganize the notebook around a clear analytical story.

Use a structure appropriate to the notebook, typically including:

1. notebook header,
2. setup and dependencies,
3. data sources and loading,
4. data preparation,
5. major analytical sections,
6. exploratory experiments and alternative approaches where relevant,
7. current/final analyses,
8. results and interpretation,
9. conclusions,
10. unresolved questions or next steps.

Do not force exploratory work into a single linear story when the analytical process legitimately branched.

Preserve useful experimental history, but clearly distinguish it from the analyses that support the current conclusions.

This is a default structure, not a mandatory template. Omit sections that do not serve the notebook.

Prefer the narrative pattern:

`question -> analysis/experiment -> result -> interpretation -> next decision`

Do not preserve exploratory chronology when it makes the final notebook harder to understand.

Write for an outside data scientist who understands the analytical concepts but does not know the project. Explain project-specific data sources, variables, decisions, and results; do not spend space re-explaining standard statistical or machine-learning concepts.

## 4. Add a Comprehensive Notebook Header

At the top of the notebook, create or improve a substantial markdown header that explains:

- notebook title,
- purpose,
- scope,
- primary analytical questions,
- data sources,
- required external services or databases,
- important dependencies,
- setup assumptions,
- how to run the notebook,
- expected execution order,
- important runtime or cost considerations,
- outputs or artifacts produced,
- major findings,
- known caveats,
- unresolved questions,
- current status of the analysis.

The header should help a future user understand the notebook before reading the code.

Do not turn the header into a full project document. Keep it specific to the notebook.

## 5. Distinguish Current Analysis from Experimental History

Identify which analyses represent the current state of the work and which are retained as part of the analytical history.

Classify meaningful analytical branches as appropriate:

- **Current** — contributes to the present conclusions or final analytical approach.
- **Exploratory** — investigates a question or alternative without necessarily producing the final approach.
- **Rejected** — tested and intentionally abandoned because the evidence did not support it.
- **Superseded** — once useful but replaced by a later approach.

Make these distinctions obvious through notebook structure and markdown.

For retained historical experiments, record enough context to explain:

- what question was being tested,
- what approach was tried,
- what was observed,
- why the approach was rejected, superseded, or not pursued further.

Do not erase useful failed experiments merely because they are not part of the final solution. Negative results and abandoned approaches can be important analytical evidence.

At the same time, a reader interested only in the current conclusions should be able to identify and follow the current analysis without reconstructing the entire exploratory history.

The goal is not one execution path. The goal is a notebook whose analytical status is explicit.

## 6. Reorder Cells Aggressively When Needed

Move cells into a logical analytical structure when the current ordering primarily reflects accidental interactive editing.

Preserve meaningful experimental progression when chronology helps explain how an analytical decision was reached. Reorganization should clarify the analysis, not rewrite its history into an artificially linear process.

Before moving cells, account for:

- variable dependencies,
- object mutation,
- files written or read,
- data loaded,
- random state,
- model state,
- downstream assumptions.

Prefer explicit dependencies over hidden state.

Do not preserve confusing order merely because that is how the notebook evolved.

## 7. Remove Redundant and Obsolete Cells

Remove or consolidate cells that provide neither current analytical value nor useful historical context, including:

- exact duplicates,
- repeated setup,
- abandoned approaches that provide no useful evidence or decision history,
- old versions of later code that do not explain an important analytical decision,
- temporary debugging,
- unused intermediate calculations,
- obsolete plots,
- stale inspection cells,
- redundant outputs.

Preserve exploratory, rejected, or superseded experiments when they document useful evidence, explain why an analytical direction changed, prevent future repetition of an unproductive approach, or otherwise contribute to the analytical record.

When retaining them, clearly label their status and summarize the outcome.

Remove redundant experimentation, not useful analytical history.

If removing a cell could alter the analytical meaning or erase valuable evidence, keep it or summarize it explicitly.

Apply the same test to documentation. Remove explanatory cells that merely repeat a nearby heading, cell comment, or result. Prefer one precise explanation in the most useful location over several generic reminders.

## 8. Format and Lint Code Cells

Improve code quality inside the notebook without changing analytical semantics.

When appropriate:

- normalize formatting,
- fix indentation,
- remove unused imports,
- consolidate duplicate imports,
- clean obvious dead code,
- improve variable naming where the meaning is clear,
- break overly dense cells into logical units,
- combine tiny fragmented cells when doing so improves readability.

For exploratory or historical cells, the surrounding documentation should also make their status clear. A future reader should not have to infer whether a cell represents the current approach or an abandoned experiment.

Use the project's established formatter/linter conventions when available.

Do not refactor analytical logic merely for stylistic preference.

When a group contains several cells that repeat the same analytical procedure with different feature sets, targets, filters, or parameter values, consider extracting the shared procedure into a small, local helper function. Use this only when the shared logic is genuinely clear and the helper makes the analysis easier to follow. Keep separate, clearly labeled call cells for each meaningful model or parameter variation so the comparison remains visible. Do not hide the experimental design inside an opaque generalized framework, and do not make this refactor when it risks changing semantics or cannot be statically checked with reasonable confidence.

## 9. Document Code Cells Selectively

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

## 10. Document Every Major Section

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

## 11. Reconcile Markdown, Code, and Outputs

After restructuring:

- update markdown that describes old behavior,
- remove stale conclusions,
- ensure section headings match the actual analysis,
- clear or regenerate stale outputs when appropriate,
- remove references to deleted cells,
- make sure findings correspond to the current canonical code.

Do not preserve output simply because it exists.

## 12. Preserve Analytical Meaning

Curation must not silently change:

- formulas,
- filters,
- cohorts,
- statistical methods,
- feature definitions,
- model choices,
- evaluation metrics,
- data-source semantics,
- domain assumptions,
- analytical conclusions.

If a substantive analytical error is discovered, flag it separately.

Do not fix analytical logic unless the user separately authorizes analysis or implementation changes.

## 13. Improve Reproducibility Without Productionizing

Make the canonical notebook as reproducible as practical.

When useful:

- centralize imports and setup,
- expose important parameters,
- preserve random seeds,
- make data-loading assumptions explicit,
- avoid accidental dependency on prior interactive execution,
- keep the intended run order clear.

Do not introduce orchestration frameworks, package architecture, deployment systems, or production abstractions merely to improve notebook organization.

Productionization is a separate task.

## 14. Use a Bounded Verification Strategy

Do not assume every cell should be executed during curation.

Use a total default execution budget of approximately 5 minutes for the curation session.

Before running cells, consider whether they may be:

- long-running,
- data-intensive,
- externally dependent,
- costly,
- destructive,
- dependent on unavailable services.

Use this verification order:

### Static Validation

Always perform the strongest practical static review first:

- notebook structure,
- cell ordering,
- variable dependencies,
- obvious undefined references,
- setup placement,
- stale-output indicators,
- hidden execution-state assumptions.

### Targeted Execution

Run fast, high-value cells or representative sections when doing so materially increases confidence.

Use the total execution budget deliberately.

Do not spend most of the budget on a single cell unless it is essential to validation.

### Full Execution

Run the notebook top-to-bottom only when:

- required dependencies and services are available,
- expected runtime is reasonable,
- execution fits the available budget or the user has approved a longer run,
- there are no destructive or externally consequential steps.

If meaningful execution would exceed the default budget, stop and ask before continuing.

Never launch operations expected to take tens of minutes or hours solely for notebook curation without explicit approval.

## 15. Report What Was and Was Not Verified

At completion, distinguish:

- what was structurally validated,
- what was actually executed,
- what was not executed,
- why execution was skipped,
- any remaining reproducibility risks.

A valid outcome may be:

- static validation only,
- static plus targeted execution,
- full top-to-bottom execution.

Do not claim the notebook was fully executed or reproducible when it was not.

## 16. Completion Standard

Before considering curation complete, confirm that a future reader can determine:

- **Purpose:** Why does this notebook exist?
- **Data:** What sources and services does it depend on?
- **Setup:** What must be available before running it?
- **Execution:** What must be run, and in what order, for the analyses the reader wants to reproduce?
- **Current analysis:** Which analyses support the present conclusions?
- **Experimental history:** Which sections are exploratory, rejected, or superseded?
- **Decisions:** Why were important alternative approaches abandoned or replaced?
- **Sections:** What does each major section do?
- **Cells:** What does each substantive code cell contribute?
- **Findings:** What did the analysis show?
- **Status:** Is the status of each important analytical branch clear?
- **Outputs:** What does the notebook produce?
- **Open questions:** What remains unresolved?
- **Verification:** What parts of the notebook were actually validated?
- **Backup:** Has the original notebook backup been retained pending user approval?

The final notebook should feel deliberately authored, not merely cleaned.

## Authorization Boundary

Curation authorizes structural, formatting, explanatory, and organizational edits to the notebook only when the user's request explicitly asks for modification.

It does not authorize:

- changing analytical logic,
- fixing newly discovered analytical defects,
- expanding the analysis,
- productionizing notebook code,
- destructive changes to source data,
- modifying application code,
- deleting the original backup.

When a discovered issue crosses from curation into analysis, debugging, or implementation, report it and stop at that boundary.

## Key Principle

Preserve the analysis and organize the archaeology. Turn the notebook into a clear, reader-facing analytical record where current conclusions are easy to follow and useful exploratory history remains understandable.

## Supporting Files

Use supporting resources when present:

- `references/curation_standard.md` for the detailed target quality standard,
- `scripts/notebook_tools.py` for deterministic notebook inspection and structural edits.

Do not read or use supporting files unnecessarily. Use them when they materially improve reliability or reduce direct manipulation of raw notebook JSON.

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

This version has been substantially modified to support aggressive notebook editorial restructuring, deterministic backup and structural handling, explicit cell/section documentation, comprehensive notebook headers, proportional verification with a bounded execution budget, and preservation of analytical meaning without requiring full execution or productionization.
