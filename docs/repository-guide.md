# Awesome Agent Research：仓库使用说明

面向博士研究的 Agent 论文阅读、复现与选题仓库，当前关注三个方向：

- 多 Agent 协同（Multi-Agent Collaboration）
- Agent 持续学习（Continual / Lifelong Learning）
- Agent 元认知（Metacognition / Self-Awareness）

这个仓库不保存论文 PDF，只保存论文链接、自己的理解、实验记录和研究判断。PDF 建议交给 Zotero 管理，避免 Git 仓库膨胀和版权问题。

## 仓库结构

```text
awesome-agent-research/
├── AGENTS.md                  # Agent 工作守则与不变量
├── CONTEXT.md                 # 仓库术语的单一来源
├── WORKFLOW.md                # 人与 Agent 共用的研究流程
├── papers.md                  # 唯一的论文进度总表
├── inbox.md                   # 尚未分类的新论文
├── .agents/skills/            # 仓库级可复用 Agent Skill
├── notes/                     # 一篇论文一个 Markdown 文件
│   ├── continual-learning/
│   ├── multi-agent/
│   └── metacognition/
├── artifacts/                 # 核心论文的分阶段分析产物
├── concepts/                  # 跨论文稳定概念
├── entities/                  # 数据集、benchmark、方法等实体
├── syntheses/                 # 跨论文比较与综合
├── reports/                   # 月报与方向报告
├── research/
│   ├── direction-map.md       # 三个方向的关系与个人判断
│   └── idea-backlog.md        # 可检验的研究想法
├── experiments/README.md      # 复现实验规范与索引
├── logs/weekly/               # 每周研究日志
├── references/library.bib     # 写论文时使用的 BibTeX
└── templates/paper-note.md    # 精读模板
```

## 阅读状态

总表只使用以下状态，避免“收藏等于读过”：

- `TO_READ`：已收录，尚未阅读
- `SKIMMED`：看过摘要、图表和结论
- `DEEP_READ`：通读并完成结构化笔记
- `REPRODUCING`：正在复现
- `REPRODUCED`：完成复现并记录结果
- `DROPPED`：确认暂时不值得继续投入

初始化的六篇笔记是 AI 辅助导读，状态仍为 `TO_READ`，需要本人阅读后才能更新。

## 标准 Workflow

完整流程见 [WORKFLOW.md](../WORKFLOW.md)：

```text
INBOX → TO_READ → SKIMMED → DEEP_READ → REPRODUCING → REPRODUCED
                         ↘ DROPPED
```

GitHub 提供 Paper、Experiment 和 Research Idea 三种 issue 表单。仓库会在 push 和 Pull Request 时自动检查论文 ID、状态、笔记元数据和内部链接；本地可以运行：

```bash
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py validate
```

仓库级 Agent Skill 位于 `.agents/skills/run-agent-paper-workflow/`。Codex 在仓库内启动时可以自动发现，也可以显式使用 `$run-agent-paper-workflow`。

结构与流程参考了 [ACautomata/researcher-service](https://github.com/ACautomata/researcher-service) 及其关联的 [ACautomata/researcher](https://github.com/ACautomata/researcher)，保留了“持久规则 + 场景 Skill + 确定性脚本 + 分阶段质量门”的思想，但简化为适合个人博士研究的单一编排 Skill。

## 推荐工作流

1. 新论文先放进 [inbox.md](../inbox.md)，不要立即分类。
2. 每周从 inbox 选择 2–3 篇，登记到 [papers.md](../papers.md)。
3. 复制 [论文精读模板](../templates/paper-note.md)，完成一篇一页的笔记。
4. 每篇至少写清楚：解决什么问题、核心证据、最大局限、能否复现、能产生什么新问题。
5. 只有可验证的想法才进入 [idea-backlog.md](../research/idea-backlog.md)。
6. 每周写一次研究日志，记录判断发生了什么变化。

## Git 与 Pull Request

所有修改，包括日常笔记、元数据、实验代码和仓库维护，都必须从最新 `main` 建立独立分支，通过 Pull Request 和自动检查后再合并。不得直接推送 `main`。详细命名与提交约定见 [WORKFLOW.md](../WORKFLOW.md#10-git-约定)。

## 当前研究假设

暂定主线为：**可靠、自适应的多 Agent 协同**；以元认知完成能力评估、路由和验证，以持续学习积累长期经验。这个假设会随阅读和实验更新，而不是预设结论。
