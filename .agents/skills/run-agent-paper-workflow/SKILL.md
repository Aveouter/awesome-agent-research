---
name: run-agent-paper-workflow
description: Manage this repository's Agent paper intake, structured reading, reviewer-style critique, validation design, reproduction tracking, cross-paper synthesis, and quality audit. Use for adding, reading, comparing, auditing, or updating research papers in this repo; do not use for unrelated research outside the repository.
---

# Run Agent Paper Workflow

Paths are relative to the repository root.

## Route the request

- **Intake** — user provides a paper and wants it collected: duplicate-check, assign an ID, add metadata and create one note.
- **Read** — user asks to skim or deeply read: inspect the primary paper, update its note, evidence level and tracker status.
- **Critique** — user asks for weaknesses, reviewer questions or research gaps: require a sufficiently complete note; write `artifacts/<paper-id>/critic.md`.
- **Validate** — user asks how to test a claim: require critique; write `design.md`, then `spec.md` only if implementation is requested.
- **Reproduce** — user asks to run an experiment: create or update `experiments/<paper-id>-<slug>/`, record configuration, cost and results, then transition status.
- **Synthesize** — user asks to compare papers or choose a direction: align methods, datasets, metrics and results in `syntheses/`; cite source notes and expose evidence gaps.
- **Audit** — user asks to check analysis quality, or a full chain is ready: inspect without silently rewriting; write `audit.md` with blocking and non-blocking findings.

For exact status transitions, artifact boundaries and completion criteria, read the relevant section of `WORKFLOW.md`. Use terminology from `CONTEXT.md`.

## Preflight

1. Search `papers.md`, `notes/`, `artifacts/` and `references/library.bib` before creating anything.
2. Resolve paper metadata from an authoritative source. When reading claims, use the paper PDF or official full text rather than search snippets or third-party summaries.
3. Preserve user-written content and unrelated changes.
4. Do not commit PDFs, model weights, datasets, secrets or large raw traces.

## Evidence contract

- Every numeric main result should name its dataset and metric and, when available, its table, figure or page.
- Label statements as author-reported, indirect observation or reader inference when the distinction matters.
- Write “原文未报告” for absent details; do not infer training settings, baselines or hardware.
- Keep `status` and `evidence_level` separate. AI-assisted reading may improve evidence level but must not claim the user personally read the paper.
- Prefer updating a canonical note to creating a duplicate.

## Full-analysis mode

Only use the full chain for an anchor paper, a direct competing work, or a paper the user intends to reproduce:

```text
note → extract → critic → design → spec → audit
```

Use templates from `templates/`. Each stage consumes the previous stage and stays within the boundary documented in `AGENTS.md`. If a prerequisite is missing, produce the missing upstream artifact first when the request authorizes that work; otherwise report the dependency.

## Repository commands

```bash
# Summary of the tracker
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py status

# Validate IDs, states, evidence levels, notes and local links
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py validate

# Apply a valid lifecycle transition to tracker and canonical note
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py transition MA-001 SKIMMED
```

Do not use `transition` as a substitute for doing the work required by the target state's definition of done.

## Finish

Run `validate`. Report the files changed, current status and evidence level, important missing evidence and the smallest useful next step. Do not publish or change repository visibility unless the user explicitly asks.
