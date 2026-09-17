---
name: verify
description: Verify claims about completed or changed work using evidence proportional to the claim, risk, and cost. Use before asserting that code works, a bug is fixed, tests pass, a build succeeds, requirements are met, data or analytical output is correct, or an implementation is complete. Choose the narrowest sufficient evidence rather than the broadest available command. Do not modify implementation merely because verification fails unless repair is separately authorized.
---

# Verify

## Goal

Make only claims that are supported by appropriate evidence.

Verification is claim-driven, not command-driven. Determine what needs to be established, then use the smallest reliable check that proves it.

## 1. Identify the Claim

Before verifying, state internally what is actually being claimed.

Examples:

- this targeted behavior works,
- this bug no longer reproduces,
- these tests pass,
- this model builds,
- this query produces the intended result,
- this notebook runs coherently,
- the requested requirements are satisfied.

Do not broaden the claim beyond what the task requires.

## 2. Determine What Evidence Would Prove It

Choose evidence that directly corresponds to the claim.

Examples:

- a targeted behavioral test for a behavior claim,
- reproduction of the original symptom for a bug-fix claim,
- test output for a test claim,
- build output for a build claim,
- rendered behavior for a UI claim,
- schema or row-level checks for a data claim,
- expected metrics or known examples for an analytical claim,
- acceptance criteria for a requirements claim.

One evidence type does not automatically prove another.

A passing linter does not prove a build succeeds. A successful build does not prove runtime behavior. Passing tests do not automatically prove every requirement was met.

## 3. Use the Narrowest Sufficient Check

Prefer the least expensive check that provides sufficient evidence for the current claim.

Consider:

- execution time,
- compute or monetary cost,
- data volume,
- external API usage,
- amount of affected state,
- feedback speed,
- operational risk,
- whether broader verification provides useful additional evidence at this stage.

Do not run a broader test suite, build, data job, model training process, or validation command merely because it is more comprehensive.

For example, if a targeted command fully establishes the requested behavior, a much broader command that adds unrelated validation may be unnecessary.

Broaden verification when:

- the narrow check cannot support the claim,
- the change affects shared or cross-cutting behavior,
- repository rules require broader validation,
- the consequence of an undetected regression justifies the additional cost.

If two reasonable verification approaches differ materially in time, cost, scope, or risk and the required level is unclear, ask before choosing the expensive one.

## 4. Prefer Fresh, Relevant Evidence

Evidence must reflect the state being claimed.

Later changes invalidate only the evidence they could affect.

Reuse sufficiently fresh evidence when:

- it was produced against the current relevant state,
- nothing material to that check has changed,
- it directly supports the current claim.

Do not rerun commands mechanically merely to make evidence newer.

Do not rely on stale evidence after relevant code, configuration, data, or environment changes.

## 5. Run and Read the Check

Execute the chosen verification when execution is authorized and available.

Inspect the actual result.

Depending on the check, examine:

- exit status,
- failures and warnings,
- returned values,
- rendered output,
- row counts,
- schemas,
- logs,
- metrics,
- expected records or examples,
- differences from baseline.

Do not treat command execution itself as verification.

Do not ignore contradictory output because the command exited successfully.

## 6. Compare Evidence to the Exact Claim

Ask:

- Does this evidence directly establish the claim?
- Does it establish only part of the claim?
- Did the check reveal contradictory evidence?
- Are there material conditions that were not exercised?

Make only the strongest statement the evidence supports.

Examples:

- If three targeted tests pass, say those tests pass.
- If the complete relevant suite passes, say the relevant suite passes.
- If only static inspection was possible, do not claim runtime behavior was verified.
- If the original bug no longer reproduces under the tested conditions, state those conditions when they matter.

Do not extrapolate from partial evidence.

## 7. Verify Behavior, Not Just Machinery

When correctness depends on an observable outcome, verify the outcome.

Examples:

- UI work may require inspecting rendered behavior rather than only unit tests.
- Data transformations may require checking representative records or aggregates rather than only successful execution.
- Configuration changes may require confirming the intended provider/runtime behavior rather than only syntax validity.
- Analytical work may require checking known cases, metric behavior, or expected invariants rather than only that code ran.

A command succeeding is not proof that the intended outcome occurred.

## 8. Verify Requirements Separately When Needed

Technical checks and requirement satisfaction are different questions.

For non-trivial work, compare the resulting behavior against the requested acceptance criteria or project contract.

Do not infer that requirements are satisfied merely because tests pass unless those tests actually cover the requirements.

Do not create a ceremonial checklist for trivial work when the requested outcome is directly observable.

## 9. Handle Failed Verification

If verification fails:

- report the failure accurately,
- preserve the evidence,
- identify what claim is now unsupported,
- use narrow diagnostics to understand the failure when appropriate.

Do not silently change implementation as part of verification unless repair was separately authorized.

Do not stack speculative fixes merely to obtain a passing result.

If the failure reveals material ambiguity about intended behavior, stop and clarify.

## 10. Report Verification Boundaries

When full verification is impractical, unavailable, or intentionally unnecessary, distinguish:

- **Verified:** what the evidence established,
- **Not verified:** what was not checked,
- **Remaining risk:** material uncertainty that still matters.

Keep this proportional. Do not produce a formal verification report for a trivial change unless requested.

Do not describe unverified work as complete if the missing evidence is necessary to support the completion claim.

## 11. Respect Repository Requirements

When applicable, project-specific verification rules define additional checks. Apply them subject to the authority order in `AGENTS.md`; current user instruction and authorization/safety boundaries remain above project requirements and this skill.

Use required:

- test commands,
- acceptance checks,
- security gates,
- framework audits,
- CI expectations,
- data validation rules.

Applicable repository requirements can mandate broader verification than this skill would otherwise choose, but they do not authorize implementation or other mutation.

Do not invent broader requirements that the project does not have.

## Authorization Boundary

Verification authorizes only the checks necessary to establish the requested claim when those checks are safe and within the user's existing authorization.

Do not use verification as permission to:

- modify implementation,
- repair failures,
- rewrite tests to make them pass,
- mutate production data,
- deploy,
- run destructive operations,
- commit, merge, or push.

If a verification step itself is expensive, destructive, externally consequential, or materially broader than the user's request, obtain authorization first.

## Key Principle

Claim -> required evidence -> narrowest sufficient check -> inspect result -> make only the claim the evidence supports.

## Attribution

This skill was adapted from concepts and workflow patterns in:

- `verification-before-completion` from `obra/superpowers`: https://github.com/obra/superpowers/tree/main/skills/verification-before-completion
- `verification-before-completion` from `eagleagentic/superpowers-gpt-5.6`: https://github.com/eagleagentic/superpowers-gpt-5.6/tree/main/skills/superpowers/verification-before-completion
- verification adaptations from `netzkontrast/agency-backups`: https://github.com/netzkontrast/agency-backups
- `validate-implementation` from `tomzx/agents`: https://github.com/tomzx/agents/tree/main/skills/validate-implementation

See each upstream repository for its complete license terms and notices before redistributing copied or derivative material.

This version has been substantially modified to make verification claim-driven and proportional, prefer the narrowest sufficient evidence over universally running full command suites, account for execution cost and risk, reuse sufficiently fresh evidence, distinguish behavioral evidence from mechanical success, and preserve a strict boundary between verification and repair.
