---
name: review
description: Perform a read-only, evidence-based review of code or a branch. Use when the user asks to review, inspect, assess, audit, or critique changes without modifying them. Focus on concrete defects, regressions, security issues, data integrity risks, performance problems, and maintainability concerns that are supported by the actual code path and project context. Do not use to implement fixes unless the user separately authorizes changes.
---

# Review

## Goal

Assess whether a change is correct, safe, and appropriate for the project without modifying code.

Prioritize real defects and meaningful risks over style preferences, speculative concerns, or enterprise assumptions that do not apply to the project.

## 1. Preserve the Read-Only Boundary

Review is read-only.

Do not:

- edit files,
- apply patches,
- run mutating commands,
- change configuration,
- fix findings,
- refactor code,
- update documentation,

unless the user separately and explicitly authorizes implementation.

A request to review, audit, inspect, critique, or assess does not authorize fixes.

If the user asks what should be changed, describe the change rather than applying it.

## 2. Establish Review Scope

Determine what is being reviewed.

Examples:

- current branch vs base branch,
- a pull request,
- a specific commit,
- selected files,
- a proposed design or implementation,
- a notebook or analysis artifact.

Use the narrowest scope that matches the request.

When reviewing a branch, identify the correct comparison base rather than assuming one if the repository context makes it uncertain.

Do not expand the review to unrelated code merely because adjacent issues are visible.

## 3. Establish Intended Behavior

Before judging correctness, determine what the change is supposed to do.

Use authoritative project evidence when available:

- user instructions,
- project rules,
- specs,
- contracts,
- tests,
- schemas,
- documentation,
- established code behavior,
- accepted design decisions.

Do not replace project intent with generic best practices.

If expected behavior is ambiguous and the ambiguity could materially change the review finding, resolve it before treating the issue as a defect.

## 4. Inspect the Complete Change

Review the full relevant change, not isolated lines.

When needed, inspect surrounding context such as:

- callers,
- downstream consumers,
- related tests,
- schemas,
- validation logic,
- configuration,
- migrations,
- interfaces,
- adjacent code paths.

A diff may suggest a problem that surrounding code disproves.

Do not report a finding solely because one line looks suspicious.

## 5. Review for Defects First

Prioritize findings in this order:

### Correctness

Look for:

- logic errors,
- broken edge cases,
- incorrect state transitions,
- wrong assumptions,
- missing required behavior,
- unintended regressions.

### Security

Look for:

- exposed secrets,
- missing authentication or authorization,
- injection risks,
- unsafe input handling,
- insecure data access,
- destructive behavior without safeguards.

### Data Integrity

Look for:

- silent data loss,
- incorrect schema handling,
- destructive migrations,
- invalid transformations,
- inconsistent source-of-truth behavior,
- stale or incompatible persisted data.

### Reliability and Error Handling

Look for:

- failures that are swallowed,
- incorrect retry behavior,
- non-idempotent operations where that matters,
- partial-failure hazards,
- misleading success states.

### Performance and Cost

Look for:

- unexpectedly expensive queries or operations,
- unnecessary full scans or large builds,
- avoidable repeated computation,
- pathological scaling behavior,
- broad validation or execution whose cost is disproportionate to the requested task.

Judge performance relative to actual project scale and usage.

### Maintainability

Look for maintainability issues only when they create a concrete risk, such as:

- duplicated logic likely to diverge,
- misleading abstractions,
- hidden coupling,
- dead compatibility paths,
- unnecessary legacy code,
- changes that conflict with established project patterns.

Do not report stylistic preference as maintainability risk.

## 6. Respect Project Scale and Intent

Review the project that actually exists.

Do not impose:

- enterprise compatibility requirements on a solo project,
- speculative scalability requirements,
- unnecessary abstractions,
- mandatory legacy support,
- production-grade infrastructure where the project does not need it.

Backward compatibility is a requirement only when the project actually has consumers or constraints that require it.

A breaking change is not automatically a defect if it is intentional and appropriate for the project.

## 7. Generate Candidate Findings

During review, treat suspected problems as candidate findings.

For each candidate, determine:

- what behavior is expected,
- what the code actually does,
- what path triggers the issue,
- what impact results,
- whether the reviewed change introduced or exposed it.

Do not report a candidate yet if the evidence is incomplete.

## 8. Verify Every Finding

Before reporting a finding, independently verify it against the code and project context.

Use the cheapest useful evidence source, such as:

- tracing the relevant code path,
- checking a caller or consumer,
- reading a related test,
- comparing with a contract or schema,
- checking configuration,
- using a read-only static or targeted runtime check when appropriate.

Drop findings that are:

- contradicted by surrounding code,
- based on assumptions rather than evidence,
- merely hypothetical without a plausible trigger,
- subjective style preferences,
- outside the requested scope,
- already intentionally handled by project rules.

A plausible concern is not yet a finding.

## 9. Prioritize by Impact

Report only findings that are worth the user's attention.

Use severity based on likely impact:

### Critical

Likely to cause severe security compromise, destructive data loss, or catastrophic failure.

### Major

Likely to cause incorrect behavior, meaningful regression, significant data/reliability problems, or serious operational risk.

### Minor

Real but limited-impact defects or maintainability risks worth fixing.

Do not inflate severity because a theoretical worst case exists.

Do not bury important findings under numerous low-value comments.

## 10. Keep Findings Actionable

Each reported finding should include:

- where the issue occurs,
- what is wrong,
- why it matters,
- the evidence supporting it,
- the condition under which it occurs.

When useful, describe the general direction of the fix, but do not implement it.

Avoid vague comments such as:

- "this could be cleaner,"
- "consider refactoring,"
- "this may be inefficient,"

unless you can identify the actual failure or risk.

## 11. Review Tests Proportionately

Assess whether validation is appropriate for the change.

Do not automatically demand a full test suite.

Consider:

- whether new behavior has meaningful coverage,
- whether important failure modes are tested,
- whether the existing test level matches the project's maturity,
- whether a narrower test would provide sufficient confidence,
- whether broad test execution would be disproportionately expensive.

Flag missing tests when the lack of coverage creates meaningful regression risk.

Do not treat "more tests" as inherently better.

## 12. Use Project-Specific Review Rules When Present

If the repository contains review instructions, framework audits, project rules, or contracts that apply to the requested review, use them.

Examples include:

- `AGENTS.md`,
- `CLAUDE.md`,
- project-specific rules,
- review templates,
- architecture contracts,
- security baselines.

Do not silently substitute generic review criteria for explicit repository requirements.

If a project-specific review workflow conflicts with this skill, follow the project-specific requirement for that repository.

## 13. Output

Lead with findings, ordered by severity.

For each finding, be concise and evidence-based.

After findings, optionally include:

- a short overall assessment,
- notable strengths only when they materially affect confidence,
- unresolved review limitations.

If no meaningful findings are verified, say so directly.

Do not invent issues to make the review appear thorough.

## Authorization Boundary

This skill is strictly read-only.

Finding a defect, agreeing that it should be fixed, or describing the correct fix does not authorize implementation.

If the user later asks to make changes, transition to an implementation workflow only after that separate instruction.

## Key Principle

Review the code that exists, against the behavior this project actually requires. Verify every finding before reporting it.

## Attribution

This skill was adapted from concepts and workflow patterns in:

- `review-agent` from OpenAI Codex: https://github.com/openai/codex/tree/main/codex-rs/skills/src/assets/samples/review-agent
- PR-Agent from Codium-ai/Qodo: https://github.com/qodo-ai/pr-agent
- `code-review` from Anthropic's `knowledge-work-plugins`: https://github.com/anthropics/knowledge-work-plugins/tree/main/engineering/skills/code-review
- `code-review-and-quality` from `addyosmani/agent-skills`: https://github.com/addyosmani/agent-skills/tree/main/skills/code-review-and-quality
- `code-review` from `JUNERDD/skills`: https://github.com/JUNERDD/skills/tree/main/skills/code-review
- autoreview concepts from `openclaw/agent-skills`: https://github.com/openclaw/agent-skills

See each upstream repository for its complete license terms and notices before redistributing copied or derivative material.

This version has been substantially modified to emphasize read-only review, evidence verification, false-positive suppression, project-specific intent, proportional validation, and review standards appropriate to solo and small-project development as well as larger systems.
