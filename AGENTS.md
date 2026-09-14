# AGENTS.md

本仓库是个人博士阶段的 Agent 研究知识库。Agent 的目标不是堆积摘要，而是维护可追溯的证据、研究判断和可验证实验。

## 开始工作前

1. 阅读 `CONTEXT.md`，使用仓库定义的术语。
2. 阅读 `WORKFLOW.md` 中与当前请求对应的阶段。
3. 检查 `papers.md` 和现有笔记，避免重复收录或覆盖人工记录。
4. 论文任务优先使用 `.agents/skills/run-agent-paper-workflow/SKILL.md`。

## 内容层次

- `inbox.md`：尚未筛选的候选论文。
- `papers.md`：论文 ID、阅读状态和证据等级的唯一总表。
- `notes/`：每篇论文唯一的、供人阅读的主笔记。
- `artifacts/<paper-id>/`：核心论文的 extract、critic、design、spec、audit 分阶段产物。
- `concepts/`：跨论文稳定概念。
- `entities/`：数据集、benchmark、方法、实验室等实体页。
- `syntheses/`：跨论文对比和综合判断。
- `reports/`：月报、方向报告和阶段性长文。
- `research/`：当前方向地图和待验证想法。
- `experiments/`：复现代码、配置和汇总结果。

## 不变量

- 论文主页、会议页面、出版方或 arXiv 是元数据与主张的首选来源。
- 数值结论尽量标注页码、表格或图编号；没有核实就明确写“原文尚未核实”。
- 区分“作者报告”“从结果间接观察”“个人推断”；不得把推断写成论文结论。
- 原文未提供的信息写“原文未报告”，不得补全猜测。
- `status` 表示人的工作进度，`evidence_level` 表示当前笔记依赖的证据深度，两者不得混用。
- AI 辅助导读不能自动把用户的阅读状态改成 `SKIMMED` 或 `DEEP_READ`。
- 一篇论文只有一个主笔记和一个 ID；重读时更新原页面，不创建重复页面。
- PDF、模型、数据集、密钥和大型原始轨迹不提交到 Git。
- 修改论文笔记时，在同一个变更中同步 `papers.md`；元数据改变时同步 `references/library.bib`。
- 保留人工笔记。无法确认内容归属时，只追加有来源的补充，不静默改写原判断。

## 完整分析链

用户要求“完整分析”或论文进入重点复现时，按以下边界执行：

```text
paper note → extract → critic → design → spec → audit
```

- `extract` 只提取实验与证据，不提出方法改进。
- `critic` 分析 claim—机制—证据链，不直接写完整实验方案。
- `design` 把一个明确质疑转成低成本、可控制的验证实验。
- `spec` 把设计翻译成可执行任务，不臆造仓库路径或训练入口。
- `audit` 只检查结构、证据和跨阶段一致性，不代替上游重写。

普通论文不强制运行完整链；只有锚点论文、直接竞争工作或计划复现的论文才值得生成 `artifacts/`。

## 完成前

运行：

```bash
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py validate
```

报告实际更改、当前论文状态、证据缺口以及建议的下一步。除非用户明确要求，不自动发布、分享或将仓库改为公开。
