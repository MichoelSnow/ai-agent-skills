---
name: debug
description: Evidence-first debugging for bugs, failures, regressions, unexpected behavior, and performance problems. Use when something is broken, failing, slow, inconsistent, or behaves differently from expectation. Investigate before proposing fixes; do not use for open-ended design exploration or when the user only wants a conceptual explanation.
---

# Debug

## Goal

Find the cause of a problem with the smallest useful investigation, then fix only after the evidence supports a cause.

ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

Avoid speculative fixes, generic troubleshooting dumps, and broad investigation that is disproportionate to the problem.

## Workflow

### 1. Establish the actual symptom

Start from what is observed, not what you assume is happening.

Identify:

- what the user expected,
- what actually happened,
- the smallest known path that reproduces or exposes the problem,
- any relevant environment, command, input, or state.

Do not substitute a nearby problem for the reported one.

If a fact materially affects the diagnosis and is not known, verify it or ask.

### 2. Use the narrowest useful evidence source

Prefer the least invasive check that can distinguish between plausible causes.

Examples include:

- reading the directly relevant code or configuration,
- inspecting the exact error or output,
- checking the command that actually ran,
- comparing current behavior with a known-good case,
- checking recent changes,
- running or proposing a narrowly scoped reproduction.

Do not begin with broad filesystem searches, environment dumps, full test suites, large downstream builds, or other expensive/invasive checks unless narrower evidence is insufficient.

Scale the investigation to the stage and stakes of the work.

### 3. Build a feedback loop when practical

For non-trivial bugs, create or identify a repeatable signal that distinguishes broken from working behavior.

Prefer, in order of practicality:

- an existing failing test,
- a focused new regression test,
- a small reproduction,
- a targeted command or query,
- a stable observable output.

The loop should be as fast and deterministic as practical.

Do not force a formal reproduction when the issue is already directly observable and the extra ceremony would not improve the diagnosis.

### 4. Form a small set of evidence-based hypotheses

After gathering enough evidence, identify the most plausible causes.

Keep the hypothesis set small and falsifiable.

For each hypothesis, ask:

- What evidence supports it?
- What observation would disprove it?
- What is the cheapest check that distinguishes it from the alternatives?

Do not present guesses as findings.

### 5. Test one hypothesis at a time

Choose the highest-value discriminating check.

Change one variable at a time where practical.

If the result contradicts the hypothesis:

- update the model,
- do not defend the original theory,
- choose the next best discriminating check.

If documentation, runtime output, or user-provided domain knowledge contradicts your interpretation, treat that evidence as authoritative until reconciled.

### 6. Stop thrashing

Do not stack speculative fixes.

If multiple attempts fail or the evidence remains contradictory:

- stop,
- summarize what has been ruled out,
- identify what information is still missing,
- ask the user or escalate the investigation method.

Repeated failed fixes are evidence that the current model is wrong, not a reason to keep changing code.

### 7. Separate diagnosis from repair

A supported diagnosis does not itself authorize a code change.

If the user asked only to diagnose, explain the likely root cause and stop.

If the user explicitly authorized a fix, make the smallest change that addresses the supported cause.

Do not broaden the fix into adjacent cleanup, refactoring, or future-proofing unless requested.

### 8. Verify the fix

When a fix is made:

- rerun the narrow feedback loop,
- check the original symptom,
- add or update regression coverage when appropriate,
- verify that the fix did not violate stated constraints.

Use broader validation only when justified by the scope and maturity of the change.

Do not claim the problem is fixed without evidence.

## Debugging Data and Analysis Work

For notebooks, SQL, data pipelines, or ML analysis, the same workflow applies, but the feedback loop may be:

- a row-count or schema check,
- a known record,
- a small sample,
- a summary statistic,
- a before/after comparison,
- a controlled notebook cell,
- a metric or prediction slice.

Do not force application-style test infrastructure onto exploratory analysis when a smaller deterministic check is sufficient.

## Authorization Boundary

While diagnosing:

- read-only investigation is allowed when needed,
- do not modify files or state unless the user's request explicitly authorizes repair,
- do not treat identifying the bug as permission to fix it,
- do not run destructive or high-cost commands without explicit authorization.

When authorization is unclear, stop at diagnosis.

## Key Principle

Evidence before theory. Root cause before repair. Narrow checks before broad ones. Stop when the current model stops explaining the evidence.

## Attribution

This skill was adapted from concepts and workflow patterns in:

- `diagnosing-bugs` from `mattpocock/skills`: https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs
- `systematic-debugging` from `obra/superpowers`: https://github.com/obra/superpowers/tree/main/skills/systematic-debugging

Both upstream repositories are distributed under the MIT License. See the upstream repositories for their complete license texts and notices.

This version has been substantially modified for proportional debugging in solo engineering, data science, analysis, notebook, SQL, and pipeline workflows, with explicit authorization boundaries and narrow-first investigation rules.
