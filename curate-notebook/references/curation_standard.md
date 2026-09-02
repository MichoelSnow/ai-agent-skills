# Notebook Curation Standard

Use this reference when performing a full `curate-notebook` pass.

This document defines the desired end state. It is not a rigid notebook template. Apply each requirement only where it improves the notebook being curated.

## 1. Reader Standard

The curated notebook should be understandable to a knowledgeable reader who did not participate in the original analysis.

That reader should be able to determine:

- why the notebook exists,
- what questions it addresses,
- what data and external systems it depends on,
- how to run the relevant analyses,
- which work represents current conclusions,
- which work is retained as experimental history,
- why important alternatives were rejected or superseded,
- what the notebook produces,
- what conclusions were reached,
- what remains unresolved.

The reader should not need to reconstruct the author's interactive editing history.

Assume the reader is a data scientist who understands standard analytical methods but does not know this project's data model, terminology, provenance, or prior decisions. Focus explanations on project-specific context and analytical choices rather than introductory explanations of familiar concepts.

## 2. Notebook Header

Begin with a substantial markdown header appropriate to the notebook.

Include, when relevant:

### Title

Use a descriptive analytical title rather than a generic filename-derived heading.

### Purpose

Explain why the notebook exists and what problem it addresses.

### Scope

State what the notebook does and, when useful, what it intentionally does not cover.

### Questions

Identify the principal analytical questions, hypotheses, experiments, or decisions addressed.

### Data Sources

Document:

- datasets,
- tables,
- files,
- databases,
- APIs,
- external services,
- important date ranges or cohorts when material.

Do not expose secrets or credentials.

### Dependencies and Setup

Document prerequisites needed to use the notebook, such as:

- required packages,
- database availability,
- local services,
- environment variables,
- expected working directory,
- upstream generated files.

### How to Run

Explain the intended execution model.

Distinguish when necessary between:

- setup required for all work,
- current/final analyses,
- optional exploratory or historical experiments,
- expensive or externally dependent sections.

Do not imply that every retained historical experiment must be rerun to reproduce the current conclusions.

### Runtime and Cost

Call out sections known to be:

- slow,
- memory-intensive,
- data-intensive,
- API-dependent,
- costly,
- destructive or externally consequential.

### Outputs

Describe important artifacts produced by the notebook, such as:

- tables,
- files,
- figures,
- model artifacts,
- database writes,
- metrics,
- intermediate datasets.

### Findings

Summarize the major current findings when the notebook has reached conclusions.

### Caveats and Open Questions

Record important limitations, unresolved questions, and incomplete work.

### Status

Make the state of the notebook clear, for example:

- active exploration,
- analysis complete,
- partially validated,
- historical reference,
- awaiting additional data.

Do not force every header subsection into notebooks where it would add no value.

## 3. Section Structure

Organize the notebook into meaningful sections.

Use a consistent heading hierarchy:

- `#` notebook title,
- `##` major sections,
- `###` analytical subsections or experiments,
- deeper levels only when genuinely necessary.

Each major section should briefly explain:

- what it does,
- why it exists,
- what the reader should expect from it.

Avoid long stretches of code without narrative structure.

Documentation should be information-dense. Remove or merge explanations that repeat a heading, an adjacent comment, or an existing conclusion. A shorter notebook with precise context is preferable to one filled with mechanically generated prose.

## 4. Analytical Status

Make the status of meaningful analytical branches explicit.

Use concepts such as:

### Current

Work that contributes to the present analytical approach or conclusions.

### Exploratory

Work that investigates a question or candidate direction without necessarily becoming part of the final approach.

### Rejected

An experiment or hypothesis that was evaluated and intentionally abandoned.

Record why it was rejected.

### Superseded

An approach that was previously useful but replaced by a later method.

Record what replaced it and why when that information matters.

These labels do not require identical literal headings in every notebook. The distinction must be obvious to the reader.

## 5. Preserve Useful Experimental History

Do not confuse unsuccessful experiments with clutter.

Retain failed, rejected, or superseded work when it:

- provides evidence,
- explains an analytical decision,
- records a meaningful negative result,
- prevents future repetition of an unproductive approach,
- documents how an important conclusion was reached.

For retained historical experiments, capture:

1. the question,
2. the approach,
3. the result,
4. the interpretation,
5. the decision.

Remove experiments that are merely redundant, accidental, or provide no useful analytical record.

The objective is to organize the archaeology, not erase it.

## 6. Current Analysis

A reader interested only in the current conclusions should be able to identify the relevant analysis quickly.

Do not require that reader to execute or understand every historical experiment first.

When current analysis depends on outputs from earlier exploration, make that dependency explicit.

When useful, consolidate the final/current implementation separately from historical experiments rather than forcing the reader to infer which version is authoritative.

## 7. Code Cell Standard

Every substantive code cell should have a clear purpose.

Prefer markdown immediately before a code cell or logical group of cells to explain analytical intent.

Use inline comments for implementation details that are not obvious from the code itself.

A reader should generally be able to determine:

- why the code is being run,
- what inputs it relies on,
- what it produces,
- how the output is used.

Do not add comments that merely translate obvious code into English.

### Cell Size

Prefer cells that represent one coherent analytical operation.

Split cells that contain several conceptually distinct operations when separation improves comprehension.

Combine fragmented cells when several tiny cells collectively perform one obvious operation.

Do not optimize cell size toward an arbitrary line count.

## 8. Code Quality

Format code consistently.

When safe and appropriate:

- normalize indentation and whitespace,
- follow project formatting conventions,
- consolidate imports,
- remove genuinely unused imports,
- remove dead debugging code,
- eliminate exact duplicate code,
- improve clearly misleading names,
- simplify unnecessarily confusing expressions.

Do not change analytical semantics merely to satisfy style preferences.

Do not introduce abstractions unless they improve the notebook's actual readability or correctness.

When multiple experiment cells repeat a clear procedure with only feature, target, filter, or parameter changes, a small local helper function is encouraged. Keep one explicit, clearly labeled call cell per meaningful variation so the experimental comparison remains inspectable. Do not force unrelated branches into one helper or introduce a generalized framework that obscures the analytical design.

## 9. Cell Documentation

Document substantive code cells selectively. A short comment at the beginning of the code cell is appropriate when it makes the cell's purpose, inputs, outputs, or role in the analysis clearer. Nearby markdown is also appropriate for a logical group of cells.

Do not add identical boilerplate to every cell, explain trivial statements unnecessarily, or leave stale labels such as `Cell 3:` after reorganization. For repeated experiments, identify the specific variation at the top of each call cell.

## 10. Imports and Setup

Keep common setup easy to locate.

Prefer:

- imports near the beginning,
- configuration and important parameters in a clear setup section,
- explicit random seeds when reproducibility depends on them,
- clear environment or service prerequisites.

Avoid repeatedly importing the same packages throughout the notebook unless local placement has a meaningful reason.

Do not hide important analytical parameters inside distant cells.

## 11. Data Loading and Mutation

Make data provenance understandable.

For important data-loading cells, make clear:

- what is being loaded,
- from where,
- relevant filters or date ranges,
- whether the operation reads or writes,
- whether it can be expensive.

Clearly identify cells that:

- write files,
- modify databases,
- call external services,
- overwrite artifacts,
- mutate shared external state.

Curation does not authorize destructive execution.

## 12. Results and Interpretation

Important analytical output should be followed by interpretation when the implication is not self-evident.

For each section that produces analytical output, add or improve a concise markdown summary at the end of the section. It should state the observed result, what it means, and whether it changes the next step. Use existing outputs and conclusions by default; do not rerun expensive or externally dependent analysis merely to write the summary. Setup-only sections do not need result summaries.

Separate:

- observation,
- interpretation,
- decision.

Do not let important conclusions exist only implicitly in output tables or charts.

For experiments, record negative results and decisions when they affected the direction of the work.

## 13. Outputs

Keep outputs useful and bounded.

Remove or clear outputs that are:

- stale,
- redundant,
- excessively large,
- debugging remnants,
- inconsistent with current code.

Preserve outputs when they provide useful context and are known to correspond to the current code.

If correspondence cannot be established, label or clear them rather than presenting them as current evidence.

Avoid dumping large raw datasets when a representative sample or summary communicates the result.

## 14. Execution Order and Hidden State

Interactive notebooks often contain hidden state. Reduce it where practical.

Look for:

- variables used before their defining cell,
- execution counts that reveal out-of-order execution,
- objects mutated across distant cells,
- cells whose correctness depends on manually running another cell first,
- overwritten variables with materially different meanings,
- stale outputs from previous states.

Reorder or document dependencies when doing so does not alter analytical meaning.

Do not manufacture a single linear execution path when the notebook intentionally contains independent or historical experiments.

Instead, make execution requirements explicit for each relevant analytical path.

## 15. Reproducibility

Aim for the strongest practical reproducibility without turning the notebook into production software.

A reproducible notebook should make clear:

- prerequisites,
- inputs,
- important parameters,
- execution dependencies,
- expected outputs,
- known external requirements.

Full top-to-bottom execution is not mandatory for curation.

External databases, services, long-running computation, large datasets, or expensive operations may legitimately prevent it.

## 16. Verification Budget

Use approximately five minutes as the default **total execution budget for the curation session**, not per cell.

Static validation does not count against this conceptual runtime budget in the same way as expensive notebook execution.

Prioritize:

1. structural/static validation,
2. fast high-value execution,
3. representative or targeted checks,
4. full execution only when practical.

Do not start a cell likely to consume most of the execution budget unless it provides essential evidence.

If meaningful verification is expected to exceed the budget, ask the user before continuing.

Never launch operations expected to take tens of minutes or hours merely to prove that the notebook can run.

## 17. External Dependencies

Do not treat unavailable external dependencies as curation failures.

Examples include:

- Postgres,
- DuckDB services or external database files,
- cloud warehouses,
- APIs,
- remote storage,
- proprietary data,
- unavailable local infrastructure.

When execution is blocked:

- validate structure statically,
- inspect dependency flow,
- execute independent sections when useful,
- document what could not be verified and why.

Do not claim execution success where none occurred.

## 18. Backup Standard

Create a backup before modifying the source notebook.

The backup should:

- preserve the original notebook exactly,
- be clearly identifiable,
- remain untouched during curation,
- be available for comparison or restoration.

Do not delete the backup when curation finishes.

Delete it only after the user has reviewed the curated notebook, is satisfied with the result, and explicitly authorizes backup removal.

## 19. Final Editorial Pass

Before completion, read the notebook as a document rather than merely inspecting individual cells.

Check for:

- coherent section progression,
- unexplained jumps,
- duplicate explanations,
- contradictory markdown,
- historical experiments that look current,
- current analyses that look experimental,
- missing interpretations,
- stale outputs,
- inconsistent terminology,
- headings that no longer describe their contents,
- setup instructions that no longer match the notebook.

The final notebook should feel deliberately authored.

## 20. Completion Checklist

A curation pass is complete when, to the strongest practical extent:

- [ ] The original notebook has a retained backup.
- [ ] The notebook has an informative header.
- [ ] Purpose and scope are clear.
- [ ] Data sources and external dependencies are documented.
- [ ] Setup and execution instructions are clear.
- [ ] Major sections have explanatory narrative.
- [ ] Substantive code cells or logical cell groups have selective, specific purpose documentation.
- [ ] Repeated experiment groups use clear helper functions where that improves readability, with explicit variation call cells retained.
- [ ] Current analyses are easy to identify.
- [ ] Exploratory, rejected, and superseded work is clearly distinguished.
- [ ] Useful negative results and analytical decisions are preserved.
- [ ] Redundant and meaningless scratch work has been removed.
- [ ] Code formatting is consistent.
- [ ] Stale or misleading outputs have been addressed.
- [ ] Important results have interpretation.
- [ ] Every analytical-output section has a concise result summary, unless an existing conclusion already serves that purpose.
- [ ] Current conclusions are summarized.
- [ ] Open questions and caveats are visible.
- [ ] Execution dependencies are understandable.
- [ ] Verification stayed within the execution budget unless the user approved otherwise.
- [ ] The notebook states what was and was not actually executed or verified.
- [ ] The backup has not been deleted without explicit approval.

Do not satisfy this checklist mechanically. Its purpose is to ensure the notebook is genuinely easier to understand and use.
