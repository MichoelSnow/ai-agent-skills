---
name: session-handoff
description: Create, update, or resume a concise cross-session task handoff only when the user explicitly requests session continuity; never trigger from the existence of a state file or from session length, completion, or agent preference.
---

# Session Handoff

## Purpose

Provide explicit, opt-in continuity between agent sessions or handoffs. This skill is limited to current task state needed for another session to resume work.

## Explicit invocation only

Do not trigger this skill automatically because:

- `docs/session_state.md` or another handoff file exists,
- a task is long-running,
- a session is ending,
- substantial work was completed, or
- a handoff seems useful.

Creating, reading, updating, or maintaining a session-state or handoff file requires explicit user intent in the current request. Suitable requests include creating a handoff, updating session state, preparing work for another agent or session, summarizing progress for later continuation, or resuming from a named/current handoff file.

## Write or update a handoff

When explicitly requested:

1. Inspect the current task and repository state needed for an accurate handoff.
2. Capture only information needed to resume the task.
3. Update an existing project-local handoff file when the user identifies one.
4. Otherwise use `docs/session_state.md`, unless the project defines another conventional location.
5. Replace or remove stale task-state information so the handoff reflects the current state.

A concise handoff may include:

- current objective,
- branch or worktree state when relevant,
- completed work,
- important decisions and rationale,
- relevant files or components,
- unresolved questions or blockers,
- verification already performed,
- remaining work, and
- the next recommended step.

Do not turn a handoff into permanent project history, duplicate architecture documentation, a changelog, a session transcript, or a generic project summary.

## Resume from a handoff

When explicitly requested:

1. Read the specified or project-conventional handoff file.
2. Inspect enough current repository state to detect obvious drift since the handoff.
3. Distinguish handoff claims from repository state verified now.
4. Summarize relevant current state when useful.
5. Continue only within the authorization granted by the current user request.

A handoff does not grant implementation authority merely because a prior session was implementing something. If the repository has materially changed, surface the discrepancy rather than blindly following stale state.

## Authorization and scope

Defer to the repository `AGENTS.md` authority model. In particular:

- session-state creation is not automatic,
- session-state updates are not automatic,
- reading session state is not automatic,
- authorization from a prior session does not carry forward, and
- a request to prepare or read a handoff does not authorize unrelated implementation.

This skill does not add automatic hooks, background updates, mandatory end-of-session behavior, or framework rules. General documentation maintenance belongs to `maintain-docs`.

## Attribution

This skill preserves the useful cross-session task-state capability from the former canonical `docs/core/session_state.md` while intentionally removing its universal requirement to read or update state at every session.
