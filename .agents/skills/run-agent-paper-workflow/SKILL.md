---
name: run-agent-paper-workflow
description: Capture, register, read, connect, review or update Agent papers in this repository while preserving canonical notes, human progress and source evidence. Not for unrelated research.
---

# Run Agent Paper Workflow

Paths are relative to repository root. Read CONTEXT.md and the matching WORKFLOW.md stage first.

## Route and complete

- **Capture**: title, primary URL and optional reason go in inbox.md only. Finish without ID, tracker row or note.
- **Register**: search papers.md, notes/ and references/library.bib by title, DOI/arXiv ID and URL. Reuse existing paper/version identity; otherwise assign an unused ID, create one template note and register tracker + citation together. Mark inbox disposition. Finish with one ID and one note.
- **Read**: inspect official paper/full text, update canonical note and actual Evidence. Skim needs Metadata, TL;DR and Takeaways; deep reading adds Method and Evidence. Change human Status only when user explicitly confirms or authorizes progress.
- **Connect**: optional note links; compare methods, datasets and metrics in syntheses/. Concepts/entities are optional.
- **Review**: retrieve, correct or reread original note; append understanding changes and evidence positions. Preserve human content and confirmed progress.

## Evidence and preservation

Prefer paper homepages, conferences, publishers or arXiv. Numeric results name dataset, metric, available table/figure/page and version. Distinguish author reports, direct evidence, indirect observation and reader inference. Missing: “原文未报告”; unverified: “原文尚未核实”. AI may improve Evidence without changing Status. Use WORKFLOW.md transitions and explicit legacy migration; never silently convert old states.

Facts and critique belong in the main note. Historical artifacts, research and experiments are optional and preserved. Generate extract/critic/design/spec/audit only on explicit request for staged research products, using AGENTS.md boundaries and templates/. Ordinary reading requires no hypothesis or experiment.

Read docs/storage-boundaries.md before handling local attachments. Keep PDFs, Zotero databases, full-text extraction, secrets and large binaries outside Git. Git rules are in WORKFLOW.md.

## Commands and finish

```bash
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py status
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py validate
# Only after user confirms human progress:
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py transition MA-001 DEEP_READ
```

Run validate after changes. Report changed records, unchanged/confirmed human Status, Evidence, source gaps and next reading step. Do not publish or change visibility without explicit request.
