---
name: plan
description: Create a concrete, sequential implementation plan that can be followed exactly by a human or AI agent. Use when the user asks to plan, design an implementation sequence, break work into phases, or prepare work for later execution. Planning is read-only and does not authorize implementation.
---

# Plan

## Goal

Create an implementation plan that another competent human or AI agent can execute from top to bottom without reconstructing the planning conversation.

The plan should remove material ambiguity before implementation begins, order work by dependency, separate tasks from constraints and decisions, define completion conditions for each phase, and make deviation obvious.

Once the user approves the plan, it becomes the authoritative execution contract for the work it covers.

Planning itself is read-only. Creating, revising, or approving a plan does not authorize implementation or command execution.

## 1. Inspect Before Planning

Inspect enough of the relevant repository and project context to understand the requested work before drafting a detailed plan.

Use, as applicable:

- the current user request;
- `AGENTS.md`;
- relevant `docs/project_context.md` content;
- applicable scoped requirements;
- relevant source files;
- tests and contracts;
- current documentation;
- existing architecture and tooling;
- accepted decisions from the current conversation.

Prefer repository evidence over assumptions.

Do not turn planning into an exhaustive repository audit unless the task genuinely requires one.

Inspect only enough context to produce a reliable plan.

## 2. Clarify Material Uncertainty

Resolve uncertainty before finalizing the plan when different answers would materially change:

- scope;
- architecture;
- data contracts;
- implementation order;
- dependencies;
- security;
- cost;
- migration behavior;
- release strategy;
- user-visible behavior.

Ask only decision-relevant questions.

Prefer 1–3 questions per round.

Do not ask the user to repeat information already established in the repository or conversation.

If multiple reasonable interpretations would materially change the plan, ask rather than choosing silently.

For low-impact, reversible decisions that fit established project defaults, choose the simplest reasonable interpretation and state the assumption.

## 3. Define the Plan Inputs

Before writing implementation phases, identify the information that governs the plan.

When relevant, distinguish:

### Goal

The concrete outcome the work must achieve.

### Fixed decisions

Decisions already made by the user or established by authoritative project requirements.

These are not checklist items.

### Constraints and guardrails

Rules that remain true throughout execution.

Examples:

- preserve existing scoring behavior;
- do not add a new framework;
- do not expose internal fields publicly;
- preserve unrelated user work;
- do not retain compatibility wrappers unless required.

These are not checklist items.

### Assumptions

Facts the plan currently depends on but has not fully verified.

Resolve material assumptions before approval when practical.

### Prerequisites

Conditions that must be established before dependent work begins.

Prerequisites must appear before the work that depends on them.

### Non-goals

Related work explicitly outside the plan.

These are not checklist items.

Do not mix these categories into one undifferentiated checklist.

## 4. Build the Plan in Dependency Order

Plans are sequential by default.

Order phases and steps according to actual dependency.

A common sequence is:

1. resolve decisions and prerequisites;
2. define or update contracts;
3. implement foundational behavior;
4. implement dependent behavior;
5. migrate callers or consumers;
6. remove superseded behavior;
7. verify;
8. release or deploy when applicable.

Do not use this sequence mechanically. Use the order required by the actual work.

A user should be able to read the plan from top to bottom without discovering later that an earlier step depended on something never mentioned.

Do not place a prerequisite, decision, migration, or verification dependency after the work that requires it.

If work truly cannot be represented as one linear sequence:

- explain why;
- identify the independent branches;
- state what may happen in parallel;
- identify the synchronization point;
- state exactly how the executor should proceed.

Prefer a simple sequential path unless parallel work is genuinely necessary.

## 5. Make Each Task Unambiguous

Each task should be small enough that a competent human or another AI agent can execute it without reinterpreting the intended work.

A good task should make clear, when relevant:

- what changes;
- where it changes;
- what behavior should result;
- what existing behavior must remain unchanged;
- what evidence establishes completion.

Name concrete files, modules, functions, routes, schemas, tests, or interfaces when repository inspection has established them.

Do not invent filenames, abstractions, helper layers, or APIs merely to make the plan appear specific.

If the exact implementation location is intentionally left open, state the responsibility and the criteria for choosing the location.

Avoid vague tasks such as:

- "handle edge cases";
- "add validation";
- "refactor as needed";
- "improve error handling";
- "clean up the API";
- "add tests."

State the actual edge cases, validation rules, errors, behavior, or tests required.

## 6. Use Checkboxes Only for Actions

A checkbox represents a concrete action that can be completed and verified.

Good checklist items:

- [ ] Add duplicate-user-key validation in the established request-validation module.
- [ ] Update the frontend caller to use the new response contract.
- [ ] Remove the old route after all callers are migrated.
- [ ] Run the targeted contract tests and record the result.

Do not use checkboxes for:

- principles;
- constraints;
- definitions;
- standing guardrails;
- architectural philosophy;
- non-goals;
- descriptive facts;
- decisions already made.

Bad checklist items:

- [ ] Keep the design simple.
- [ ] Do not introduce a new framework.
- [ ] Prefer explicit code.
- [ ] Security matters.

Those belong in prose.

## 7. Group Work Into Coherent Phases

Use phases when the work is large enough to benefit from checkpoints.

A phase should represent one coherent stage of progress.

Each phase should contain:

### Purpose

What this phase establishes.

### Tasks

Ordered concrete actions.

### Completion conditions

Observable conditions that must be true before the phase is complete.

Do not use phases merely to make a plan look structured.

For small tasks, a short ordered sequence may be enough.

## 8. Define Completion Conditions for Every Phase

Every phase must have explicit completion conditions.

Completion conditions should describe observable outcomes, not intentions.

Examples:

- invalid input is rejected before database or external-source work begins;
- all current callers use the new contract;
- no old route registration remains;
- public serialization excludes protected fields;
- the targeted test suite passes;
- the relevant documentation matches the implemented contract.

A phase is not complete merely because code was written.

The executor must not proceed to the next phase while required completion conditions remain unsatisfied.

When a completion condition requires command execution and execution has not been authorized, the condition remains unverified.

Do not mark it complete based solely on static inspection unless static inspection can genuinely establish the condition.

## 9. Put Verification Next to the Work It Validates

Verification should follow the implementation work it validates.

Do not collect all verification at the bottom when earlier phases depend on knowing whether preceding work succeeded.

Use the narrowest meaningful verification first.

A phase may include:

- static inspection;
- targeted tests;
- contract checks;
- database checks;
- lint or type checks;
- build checks;
- manual behavior checks;
- broader suites when justified.

Keep verification proportional to project scale, risk, and cost.

Do not require large test suites, builds, deployments, or expensive workflows merely for completeness.

Planning verification steps does not authorize executing them.

## 10. Avoid Duplication

Do not repeat the same rule or task in multiple sections.

If a rule applies throughout the plan, state it once as a constraint.

If a verification action belongs to a phase, place it in that phase rather than repeating it in:

- a global checklist;
- a later review checklist;
- final completion criteria;
- release steps.

Use a concise cross-reference when necessary.

Duplicated checklist items create ambiguity about which copy is authoritative and whether both must be performed.

## 11. Keep Plans Separate From Permanent Project Policy

A plan should use authoritative project requirements rather than becoming a second source of truth.

Reference applicable requirements when possible.

Repeat only the details necessary to make the implementation task unambiguous.

Do not permanently redefine:

- data contracts;
- architecture rules;
- security requirements;
- product behavior;
- operational policy

inside a temporary implementation plan.

If planning reveals a missing or incorrect project requirement, identify that separately.

Do not silently redefine the requirement inside the plan.

## 12. Self-Review Before Presenting the Plan

Before presenting the plan, review it as though a different agent will execute it with no access to the planning conversation beyond the approved plan and repository.

Check that:

- the requested outcome is fully covered;
- applicable requirements have corresponding work;
- all material decisions are resolved or explicitly surfaced;
- prerequisites appear before dependent work;
- phases are in execution order;
- no later section reveals an earlier prerequisite;
- every checkbox is a real action;
- every action is sufficiently specific;
- every phase has explicit completion conditions;
- verification follows the work it verifies;
- permanent constraints are not disguised as tasks;
- the plan does not duplicate work;
- filenames and symbols are based on evidence rather than invention;
- non-goals are clear;
- release or deployment steps do not appear before implementation is actually ready;
- nothing outside the requested scope was added merely because it might be useful.

If the plan fails this review, revise it before presenting it.

## 13. Approval Boundary

A plan is not implementation authorization.

When the user asks only for a plan:

- inspect;
- clarify;
- produce the plan;
- stop.

Do not begin implementation because the plan is complete.

Once the user approves a plan, the plan becomes the authoritative execution contract for the work it covers.

Approval of the plan does not override other authorization boundaries in `AGENTS.md`.

In particular, approval of a plan does not itself authorize:

- file modification unless the current request authorizes implementation;
- command execution;
- tests;
- builds;
- package-manager commands;
- database operations;
- migrations;
- Git commits;
- pushes;
- merges;
- deployments.

## 14. Approved Plan Fidelity

When an approved plan exists, follow it exactly enough that execution remains faithful to the agreed sequence and scope.

Proceed from top to bottom.

Do not independently:

- reorder phases or tasks;
- skip incomplete tasks;
- add material work;
- substitute a different implementation approach;
- broaden scope;
- reinterpret an agreed decision;
- weaken completion conditions;
- mark unverified work complete;
- continue around a contradiction between the plan and repository reality.

Checkboxes should reflect actual progress.

Mark a task complete only when the described action is complete.

Mark a phase complete only when its completion conditions are satisfied.

Do not treat the high-level outcome as permission to ignore unfinished plan items.

## 15. Amendment Protocol

An approved plan may become wrong, incomplete, or blocked as implementation reveals new facts.

Do not improvise around the plan.

Stop at the affected point and propose an amendment.

The proposed amendment should state:

1. what was discovered;
2. why the existing plan cannot be followed as written;
3. the smallest change needed;
4. which current or downstream steps are affected;
5. whether scope, requirements, risk, cost, or verification changes.

Do not edit the approved plan yet.

Wait for explicit user approval.

After approval:

- update the plan;
- make the amendment visible;
- preserve completed work that remains valid;
- resume from the earliest affected step.

If the user rejects the amendment, do not proceed with the conflicting implementation.

## 16. Updating Progress During Execution

Keep the plan useful as an execution record.

Allowed updates that do not change the plan's substance include:

- checking completed tasks;
- recording concise verification results;
- recording factual completion notes.

Changes to any of the following require the amendment process:

- scope;
- order;
- implementation approach;
- requirements;
- tasks;
- completion conditions;
- verification obligations.

Do not rewrite completed history merely to make execution appear cleaner.

## 17. Keep Plan Size Proportional

Use as much detail as needed for reliable execution, but no more.

A plan should be detailed because the work requires detail, not because long plans look thorough.

Prefer:

- specific tasks;
- clear ordering;
- explicit completion conditions;
- concise constraints.

Avoid:

- repeated prose;
- generic best-practice essays;
- giant checklists of permanent rules;
- speculative future work;
- process ceremony unrelated to implementation;
- exhaustive command lists before they are relevant.

For a small change, a few ordered tasks may be enough.

For a substantial feature, migration, or release, use phases.

## 18. Recommended Output Structure

Adapt the structure to the task.

Prefer:

```markdown
# <Plan title>

## Goal

<Concrete outcome>

## Fixed decisions

- ...

## Constraints and guardrails

- ...

## Assumptions

- ...

## Non-goals

- ...

## Phase 1: <name>

### Purpose

...

### Tasks

- [ ] ...
- [ ] ...
- [ ] ...

### Completion conditions

- ...
- ...

## Phase 2: <name>

...

## Final verification

<Only if there is verification that is genuinely plan-wide rather than phase-specific.>

## Release / deployment

<Only when applicable.>
```

Do not create empty sections merely to satisfy the template.

## Authorization Boundary

This skill is read-only.

It authorizes inspection, clarification, and creation or revision of a plan only.

It does not authorize implementation, file mutation, command execution, testing, building, package-manager operations, database changes, Git actions, deployment, or other state-changing work.

Follow `AGENTS.md` for universal authorization, preservation, and stopping boundaries.

If the user's request changes from planning to implementation, evaluate that new request independently for authorization.

## Key Principle

Inspect first. Resolve material uncertainty. Build the plan in dependency order. Make every action unambiguous. Once approved, follow the plan or stop and request an amendment.

## Attribution

This skill was adapted from concepts and workflow patterns in:

- `writing-plans` from OpenAI Superpowers:
  https://github.com/openai/plugins/blob/main/plugins/superpowers/skills/writing-plans/SKILL.md
- `executing-plans` from OpenAI Superpowers:
  https://github.com/openai/plugins/blob/main/plugins/superpowers/skills/executing-plans/SKILL.md
- `claude-plan` / `implement-reviewed-plan`:
  https://github.com/sergei-gaponik/claude-plan

The OpenAI Superpowers repository is distributed under the MIT License. See each upstream repository for its complete license text and notices, and verify applicable license terms before redistributing material derived from sources whose licensing is not explicitly stated here.

This version has been substantially modified for sequential user-approved planning, explicit plan fidelity, amendment-before-deviation behavior, proportional verification, solo-development workflows, and strict separation between planning authorization, implementation authorization, and execution authorization.
