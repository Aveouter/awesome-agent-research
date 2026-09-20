# Paper Tracker

更新时间：2026-09-21

> “AI 导读已建”只表示仓库里已有辅助摘要，不代表本人读过。

| ID | 方向 | 年份/会议 | 论文 | 状态 | Evidence | 笔记 | 下一步 |
|---|---|---|---|---|---|---|---|
| MA-001 | 多 Agent | NeurIPS 2025 D&B | Why Do Multi-Agent LLM Systems Fail? | TO_READ | skimmed | [导读](notes/multi-agent/why-mas-fail.md) | 精读分类体系和干预实验 |
| MA-002 | 多 Agent | ACL 2025 | MultiAgentBench | TO_READ | skimmed | [导读](notes/multi-agent/multiagentbench.md) | 核对强单 Agent 基线与成本指标 |
| MA-003 | 多 Agent | IJCAI 2024 Survey | Large Language Model Based Multi-agents: A Survey of Progress and Challenges | TO_READ | abstract-only | [导读](notes/multi-agent/llm-multi-agent-survey.md) | 明日主读：画出系统组成与研究问题地图 |
| MA-004 | 多 Agent | arXiv 2025 | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | TO_READ | skimmed | [导读](notes/multi-agent/collaboration-mechanisms-survey.md) | 已核验机制分类并对齐 MA-003；选择单一动态控制变量和直接竞争工作 |
| CL-001 | 持续学习 | TPAMI 2026 | Lifelong Learning of LLM-based Agents: A Roadmap | TO_READ | skimmed | [导读](notes/continual-learning/lifelong-agent-roadmap.md) | 重点读定义、记忆和评测章节 |
| CL-002 | 持续学习 | arXiv 2025 | LifelongAgentBench | TO_READ | skimmed | [导读](notes/continual-learning/lifelongagentbench.md) | 选一个环境跑最小基线 |
| CL-003 | 持续学习 | ICML 2026 | Little by Little: Continual Learning via Incremental Mixture of Rank-1 Associative Memory Experts | TO_READ | abstract-only | [导读](notes/continual-learning/moram.md) | 核对 rank-1 原子复用、路由消融和容量增长成本 |
| CL-004 | 持续学习 | ACM TOIS 2025 | A Survey on the Memory Mechanism of Large Language Model-based Agents | TO_READ | abstract-only | [导读](notes/continual-learning/agent-memory-survey.md) | 把记忆写入、管理、读取和评测映射到持续学习 |
| MC-001 | 元认知 | AAAI 2025 | Decoupling Metacognition from Cognition | TO_READ | skimmed | [导读](notes/metacognition/dmc.md) | 复核指标与代码可运行性 |
| MC-002 | 元认知 | ICML 2025 | Reflection-Bench | TO_READ | abstract-only | [导读](notes/metacognition/reflection-bench.md) | 明确七项能力如何映射到 Agent |
| MC-003 | 元认知 | Findings of ACL 2026 | From Passive Metric to Active Signal | TO_READ | abstract-only | [导读](notes/metacognition/uncertainty-as-active-signal-survey.md) | 明日主读：提取监控信号到控制动作的设计模式 |
| MC-004 | 元认知 | TACL 2024 | When Can LLMs Actually Correct Their Own Mistakes? | TO_READ | abstract-only | [导读](notes/metacognition/self-correction-critical-survey.md) | 提取自我纠错成立条件与实验检查表 |
| X-001 | 跨方向 | arXiv 2026 | Mendel Gödel Machine | TO_READ | abstract-only | [导读](notes/cross-cutting/mendel-godel-machine.md) | 精读比较进化算子、基线公平性和迁移实验 |

## 本月目标

- 完成 [2026-09-16 综述阅读包](reports/2026-09-16-survey-reading-pack.md) 的三篇主读。
- 复现一个低成本 DMC 或 MAST 子实验。
- 将一个研究想法写成“问题—假设—实验—反证条件”。
