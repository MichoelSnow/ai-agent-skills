---
name: explore-data
description: Explore data and run iterative analytical or ML experiments. Use when the user wants to understand a dataset, investigate patterns or data quality, answer analytical questions, test hypotheses, engineer or evaluate candidate features, compare models, or work iteratively in notebooks, SQL, Python, or similar analytical environments. Do not assume exploration should progress to modeling, productionization, or a polished deliverable unless requested.
---

# Explore Data

## Goal

Learn from data efficiently without prematurely turning exploratory work into a production pipeline, polished notebook, or rigid research process.

Work incrementally: understand enough context to choose a useful next step, run that step, inspect the result, and let the evidence determine what comes next.

Keep active analytical work understandable as it evolves, but do not perform a full editorial notebook refactor unless explicitly requested. Use `curate-notebook` when an existing notebook needs deliberate restructuring or cleanup.

## 1. Establish the Analytical Objective

Before doing substantial work, identify what the user is currently trying to learn or decide.

Use available context first. Clarify only material uncertainty.

Do not require a complete analysis plan when the purpose of the work is exploratory and later steps depend on what the data reveals.

Do not silently expand the objective. Exploring a dataset does not authorize model building; comparing models does not authorize productionizing one.

## 2. Understand the Data Before Interpreting It

Establish enough structure to reason correctly about the data.

When relevant, determine:

- the grain: what one row represents;
- identifiers and likely keys;
- dimensions or categorical variables;
- metrics or quantitative variables;
- temporal fields;
- target or outcome variables;
- important joins or relationships;
- dataset size and relevant time coverage.

Check data quality where it could affect the current analysis, including missingness, duplicates, suspicious values, inconsistent types, unexpected ranges, or leakage.

Treat quality flags as things to investigate, not automatic errors to clean.

Do not profile every column exhaustively when only a narrow subset matters to the question.

## 3. Scale the Work to the Question and Data

Use the smallest amount of data and computation that can answer the immediate question reliably.

Prefer:

- targeted columns;
- relevant cohorts or time windows;
- samples for early exploration of very large datasets;
- focused summaries over large raw outputs;
- small experiments before expensive searches or model training.

Escalate to full-data computation only when the result requires it.

Do not run broad queries, exhaustive profiling, large parameter searches, or expensive model training merely because they are available.

For potentially expensive operations:

- begin with a small representative check that verifies correctness and feasibility;
- estimate runtime or memory when that materially affects the approach;
- prefer vectorized, batched, or database-native operations over repeated per-row or per-user processing;
- provide progress reporting for meaningfully long-running operations;
- reconsider the approach when runtime or implementation complexity becomes disproportionate to the analytical question.

## 4. Work in Small Analytical Steps

Prefer one coherent analytical step at a time.

For notebooks:

- keep each substantive cell focused on one coherent analytical purpose and one primary intermediate result or output;
- separate setup and helper definitions, data loading, transformations, model calculations, and presentation when they are distinct analytical phases;
- keep outputs bounded and readable;
- inspect the output before deciding the next analytical step;
- default to a single top-to-bottom execution path for the active notebook;
- keep section and subsection headings in their own Markdown cells so notebook collapsing remains useful.
- If a later section needs additional data, update the earlier loading cell rather than adding a later reload. Keep expensive source extraction, transformation, modeling, and presentation in separate cells.

A cell whose purpose requires multiple major “and” clauses should normally be split before continuing. Prefer splitting by analytical phase rather than by arbitrary line count.

For SQL or scripts, use the same principle: produce an interpretable intermediate result before layering on additional transformations.

Do not generate a large sequence of speculative cells or analyses before seeing whether early assumptions hold.

Do not pre-create notebook sections, placeholder cells, utilities, or infrastructure for analyses that are merely possible future directions. Add them only when they become part of the current analytical work.

Optimize for the simplest readable implementation that answers the analytical question correctly.

- Prefer established libraries before writing substantial custom utilities or algorithms.
- Prefer less code when two approaches are equally correct and understandable.
- Keep straightforward transformations, model calls, and calculations visible.
- Extract helpers only when they eliminate meaningful duplication or clarify genuinely complex logic.
- Avoid speculative abstractions, configuration systems, custom classes, or generalized infrastructure.
- Do not compress code into clever expressions merely to reduce line count.

### Progress for long-running cells

Any notebook cell expected to run longer than 30 seconds must provide progress feedback.

Use a progress bar, staged status messages, or periodic elapsed-time updates. 
The feedback should identify the current stage and, when practical, report completion or elapsed time for meaningful substeps.

The objective is the simplest readable implementation, not the fewest possible characters.

## 5. Maintain the Active Analytical Thread

Exploratory work should remain understandable while it is happening.

Use lightweight Markdown or equivalent notes around important steps to capture:

- the current question;
- why the next analysis is being run;
- the key result;
- the interpretation;
- the next decision or question.

Prefer the compact pattern:

`question -> experiment -> result -> conclusion/next step`

Do not narrate trivial cells.

When an earlier result changes materially:

- reconcile downstream analyses that depend on it;
- update conclusions based on the old result;
- clearly mark materially superseded work;
- remove obvious temporary clutter that no longer contributes to the active analysis.

Do not perform a full editorial cleanup, aggressive historical pruning, or notebook-wide restructuring during ordinary exploration unless the user explicitly asks for curation.

If notebook complexity is becoming disproportionate to the analytical question, stop adding code and simplify the active path before continuing.

## 6. Monitor Analytical Complexity

As exploratory work grows, periodically reassess whether the notebook's complexity is still proportional to the analytical question.

Use simple structural indicators as warning signals, including:

- total code lines,
- number of code cells,
- number of helper functions or classes,
- unusually large individual cells,
- repeated abstractions or utilities,
- growing amounts of configuration or control flow.

Use these practical thresholds as warning signals, not hard limits:

- more than 75 physical lines or 50 executable lines;
- three or more distinct analytical phases;
- more than one distinct expensive operation, such as a database query, large join, model fit, or file export;
- more than two major intermediate DataFrames;
- substantial calculation and presentation logic in the same cell.

If a cell triggers at least two of these conditions, review it for splitting before adding more code. Split by analytical responsibility when the cell combines data preparation, model calculation, prediction generation, or presentation.

A lightweight notebook complexity report may use `nbformat` and Python AST inspection to report per-cell line counts, top-level statements, AST nodes, queries, displays, file operations, and major assignments. Use Radon for Halstead and cyclomatic metrics when useful. Treat all metrics as warning signals; sequential readability and analytical responsibility take precedence.

These are diagnostic signals, not hard limits.

When complexity grows materially, do not respond by automatically refactoring the same amount of machinery into cleaner abstractions. First determine whether the added code, experiments, helpers, or infrastructure are still necessary to answer the current question.

Prefer reducing unnecessary analytical surface area before improving its architecture.

If implementing a method requires a substantial amount of custom infrastructure, control flow, state management, checkpointing, or reusable machinery, stop and reassess whether that implementation is necessary for the analytical question and whether an established implementation can answer it more simply. Do not allow implementation effort to become the primary work of an exploratory notebook.

Use established code-quality tools such as Ruff or Radon when they help identify specific sources of complexity. Do not introduce custom complexity metrics or additional tooling solely to measure the notebook.

Do not reduce measured complexity by moving large amounts of code into external modules solely to shorten the notebook, creating generalized frameworks around exploratory work, or compressing readable code into dense expressions.

If the notebook is becoming difficult for a competent data scientist to understand by reading it sequentially, treat that as a stronger warning than any individual metric.

Before adding another substantial analytical section, model family, utility layer, or diagnostic branch to an already complex notebook, reassess whether it is necessary and whether existing work can first be removed, consolidated, or summarized.

## 7. Choose Freeform or Hypothesis-Driven Exploration

Use the lightest mode appropriate to the work.

### Freeform Exploration

Use when becoming familiar with unfamiliar data, looking for patterns, trying candidate transformations or features, exploring possible relationships, or when the useful next question depends on the current result.

A formal hypothesis is optional.

Allow the analysis to evolve organically, but keep track of what was observed and what motivated the next step.

### Hypothesis-Driven Experimentation

Use when evaluating a specific claim, method, feature, model, or analytical choice.

Make explicit, when material:

- the hypothesis or question;
- the comparison or baseline;
- the metric or evidence that matters;
- important controls or constraints;
- what result would change the conclusion.

Do not retrofit hypotheses after seeing results as though they were specified beforehand.

Move from freeform to hypothesis-driven work when exploration produces a concrete claim worth testing.

## 8. Follow Evidence, Not a Prescribed Pipeline

After each meaningful result:

1. inspect what actually happened;
2. check whether the result is plausible;
3. update the working interpretation;
4. choose the next highest-value step.

Do not automatically march through `load -> clean -> EDA -> feature engineering -> model -> tune -> report`.

Skip stages that do not serve the current question.

If a result is surprising or consequential, perform a focused reasonableness check before building further conclusions on it.

## 9. ML Experimentation

When the task reaches modeling:

- establish a meaningful baseline before adding complexity;
- use evaluation metrics that match the actual objective;
- guard against target leakage and inappropriate train/test contamination;
- preserve comparable evaluation conditions across candidate models;
- change a small number of important factors at a time when practical;
- inspect relevant segments or failure cases when aggregate metrics may hide important behavior.

Before introducing another model family, substantial diagnostic experiment, or new layer of modeling infrastructure, reassess whether it is necessary to answer the original analytical question.

Consider:

- What specific uncertainty will this experiment resolve?
- What result would change the current decision?
- Is there a simpler experiment that could answer the same question?
- Is the likely value of the information worth the additional complexity?

Do not expand a straightforward analysis into an open-ended model-development project through successive additions.

When proposed work materially changes the scope or complexity of the analysis, explain that change and obtain user approval before proceeding.

Do not assume a more complex model is preferable because it performs slightly better.

Do not launch broad hyperparameter searches or production-grade experiment infrastructure unless the stage and objective justify them.

For important model comparisons, record enough context to understand what changed: candidate, meaningful configuration difference, evaluation setup, result, and interpretation.

## 10. Preserve Reproducibility Without Overengineering

Exploratory work should be rerunnable enough to support its conclusions, but it does not need production architecture.

When results become important:

- make key assumptions explicit;
- preserve important parameters and random seeds;
- keep transformations traceable;
- record the evaluation setup;
- make consequential calculations reproducible.

If an expensive database extract or intermediate result materially improves rerun time when cached, use the project's established cache location and format. Otherwise choose the simplest appropriate local format. Do not create caching infrastructure for cheap transformations.

Treat saved intermediate files as explicit analysis artifacts with documented paths and purposes, not as hidden notebook cache state.

Prefer a clean top-to-bottom path for the active analysis.

Reproducibility means preserving the data sources, transformations, parameters, random seeds, and execution sequence necessary to reproduce the analytical conclusions.

It does not require generalized experiment runners, large configuration systems, checkpointing frameworks, custom data-loading infrastructure, or other production-style abstractions.

If exploratory code later needs to become production code, treat productionization as a separate task.

## 11. Separate Observation, Interpretation, and Decision

Distinguish:

- **Observation:** what the data or experiment shows;
- **Interpretation:** what may explain the observation;
- **Decision:** what should be done because of it.

Do not present exploratory correlations as causal findings.

Do not present a plausible interpretation as an observed fact.

Do not claim an experiment supports a conclusion beyond what its design and evidence justify.

## 12. Completion and Handoff

Stop when the user's current analytical question has been answered sufficiently or when the next useful step requires a new decision from the user.

Before leaving a substantial analytical session, make the active work recoverable:

- record the current objective if it changed;
- mark materially superseded paths;
- record key conclusions;
- identify unresolved questions;
- make the next logical step clear.

Do not turn this into a full notebook-curation pass unless requested.

Summarize, when appropriate, what was learned, important caveats, unresolved questions, and the most useful next analytical step.

Do not automatically execute the suggested next step unless the current request authorizes it.

## Authorization Boundary

Exploration may involve running analytical code, notebook cells, queries, or experiments when the user's request authorizes that work.

It does not authorize changing production systems, modifying source application behavior, destructive data operations, productionizing exploratory code, or expanding into adjacent analyses or model families that were not requested.

When the boundary between exploration and implementation is unclear, stop before crossing it.

## Key Principle

Use the smallest useful experiment to learn the next important thing. Keep the active analytical thread visible without turning exploration into notebook curation or production engineering.

## Attribution

This skill was adapted from concepts and workflow patterns in:

- `jupyter-notebook` from OpenAI's `openai/skills`: https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook
- `explore-data` from Anthropic's `anthropics/knowledge-work-plugins`: https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/explore-data
- `lab-notes` from `eins78/agent-skills`: https://github.com/eins78/agent-skills/tree/main/skills/lab-notes

The OpenAI `jupyter-notebook` skill and Anthropic `knowledge-work-plugins` repository are distributed under the Apache License 2.0. `eins78/agent-skills` is distributed under the MIT License. See the upstream repositories for the complete license texts and notices.

This version has been substantially modified to combine lightweight exploratory data analysis and ML experimentation, scale process to the analytical question, support notebooks/SQL/scripts without requiring them, maintain analytical continuity during active work, and avoid automatically escalating exploratory work into notebook curation, modeling infrastructure, or production engineering.
