# 仓库使用说明

个人 Agent 论文阅读与知识记录系统。最小流程为收藏 → 正式收录 → 记录理解，连接与回顾按需进行。无需研究假设、实验设计或固定日志。

## 目录

核心：inbox.md（收藏）、papers.md（唯一状态总表）、notes/（唯一主笔记）、references/library.bib（引用）、templates/paper-note.md（阅读模板）。syntheses/ 用于跨论文总结；concepts/、entities/ 可选。artifacts/、research/、experiments/、reports/、logs/ 和研究模板是可选扩展与历史资料，保留但不是普通阅读校验依赖。

## 完整例子（演示，不新增登记）

1. **收藏**：在 [inbox](../inbox.md) 写 “Why Do Multi-Agent LLM Systems Fail?”、[原文链接](https://arxiv.org/abs/2503.13657)，可选理由“了解协作失败类型”。不建 ID 或笔记。
2. **正式收录**：检索总表发现已有 MA-001，复用 [原笔记](../notes/multi-agent/why-mas-fail.md)，inbox 标注“已登记 MA-001”。真正的新论文才分配未使用 ID、复制模板、登记总表与 BibTeX，默认 TO_READ。同论文不同版本不重复登记。
3. **阅读记录**：速读填 TL;DR 和 Takeaways，精读补 Method 和 Evidence，记录数据集、指标、表 5/附录 H 等已核验位置及版本。仅用户确认后修改人工状态；MA-001 已确认 DEEP_READ，保持不变，Evidence skimmed 不猜测升级。
4. **关联**：Connections 链接 [MA-002](../notes/multi-agent/multiagentbench.md)，说明失败分类与协作评测的关系，较长对照可写 syntheses，无需概念页。
5. **重读**：更新 MA-001 原笔记，Reading History 追加日期、证据与理解变化，保留旧判断并说明修正理由。不建重复笔记、不回退 DEEP_READ。暂缓用 ARCHIVED，保留原状态；恢复可回到 DEEP_READ。

## 校验与 Git

状态、Evidence、历史兼容和 Git 规则见 [WORKFLOW](../WORKFLOW.md)。AI 导读不会自动修改人工状态；README 仅列元数据和链接，笔记状态是总表镜像。

```bash
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py validate
python3 -m unittest discover -s tests
python3 scripts/check_git_boundary.py --staged
```

本次重构独立分支与 PR，合并后普通阅读可按批次提交并共用 PR；规则、脚本、模板、迁移仍独立维护 PR。保留 hooks 与 CI，不直接推送 main。按 [文件边界](storage-boundaries.md) 将 PDF、Zotero、全文提取和附件留在 D:\paper，本次不迁移本地数据。
