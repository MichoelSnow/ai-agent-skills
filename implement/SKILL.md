---
name: implement
description: Make authorized code or configuration changes with scope proportional to the task. Use when the user explicitly asks to create, modify, refactor, or implement software behavior. Inspect the relevant code first, follow established project patterns and constraints, make the smallest complete change that solves the requested problem, and stop when new material uncertainty or blockers appear. Do not use for discussion, planning, diagnosis, review, or clarification without explicit authorization to modify state.
---

# Implement

## Goal

Implement the requested change correctly with the least unnecessary disruption.

Prefer existing project decisions over generic best practices, complete solutions over brittle patches, and the minimum process necessary for the scope and risk of the task.

## 1. Confirm Authorization and Scope

Follow the repository's `AGENTS.md` authority model for universal authorization and scope boundaries. Implementation requires the current user request to independently authorize modification; a discussion, clarification, diagnosis, review, plan, or acknowledgement of a problem is not implementation authorization.

Before changing state, identify the requested outcome and the boundaries of the work.

If material ambiguity remains, clarify it before implementation.

## 2. Inspect Before Editing

Read the code, configuration, instructions, and nearby patterns needed to understand the change.

Prefer repository evidence over assumptions.

When relevant:

- inspect the target files,
- inspect directly related callers or consumers,
- check project-specific rules,
- find an existing analogous implementation,
- understand tests and interfaces affected by the change,
- check current working-tree state before operations that could disturb user work.

Do not perform exhaustive repository archaeology for a small, well-bounded change.

Investigate enough to make the change safely, then act.

## 3. Follow the Project, Not Generic Preference

Existing project decisions are authoritative unless the user explicitly asks to reconsider them.

Match established:

- architecture,
- naming,
- libraries,
- abstractions,
- data contracts,
- configuration patterns,
- error-handling conventions,
- testing conventions.

Do not replace an established project approach with a convention you consider more standard or elegant.

When project instructions conflict with generic implementation advice, follow the project instructions.

## 4. Scale Process to the Task

Use the lightest implementation process that reliably fits the change.

Choose the narrowest action that satisfies the immediate objective.

Before using a broader command, build, test suite, migration, data operation, or other potentially expensive action, consider whether the narrower alternative answers the current question or satisfies the current acceptance criterion.

Do not choose a broader action merely because it is more comprehensive.

Consider:

- execution time,
- compute or monetary cost,
- amount of affected state,
- feedback speed,
- risk,
- whether the additional work provides useful information at this stage.

If the difference is potentially material and it is unclear which scope the user intends, ask before proceeding.

### Small, Bounded Change

For obvious, low-risk changes:

- inspect the relevant context,
- make the change,
- run proportionate verification,
- stop.

Do not manufacture a design document, implementation plan, abstraction, or checkpoint for trivial work.

### Moderate Change

For changes spanning multiple related pieces:

- identify the small set of affected components,
- implement in coherent units,
- verify important boundaries as you go,
- reassess if repository reality differs materially from expectation.

### Large or High-Risk Change

For substantial features, migrations, architectural changes, or difficult-to-reverse work:

- work from an approved scope or plan when one exists,
- divide execution into bounded units,
- preserve acceptance criteria,
- use checkpoints where they reduce risk,
- stop before consequential deviations from the agreed approach.

A plan is an outcome contract, not a transcript. Adapt implementation mechanics to repository reality when necessary, but do not silently change scope, requirements, or acceptance criteria.

## 5. Make the Smallest Complete Change

Change only what is necessary to satisfy the requested outcome.

Prefer:

- existing utilities over new ones,
- existing patterns over new architecture,
- local changes over broad rewrites,
- clear direct code over speculative flexibility.

Do not:

- refactor unrelated working code,
- add unrequested features,
- perform "while I'm here" cleanup,
- add abstractions for hypothetical future needs,
- introduce dependencies without a concrete need,
- expand the task because adjacent work would also be useful.

Minimal does not mean brittle.

If a small abstraction or broader change is genuinely required to preserve a real invariant, eliminate meaningful duplication, or solve the actual class of problem rather than one example, use it. Be able to explain why the narrower patch would be incorrect or fragile.

### Backward Compatibility Is a Requirement, Not a Default

Do not preserve legacy behavior merely because it already exists.

Only add compatibility layers, deprecated aliases, fallback paths, migration shims, or parallel implementations when there is a concrete compatibility requirement.

For solo or early-stage projects with no external consumers, prefer replacing the old implementation cleanly and removing superseded code.

If it is unclear whether compatibility is required and preserving it would materially affect the implementation, ask before adding it.

Do not assume enterprise compatibility requirements apply to every project.

## 6. Protect Existing Work

Assume uncommitted user changes may be intentional.

Before operations that can overwrite, reset, regenerate, migrate, or broadly reformat files:

- inspect relevant working-tree state,
- avoid overwriting unrelated changes,
- preserve user work,
- disclose destructive or difficult-to-reverse actions before taking them.

Do not reset, revert, discard, or replace user changes merely because they complicate implementation.

## 7. Implement in Coherent Units

For non-trivial work, make changes in units small enough that their purpose and correctness remain understandable.

After a meaningful unit:

- inspect the result,
- run the narrow verification that provides useful feedback,
- confirm assumptions still hold before building further work on top.

Do not generate a large speculative implementation before checking whether its foundation is correct.

Do not force every small edit into an artificial multi-step workflow.

## 8. Stop on Material Surprises

Stop and reassess when:

- repository reality contradicts the assumed design,
- a required dependency or capability is missing,
- requirements conflict,
- the change would need to exceed the authorized scope,
- a destructive action becomes necessary but was not authorized,
- repeated verification failures indicate the implementation model may be wrong.

Resolve what can be established safely from the repository first.

If the remaining uncertainty could materially change the solution, ask rather than guess.

Do not stack speculative changes to push through a blocker.

## 9. Keep the Codebase Clean

When the requested change supersedes code within its authorized scope:

- remove dead code created by the change,
- remove failed or abandoned implementation attempts,
- update affected references,
- avoid leaving duplicate paths unless compatibility is explicitly required.

Do not preserve obsolete implementation history inside production code merely because it existed before the final solution.

Do not extend cleanup beyond the scope of the change.

## 10. Respect Interfaces and Data Contracts

Before changing schemas, parsers, APIs, configuration keys, persisted fields, or shared interfaces, inspect relevant consumers and validation points.

Account for places such as:

- callers and downstream consumers,
- schemas and specifications,
- validation logic,
- tests,
- migrations,
- serialized or persisted data,
- documented contracts.

Do not remove or rename a field based only on the file where it is defined.

## 11. Verify Before Claiming Completion

Implementation is not complete merely because code was written.

Run the narrowest verification that provides sufficient evidence for the current change, such as:

- focused tests,
- type or static checks,
- targeted builds,
- smoke tests,
- direct behavior checks,
- inspection of generated output.

Prefer narrow, informative checks first. Use broader validation when the scope or risk warrants it.

If verification cannot be performed, state that limitation.

Do not claim success without evidence.

## 12. Finish at the Requested Boundary

Once the requested outcome is implemented and proportionately verified, stop.

Do not automatically:

- begin the next roadmap item,
- implement follow-up ideas,
- productionize adjacent exploratory work,
- refactor neighboring systems,
- deploy or migrate environments,
- commit, merge, or push unless authorized.

If useful follow-up work is discovered, mention it briefly rather than performing it.

## Authorization Boundary

This skill permits code or configuration mutation only when the current user request explicitly authorizes implementation within the requested scope. Follow `AGENTS.md` for universal authorization, preservation, and stopping boundaries.

Consequential actions such as destructive migrations, deployment, overwriting user work, deleting data, committing, merging, or pushing require their own authorization when they are not clearly part of the user's request.

When scope or authorization is ambiguous, prefer not to mutate and clarify the decision-relevant uncertainty.

## Key Principle

Inspect first. Follow the project. Make the smallest complete change. Verify it. Stop at the authorized boundary.

## Attribution

This skill was adapted from concepts and workflow patterns in:

- implementation principles from `agents-inc/skills`: https://github.com/agents-inc/skills
- `executing-plans` from `obra/superpowers`: https://github.com/obra/superpowers/tree/main/skills/executing-plans
- `better-codex` from `noobnooc/agent`: https://github.com/noobnooc/agent/tree/main/skills/better-codex
- `executing-plans` from `eagleagentic/superpowers-gpt-5.6`: https://github.com/eagleagentic/superpowers-gpt-5.6/tree/main/skills/superpowers/executing-plans

The `agents-inc/skills` and `obra/superpowers` repositories are distributed under the MIT License. See all upstream repositories for their complete license texts and notices, and verify applicable license terms before redistributing material derived from sources whose licensing is not explicitly stated here.

This version has been substantially modified for proportional solo-development workflows, explicit mutation authorization, preservation of project-specific decisions, protection of existing user work, and support for tasks ranging from tiny edits to substantial features without imposing a mandatory planning framework.
