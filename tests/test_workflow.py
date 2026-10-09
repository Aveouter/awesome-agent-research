from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / ".agents/skills/run-agent-paper-workflow/scripts/workflow.py"
)
SPEC = importlib.util.spec_from_file_location("research_workflow", SCRIPT)
assert SPEC and SPEC.loader
workflow = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(workflow)


class WorkflowTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "notes").mkdir()
        (self.root / "artifacts").mkdir()
        self.tracker = self.root / "papers.md"
        self.tracker.write_text(
            "# Paper Tracker\n\n"
            "| ID | 方向 | 年份/会议 | 论文 | 状态 | Evidence | 笔记 | 下一步 |\n"
            "|---|---|---|---|---|---|---|---|\n"
            "| MA-001 | 多 Agent | 2025 | Example | TO_READ | skimmed | "
            "[导读](notes/example.md) | 精读 |\n",
            encoding="utf-8",
        )
        self.note = self.root / "notes/example.md"
        self.note.write_text(
            "# Example\n\n"
            "- ID：MA-001\n"
            "- Paper：https://example.com/paper\n"
            "- Status：TO_READ（AI 导读已建，本人待精读）\n"
            "- Evidence level：skimmed\n",
            encoding="utf-8",
        )
        self.root_patch = mock.patch.object(workflow, "ROOT", self.root)
        self.tracker_patch = mock.patch.object(workflow, "TRACKER", self.tracker)
        self.root_patch.start()
        self.tracker_patch.start()

    def tearDown(self) -> None:
        self.tracker_patch.stop()
        self.root_patch.stop()
        self.temp_dir.cleanup()

    def test_transition_replaces_the_complete_status_value(self) -> None:
        with mock.patch.object(workflow, "validate", return_value=[]):
            result = workflow.transition("MA-001", "SKIMMED", None)

        self.assertEqual(result, 0)
        self.assertIn("- Status：SKIMMED\n", self.note.read_text(encoding="utf-8"))
        self.assertNotIn("本人待精读", self.note.read_text(encoding="utf-8"))

    def test_transition_rejects_a_reason_that_can_break_the_table(self) -> None:
        original_tracker = self.tracker.read_text(encoding="utf-8")
        original_note = self.note.read_text(encoding="utf-8")

        with mock.patch.object(workflow, "validate", return_value=[]):
            result = workflow.transition("MA-001", "ARCHIVED", "证据不足 | 暂停")

        self.assertEqual(result, 1)
        self.assertEqual(self.tracker.read_text(encoding="utf-8"), original_tracker)
        self.assertEqual(self.note.read_text(encoding="utf-8"), original_note)

    def test_validate_rejects_an_artifact_for_an_untracked_paper(self) -> None:
        (self.root / "artifacts/MA-999").mkdir()

        with mock.patch.object(workflow, "REQUIRED_FILES", set()):
            errors = workflow.validate()

        self.assertIn(
            "artifacts/MA-999: paper ID is absent from papers.md",
            errors,
        )

    def check(self):
        with mock.patch.object(workflow, "REQUIRED_FILES", set()):
            return workflow.validate()

    def test_direct_deep_read_and_history(self):
        with mock.patch.object(workflow, "REQUIRED_FILES", set()):
            self.assertEqual(workflow.transition("MA-001", "DEEP_READ", None), 0)
        self.assertIn("TO_READ → DEEP_READ", self.note.read_text(encoding="utf-8"))
        self.assertIn("Evidence level：skimmed", self.note.read_text(encoding="utf-8"))

    def test_archive_and_restore_confirmed_progress(self):
        with mock.patch.object(workflow, "REQUIRED_FILES", set()):
            self.assertEqual(workflow.transition("MA-001", "DEEP_READ", None), 0)
            self.assertEqual(workflow.transition("MA-001", "ARCHIVED", "暂缓"), 0)
            self.assertEqual(workflow.transition("MA-001", "DEEP_READ", "恢复精读进度"), 0)
        self.assertIn("DEEP_READ → ARCHIVED", self.note.read_text(encoding="utf-8"))

    def test_archive_requires_reason_without_mutation(self):
        original = self.tracker.read_text(encoding="utf-8")
        with mock.patch.object(workflow, "REQUIRED_FILES", set()):
            self.assertEqual(workflow.transition("MA-001", "ARCHIVED", None), 1)
        self.assertEqual(original, self.tracker.read_text(encoding="utf-8"))

    def test_duplicate_id_title_and_note(self):
        row = self.tracker.read_text(encoding="utf-8").splitlines()[-1]
        with self.tracker.open("a", encoding="utf-8") as f:
            f.write(row + "\n")
        errors = "\n".join(self.check())
        self.assertIn("duplicate paper ID", errors)
        self.assertIn("duplicate paper title", errors)
        self.assertIn("duplicate canonical note path", errors)

    def test_duplicate_source_across_arxiv_versions(self):
        self.note.write_text(self.note.read_text(encoding="utf-8").replace("https://example.com/paper", "https://arxiv.org/abs/2503.13657v1"), encoding="utf-8")
        second = self.note.read_text(encoding="utf-8").replace("MA-001", "MA-002").replace("/abs/2503.13657v1", "/pdf/2503.13657v2.pdf")
        (self.root / "notes/second.md").write_text(second, encoding="utf-8")
        with self.tracker.open("a", encoding="utf-8") as f:
            f.write("| MA-002 | 多 Agent | 2025 | Other title | TO_READ | skimmed | [note](notes/second.md) | 阅读 |\n")
        self.assertTrue(any("duplicate paper source" in e for e in self.check()))

    def test_optional_artifacts_directory_and_short_note(self):
        (self.root / "artifacts").rmdir()
        self.assertEqual(self.check(), [])

    def test_status_and_evidence_mismatches(self):
        content = self.note.read_text(encoding="utf-8").replace("Status：TO_READ", "Status：SKIMMED").replace("Evidence level：skimmed", "Evidence level：full-paper")
        self.note.write_text(content, encoding="utf-8")
        errors = "\n".join(self.check())
        self.assertIn("status 'SKIMMED' does not match", errors)
        self.assertIn("evidence 'full-paper' does not match", errors)

    def test_readme_cannot_duplicate_paper_progress(self):
        (self.root / "README.md").write_text("Example · `TO_READ / skimmed`", encoding="utf-8")
        self.assertTrue(any("per-paper status" in e for e in self.check()))

    def test_legacy_warns_and_never_silently_migrates(self):
        for p in [self.tracker, self.note]:
            p.write_text(p.read_text(encoding="utf-8").replace("TO_READ", "REPRODUCED"), encoding="utf-8")
        self.assertEqual(self.check(), [])
        self.assertTrue(workflow.compatibility_warnings())
        before = self.tracker.read_text(encoding="utf-8")
        with mock.patch.object(workflow, "REQUIRED_FILES", set()):
            self.assertEqual(workflow.transition("MA-001", "DEEP_READ", "未知人工进度"), 1)
        self.assertEqual(before, self.tracker.read_text(encoding="utf-8"))

    def test_ai_evidence_does_not_change_human_status(self):
        for p in [self.tracker, self.note]:
            p.write_text(p.read_text(encoding="utf-8").replace("skimmed", "full-paper"), encoding="utf-8")
        self.assertEqual(self.check(), [])
        self.assertIn("Status：TO_READ", self.note.read_text(encoding="utf-8"))

    def test_broken_link_and_duplicate_note_id(self):
        (self.root / "notes/duplicate.md").write_text(self.note.read_text(encoding="utf-8") + "\n[missing](missing.md)\n", encoding="utf-8")
        errors = "\n".join(self.check())
        self.assertIn("duplicate note ID", errors)
        self.assertIn("broken local link", errors)

    def test_validation_is_read_only(self):
        originals = {p: p.read_bytes() for p in [self.tracker, self.note]}
        self.assertEqual(self.check(), [])
        self.assertEqual(originals, {p: p.read_bytes() for p in originals})

    def test_research_files_are_not_required(self):
        self.assertFalse(any(p.startswith(("artifacts/", "research/", "experiments/")) for p in workflow.REQUIRED_FILES))

    def test_readme_standalone_status_is_rejected(self):
        (self.root / "README.md").write_text("| MA-001 | DEEP_READ |", encoding="utf-8")
        self.assertTrue(any("per-paper status" in e for e in self.check()))

    def test_legacy_values_are_not_transition_targets(self):
        with mock.patch.object(workflow, "REQUIRED_FILES", set()):
            for status in workflow.LEGACY_STATUSES:
                with self.subTest(status=status):
                    self.assertEqual(workflow.transition("MA-001", status, None), 1)

    def test_rereading_does_not_demote_deep_read(self):
        with mock.patch.object(workflow, "REQUIRED_FILES", set()):
            self.assertEqual(workflow.transition("MA-001", "DEEP_READ", None), 0)
            self.assertEqual(workflow.transition("MA-001", "SKIMMED", None), 1)


if __name__ == "__main__":
    unittest.main()
