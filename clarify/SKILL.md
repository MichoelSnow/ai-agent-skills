---
name: clarify
description: Clarifies materially ambiguous requests before action. Use when unresolved intent, scope, constraints, success criteria, destructive consequences, or consequential trade-offs could materially change what should be done, across engineering, data science, analysis, planning, or other work. Do not use merely because more information could be useful, when the answer is available from existing context, or when remaining uncertainty would not change the immediate next step.
metadata:
  version: 1.0.0
---

# Clarify

## Goal

Prevent wrong work by resolving only the uncertainties that materially affect the immediate next step.

Do not pursue completeness for its own sake.

## Workflow

### 1. Inspect before asking

First use the context already available to you.

When relevant, inspect low-risk sources that can resolve the uncertainty without committing to a solution, such as:

- existing code and configuration,
- repository instructions and documentation,
- data already provided,
- prior decisions in the current context.

Do not ask the user for information that can be determined reliably from available context.

### 2. Decide whether clarification is necessary

Ask only when an unresolved answer could materially change what should be done.

Material uncertainty commonly includes:

- the objective or intended outcome,
- what is in or out of scope,
- important constraints,
- what constitutes success,
- a consequential technical or analytical choice,
- conflicting requirements,
- potentially destructive or difficult-to-reverse actions.
- the appropriate scope of the immediate action,
- a choice that could materially change execution time, compute cost, or operational risk,
- whether legacy or backward compatibility is actually required,

When two plausible interpretations would lead to meaningfully different amounts of work, cost, risk, or implementation scope, resolve that ambiguity before acting.

Do not trigger clarification merely because:

- additional context might be interesting,
- several reasonable implementation details remain,
- a standard project convention already answers the question,
- the remaining uncertainty would not change the immediate next step.

### 3. Ask the highest-value questions

Ask 1-3 questions per round.

Prioritize questions that eliminate the largest branches of possible work.

Make questions easy to answer:

- be concise and specific,
- provide concrete options when they clarify a real decision,
- briefly state meaningful trade-offs when relevant,
- recommend a default when you have enough evidence to do so,
- avoid vague questions when a more precise question is possible.

Do not manufacture options when an open question would be clearer.

### 4. Stop when clarification stops being valuable

After each response, reassess only the uncertainty relevant to the immediate next step.

Ask another round only if the user's answers reveal new material uncertainty.

Stop questioning when remaining uncertainty would not materially change the immediate next step. Do not continue interviewing the user simply because additional questions are possible.

When low-impact uncertainty remains, state the assumption if it matters and leave it for the downstream task rather than continuing clarification.


### 5. Confirm interpretation, then proceed

Once you have answers, restate the requirements in 1-3 sentences (including key constraints and what success looks like), then start work.

## Question templates

- "Before I start, I need: (1) ..., (2) ..., (3) .... If you don't care about (2), I will assume ...."
- "Which of these should it be? A) ... B) ... C) ... (pick one)"
- "What would you consider 'done'? For example: ..."
- "Any constraints I must follow (versions, performance, style, deps)? If none, I will target the existing project defaults."
- Use numbered questions with lettered options and a clear reply format

```text
1) Scope?
a) Minimal change (default)
b) Refactor while touching the area
c) Not sure - use default
2) Compatibility target?
a) Current project defaults (default)
b) Also support older versions: <specify>
c) Not sure - use default

Reply with: defaults (or 1a 2a)
```

## Anti-patterns

- Don't ask questions you can answer with a quick, low-risk discovery read (e.g., configs, existing patterns, docs).
- Don't ask open-ended questions if a tight multiple-choice or yes/no would eliminate ambiguity faster.

## Authorization Boundary

Follow the repository's `AGENTS.md` authority model for universal authorization and scope boundaries. Clarification is not authorization to implement; while this skill is active, perform only the low-risk read-only investigation needed to resolve the uncertainty.

Low-risk read-only investigation needed to clarify the request is allowed.

Once the request is sufficiently clarified, stop this workflow. Do not transition into implementation unless the current user instruction independently and explicitly authorizes it.

## Key Principle

Investigate first. Ask only decision-relevant questions. Stop when the remaining uncertainty no longer changes the immediate next step.


## Attribution

This skill was adapted from concepts and workflow patterns in:

- `ask-questions` from `ferueda/agent-skills`: https://github.com/ferueda/agent-skills
- `asking-questions` from `oaustegard/claude-skills`: https://github.com/oaustegard/claude-skills

The resulting skill has been modified substantially for broader automatic triggering, bounded clarification rounds, diminishing-return stopping behavior, and explicit authorization boundaries.

`oaustegard/claude-skills` is distributed under the MIT License. See the upstream repository for the complete license text.