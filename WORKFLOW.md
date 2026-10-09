# Paper Reading Workflow

个人 Agent 论文阅读与知识记录系统，服务于收藏、理解、检索和长期知识积累。

```text
CAPTURE → REGISTER → READ & NOTE ↔ CONNECT ↔ REVIEW & RETRIEVE
```

阶段可跳过、重复和按需执行；实验不是阅读完成条件。

## Capture：收藏

只在 inbox.md 添加标题、原始链接与可选理由，不分配 ID、不写总表、不建主笔记。Paper intake issue 是远程收藏入口，整理到 inbox 后再决定正式收录。无需评分、研究价值或固定周计划。

## Register：正式收录

先检查 papers.md、notes/ 和 references/library.bib 的标题、DOI/arXiv ID 和链接。同论文不同版本沿用原 ID 和笔记。确认无重复才分配下一个未使用 ID（MA/CL/MC/X-###），复制 templates/paper-note.md，登记总表与引用。默认 TO_READ / abstract-only，实际核验更多材料再记录 Evidence。inbox 标注登记 ID，保留来源；ID 不复用。

## Read & Note：阅读与记录

速读可只填 Metadata、TL;DR、Takeaways；精读补 Problem & Contribution、Method、Evidence。重要数字尽量记录数据集、指标、原文版本、页码/图表。分次阅读可逐步补充，无需实验计划、可证伪假设或选题。

区分作者报告、直接证据、间接观察和个人推断；未核实写“原文尚未核实”，缺失写“原文未报告”。AI 辅助导读只更新笔记和核验范围；只有用户明确报告或授权人工进度变更，才同步总表与笔记 Status 镜像。

## 阅读状态与证据

papers.md 是阅读状态唯一权威来源；笔记 Status 是校验镜像，README 只列稳定元数据与链接。

| Status | 含义 | 可迁移到 |
|---|---|---|
| TO_READ | 已正式收录，尚未人工阅读 | SKIMMED、DEEP_READ、ARCHIVED |
| SKIMMED | 已速读，理解主要问题和贡献 | DEEP_READ、ARCHIVED |
| DEEP_READ | 已精读，形成可回顾的结构化笔记 | ARCHIVED |
| ARCHIVED | 暂缓或不再优先阅读，保留记录 | TO_READ、SKIMMED、DEEP_READ |

归档/恢复需理由，迁移记录保留日期、旧值与原进度。恢复可回到已确认进度，重读不回退 DEEP_READ。重读补充原笔记的 Reading History，不建新 ID。

Evidence 独立描述材料核验范围：abstract-only（摘要/元数据）、skimmed（全文关键章节/图表）、full-paper（正文与关键附录，主要数字可定位）。DEEP_READ / skimmed 可以共存：人的完成进度和记录的核验范围不同，不能自动升级 Evidence。

```bash
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py transition MA-001 ARCHIVED --reason "已精读，暂缓后续阅读"
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py transition MA-001 DEEP_READ --reason "恢复已确认精读进度"
```

### 旧状态兼容与迁移

校验识别历史 DROPPED、REPRODUCING、REPRODUCED 及 Evidence reproduced，并输出兼容警告；这些不属于新状态机，不能作为 transition 目标，仅供逐项处理历史资料。

- DROPPED → ARCHIVED：用户确认后同步总表和笔记，追加日期、旧值与理由。
- REPRODUCING / REPRODUCED：实验进度保留在历史记录或独立实验页；人工状态依据用户确认选择，未知则保留旧值并提示，不猜测 DEEP_READ。
- reproduced Evidence：保留复现证据引用，核对材料范围后明确改为 full-paper 等，不静默转换。

当前 13 篇无需旧状态转换；MA-001 至 MA-004 的 DEEP_READ 与 skimmed Evidence 保留。

## Connect：知识连接

按需在 Connections 链接相关论文、比较方法与概念。跨论文对齐问题、方法、数据集、指标时使用 syntheses/；concepts/、entities/ 可选。

## Review & Retrieve：回顾与检索

通过总表、标签和主笔记检索，纠错与重读更新原页，追加理解变化及证据位置。阅读日志、周报和月报可选，无固定频率。

## 可选历史研究资料

artifacts/、research/、experiments/ 及研究模板保留为历史或明确请求的扩展，不是阅读校验依赖。事实提取与批判性理解优先整合主笔记；完整阅读分析也不默认生成五阶段文件。明确要求分阶段研究或复现时才使用 extract → critic → design → spec → audit，分别负责事实、质疑、验证设计、执行任务与一致性审计；不臆造训练入口，实验进度单独记录。

## Git 约定

本次重构从最新 main 建独立分支，通过 PR 与自动检查后合并。以下轻量策略仅在本次规则合并后启用：普通笔记、总表与对应引用可按阅读批次提交，共用分支和 PR，无需一篇论文一个 PR。公共规则、脚本、模板和目录迁移仍单独维护分支与 PR。不得直接推送 main。默认分支 codex/，提交用 notes:、refactor: 或 chore:。

提交前运行 workflow validate、单元测试与文件边界检查，保留 hooks 和 CI。PDF、Zotero、全文提取、密钥和大型二进制只留本地，D:\paper 与 Git 隔离。详见 [文献文件与 Git 边界](docs/storage-boundaries.md)。
