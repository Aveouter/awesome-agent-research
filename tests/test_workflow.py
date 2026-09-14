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
            result = workflow.transition("MA-001", "DROPPED", "证据不足 | 暂停")

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


if __name__ == "__main__":
    unittest.main()
