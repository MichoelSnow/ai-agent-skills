# AI Agent Skills

Central repository for reusable Agent Skills shared across Codex and Claude Code.

The goal is to maintain one version-controlled source of truth for skills so improvements automatically propagate to every local project that uses them.

## Repository Layout

```text
ai-agent-skills/
├── README.md
├── skill_authoring_guide.md
├── clarify/
│   └── SKILL.md
├── debug/
│   └── SKILL.md
└── ...
```

Each skill should follow the conventions in `skill_authoring_guide.md`.

## Installation

Clone this repository into your Git directory:

```bash
cd ~/git
git clone <repository-url> ai-agent-skills
```

The examples below assume the repository lives at:

```text
~/git/ai-agent-skills
```

## Link Skills to Codex and Claude Code

Codex and Claude Code may already use their own `skills` directories. Do **not** replace those directories wholesale.

Instead, create a symlink for each custom skill from this repository into both agents' skill directories.

Create the parent directories if needed:

```bash
mkdir -p ~/.codex/skills ~/.claude/skills
```

The links can be created or refreshed safely with:

```bash
python3 link_skills.py
```

The script discovers top-level directories containing `SKILL.md`. Existing
links from this repository are skipped. Other entries with the same skill name
produce warnings and are left untouched; the script continues processing and
exits with a nonzero status if any conflicts occur.

For each skill in this repository, create links such as:

```bash
ln -s ~/git/ai-agent-skills/clarify ~/.codex/skills/clarify
ln -s ~/git/ai-agent-skills/clarify ~/.claude/skills/clarify

ln -s ~/git/ai-agent-skills/debug ~/.codex/skills/debug
ln -s ~/git/ai-agent-skills/debug ~/.claude/skills/debug
```

The resulting structure should look like:

```text
~/.codex/skills/
├── .system/        # Codex-managed built-in skills; leave untouched
├── clarify -> ~/git/ai-agent-skills/clarify
└── debug   -> ~/git/ai-agent-skills/debug

~/.claude/skills/
├── clarify -> ~/git/ai-agent-skills/clarify
└── debug   -> ~/git/ai-agent-skills/debug
```

## Existing Skills

Before creating a symlink, check whether that skill name already exists:

```bash
ls -la ~/.codex/skills
ls -la ~/.claude/skills
```

Do not overwrite:

- Codex-managed `.system/` content
- existing real directories
- unrelated existing symlinks

If a name conflict exists, resolve it manually before creating the link.

## Verify the Setup

Check the created links:

```bash
ls -l ~/.codex/skills
ls -l ~/.claude/skills
```

Each custom skill should resolve to its directory inside:

```text
~/git/ai-agent-skills/
```

For example:

```text
clarify -> /home/<user>/git/ai-agent-skills/clarify
debug   -> /home/<user>/git/ai-agent-skills/debug
```

## Updating Skills

Because both agents point directly to this repository, changes to a skill are immediately available through both symlinked locations.

To receive updates from Git:

```bash
cd ~/git/ai-agent-skills
git pull
```

Local edits can be committed and pushed normally:

```bash
git add .
git commit -m "Refine agent skills"
git push
```

Other machines can then receive the changes with `git pull`.

## Adding a New Skill

Add the new skill directory to this repository and create corresponding symlinks for Codex and Claude Code:

```bash
ln -s ~/git/ai-agent-skills/<skill-name> ~/.codex/skills/<skill-name>
ln -s ~/git/ai-agent-skills/<skill-name> ~/.claude/skills/<skill-name>
```

Do not copy the skill into the agent-specific directories. The repository should remain the single source of truth.

## Adding a New Machine

On each machine:

1. Clone this repository to `~/git/ai-agent-skills`.
2. Ensure `~/.codex/skills` and `~/.claude/skills` exist.
3. Create per-skill symlinks into both directories.
4. Verify the links resolve to this repository.

No skills need to be copied into individual project repositories unless a skill is genuinely project-specific.

## Scope

This repository should contain reusable workflows that describe **how an agent should work**.

Project-specific facts, architecture decisions, environment constraints, and repository conventions should remain in the relevant project's `AGENTS.md`, `CLAUDE.md`, or project documentation.
