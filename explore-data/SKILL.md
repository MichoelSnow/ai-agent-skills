---
name: explore-data
description: Explore data and run iterative analytical or ML experiments. Use when the user wants to understand a dataset, investigate patterns or data quality, answer analytical questions, test hypotheses, engineer or evaluate candidate features, compare models, or work iteratively in notebooks, SQL, Python, or similar analytical environments. Do not assume exploration should progress to modeling, productionization, or a polished deliverable unless requested.
---

# Explore Data

## Goal

Learn from data efficiently without prematurely turning exploratory work into a production pipeline or rigid research process.

Work incrementally: understand enough context to choose a useful next step, run that step, inspect the result, and let the evidence determine what comes next.

Keep exploratory work understandable enough that a future reader can recover the analytical thread without reconstructing the notebook from scratch.

## 1. Establish the Analytical Objective

Before doing substantial work, identify what the user is currently trying to learn or decide.

Use available context first. Clarify only material uncertainty.

Do not require a complete analysis plan when the purpose of the work is exploratory and later steps depend on what the data reveals.

Do not silently expand the objective. Exploring a dataset does not authorize model building; comparing models does not authorize productionizing one.

## 2. Understand the Data Before Interpreting It

Establish enough structure to reason correctly about the data.

When relevant, determine:

- the grain: what one row represents,
- identifiers and likely keys,
- dimensions or categorical variables,
- metrics or quantitative variables,
- temporal fields,
- target/outcome variables,
- important joins or relationships,
- dataset size and relevant time coverage.

Check data quality where it could affect the current analysis, including missingness, duplicates, suspicious values, inconsistent types, unexpected ranges, or leakage.

Treat quality flags as things to investigate, not automatic errors to clean.

Do not profile every column exhaustively when only a narrow subset matters to the question.

## 3. Scale the Work to the Question and Data

Use the smallest amount of data and computation that can answer the immediate question reliably.

Prefer targeted columns, relevant cohorts/time windows, samples for early exploration of very large datasets, focused summaries over large raw outputs, and small experiments before expensive searches.

Escalate to full-data computation only when the result requires it.

Do not run broad queries, exhaustive profiling, large parameter searches, or expensive model training merely because they are available.

## 4. Work in Small Analytical Steps

Prefer one coherent analytical step at a time.

For notebooks:

- keep cells focused on one purpose,
- keep outputs bounded and readable,
- inspect the output before deciding the next analytical step,
- preserve a sensible top-to-bottom execution path where practical,
- put each section or subsection heading in its own Markdown cell; place explanatory prose in the Markdown cell or cells immediately below it so collapsing the section hides the explanation as well.

For SQL or scripts, use the same principle: produce an interpretable intermediate result before layering on additional transformations.

Do not generate a large sequence of speculative cells or analyses before seeing whether the early assumptions hold.

## 5. Maintain Analytical Continuity

Exploratory notebooks should remain understandable during the work, not only after cleanup.

Use markdown cells or equivalent lightweight notes to capture the analytical thread around important steps:

- current question or objective,
- why the next analysis is being run,
- key result,
- interpretation,
- next decision or question.

Prefer the compact pattern:

`question -> experiment -> result -> conclusion/next step`

Do not narrate every trivial cell. Document only what a future reader would need to understand why the analysis moved in a particular direction.

When an earlier cell changes materially:

- reconcile downstream cells,
- update conclusions that depended on the old result,
- remove or clearly mark obsolete paths,
- avoid leaving contradictory versions of the same analysis without explanation.

Clearly distinguish current analysis from scratch exploration.

When an experiment is superseded, either remove it or label it as superseded. Do not leave multiple unexplained alternatives that make the canonical path ambiguous.

## 6. Keep the Notebook Recoverable

A notebook should make it possible for a future reader to answer:

- What problem was this notebook trying to solve?
- What data does it use?
- Which analytical path is the current/canonical one?
- What were the important findings?
- Which experiments were rejected or superseded?
- What conclusions were reached?
- What remains unresolved?
- Which cells should be run, and in what order?

When practical, maintain:

- a short opening markdown section with purpose and scope,
- clear section headings,
- a coherent execution path,
- concise conclusion notes after major analysis blocks,
- a short final summary of findings and unresolved questions.

Do not create a separate documentation artifact merely to explain a single notebook unless the analysis spans multiple notebooks or the user asks for one.

For multi-notebook or multi-session analytical work, a separate project-level analysis log may be appropriate.

## 7. Choose Freeform or Hypothesis-Driven Exploration

Use the lightest mode appropriate to the work.

### Freeform Exploration

Use when becoming familiar with unfamiliar data, looking for patterns, trying candidate transformations or features, exploring possible relationships, or when the useful next question depends on the current result.

A formal hypothesis is optional.

Allow the analysis to evolve organically, but keep track of what was observed and what motivated the next step.

### Hypothesis-Driven Experimentation

Use when evaluating a specific claim, method, feature, model, or analytical choice.

Make explicit, when material:

- the hypothesis or question,
- the comparison or baseline,
- the metric or evidence that matters,
- important controls or constraints,
- what result would change the conclusion.

Do not retrofit hypotheses after seeing results as though they were specified beforehand.

Move from freeform to hypothesis-driven work when the exploration produces a concrete claim worth testing.

## 8. Follow Evidence, Not a Prescribed Pipeline

After each meaningful result:

1. inspect what actually happened,
2. check whether the result is plausible,
3. update the working interpretation,
4. choose the next highest-value step.

Do not automatically march through `load -> clean -> EDA -> feature engineering -> model -> tune -> report`.

Skip stages that do not serve the current question.

If a result is surprising or consequential, perform a focused reasonableness check before building further conclusions on it.

## 9. ML Experimentation

When the task reaches modeling:

- establish a meaningful baseline before adding complexity,
- use evaluation metrics that match the actual objective,
- guard against target leakage and inappropriate train/test contamination,
- preserve comparable evaluation conditions across candidate models,
- change a small number of important factors at a time when practical,
- inspect relevant segments or failure cases when aggregate metrics may hide important behavior.

Do not assume a more complex model is preferable because it performs slightly better.

Do not launch broad hyperparameter searches or production-grade experiment infrastructure unless the stage and objective justify them.

Record enough information to understand what changed between meaningful experiments.

For important model comparisons, record the candidate, key configuration differences, evaluation setup, result, and interpretation so the notebook does not become a sequence of unexplained model runs.

## 10. Preserve Reproducibility Without Overengineering

Exploratory work should be rerunnable enough to support its conclusions, but it does not need production architecture.

When a database extract or intermediate computation is expensive enough that caching materially improves rerun time, save the result in the project's established cache location and load it by default on later runs. Use an explicit refresh control to rebuild the cache. Do not cache every dataframe: quick transformations should remain in memory, and caches should be reserved for database extracts, expensive computations, or substantial final analysis outputs. Follow the project's established serialization format first; when no project convention exists, pickle is a reasonable default for local pandas notebook data, but use a more portable or durable format when interoperability, archival stability, or security requires it. Never load pickle files from untrusted sources.

When results become important:

- make key assumptions explicit,
- preserve important parameters and random seeds,
- keep transformations traceable,
- record the evaluation setup,
- make consequential calculations reproducible.

Prefer a clean top-to-bottom path for the canonical analysis.

Do not introduce orchestration systems, reusable frameworks, extensive abstractions, or production pipelines merely to tidy exploratory work.

If exploratory code later needs to become production code, treat productionization as a separate task.

## 11. Separate Observation, Interpretation, and Decision

Distinguish:

- **Observation:** what the data or experiment shows,
- **Interpretation:** what may explain the observation,
- **Decision:** what should be done because of it.

Do not present exploratory correlations as causal findings.

Do not present a plausible interpretation as an observed fact.

Do not claim an experiment supports a conclusion beyond what its design and evidence justify.

## 12. Completion and Handoff

Stop when the user's current analytical question has been answered sufficiently or when the next useful step requires a new decision from the user.

Before leaving a substantial notebook session, make the notebook recoverable:

- update the current objective if it changed,
- mark obsolete or superseded paths,
- record the key conclusions reached,
- identify unresolved questions,
- make the next logical step clear.

Summarize, when appropriate, what was learned, important caveats, unresolved questions, and the most useful next analytical step.

Do not automatically execute the suggested next step unless the current request authorizes it.

## Authorization Boundary

Exploration may involve running analytical code, notebook cells, queries, or experiments when the user's request authorizes that work.

It does not authorize changing production systems, modifying source application behavior, destructive data operations, productionizing exploratory code, or expanding into adjacent analyses or model families that were not requested.

When the boundary between exploration and implementation is unclear, stop before crossing it.

## Key Principle

Use the smallest useful experiment to learn the next important thing. Keep the analytical thread visible as you go so the notebook remains understandable after the exploration is over.

## Attribution

This skill was adapted from concepts and workflow patterns in:

- `jupyter-notebook` from OpenAI's `openai/skills`: https://github.com/openai/skills/tree/main/skills/.curated/jupyter-notebook
- `explore-data` from Anthropic's `anthropics/knowledge-work-plugins`: https://github.com/anthropics/knowledge-work-plugins/tree/main/data/skills/explore-data
- `lab-notes` from `eins78/agent-skills`: https://github.com/eins78/agent-skills/tree/main/skills/lab-notes

The OpenAI `jupyter-notebook` skill and Anthropic `knowledge-work-plugins` repository are distributed under the Apache License 2.0. `eins78/agent-skills` is distributed under the MIT License. See the upstream repositories for the complete license texts and notices.

This version has been substantially modified to combine lightweight exploratory data analysis and ML experimentation, scale process to the analytical question, support notebooks/SQL/scripts without requiring them, maintain lightweight lab-note-style analytical continuity, and avoid automatically escalating exploratory work into modeling or production engineering.
