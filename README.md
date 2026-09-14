# Awesome Agent Research

A curated paper list and evidence-backed research workspace for reliable, adaptive AI agents.

本仓库持续整理三个相互关联的方向：**多 Agent 协同**、**Agent 持续学习**与 **Agent 元认知**。当前研究主线是：利用元认知进行能力评估、路由和验证，通过持续学习积累经验，从而构建可靠、自适应的多 Agent 系统。

[论文总表](papers.md) · [阅读工作流](WORKFLOW.md) · [研究方向图](research/direction-map.md) · [仓库使用说明](docs/repository-guide.md) · [BibTeX](references/library.bib)

> [!NOTE]
> 论文状态表示本人阅读进度，Evidence 表示笔记实际核对材料的深度；AI 辅助导读不等于本人已经读过。

## 📣 Updates

- **2026-09** — 建立首批 6 篇核心论文导读，覆盖多 Agent 失败分析、协同评测、持续学习与元认知评测。
- **2026-09** — 加入结构化阅读、审稿式批判、实验设计、复现与质量审计工作流。

## 📚 Table of Contents

- [Multi-Agent Collaboration](#-multi-agent-collaboration)
  - [Reliability and Failure Analysis](#reliability-and-failure-analysis)
  - [Evaluation and Coordination](#evaluation-and-coordination)
- [Continual and Lifelong Learning](#-continual-and-lifelong-learning)
  - [Roadmaps and Surveys](#roadmaps-and-surveys)
  - [Benchmarks and Memory](#benchmarks-and-memory)
- [Agent Metacognition](#-agent-metacognition)
  - [Calibration and Self-Knowledge](#calibration-and-self-knowledge)
  - [Reflection and Epistemic Agency](#reflection-and-epistemic-agency)
- [Reading Status](#-reading-status)
- [Add a Paper](#-add-a-paper)

## 🤝 Multi-Agent Collaboration

关注多 Agent 系统的失败机理、通信结构、任务分配、验证机制，以及性能与协作成本之间的权衡。

### Reliability and Failure Analysis

- **NeurIPS Datasets and Benchmarks 2025** — [Why Do Multi-Agent LLM Systems Fail?](https://arxiv.org/abs/2503.13657), Mert Cemri et al.<br>
  从 7 个多 Agent 系统的执行轨迹中归纳失败模式，适合作为失败感知协同控制的起点。<br>
  [Code](https://github.com/multi-agent-systems-failure-taxonomy/MAST) · [Reading note](notes/multi-agent/why-mas-fail.md) · `MA-001` · `TO_READ / skimmed`

### Evaluation and Coordination

- **ACL 2025** — [MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents](https://aclanthology.org/2025.acl-long.421/), Kunlun Zhu et al.<br>
  在六类环境中比较协作策略与通信拓扑，并同时衡量任务表现和协作过程。<br>
  [Code](https://github.com/ulab-uiuc/MARBLE) · [Reading note](notes/multi-agent/multiagentbench.md) · `MA-002` · `TO_READ / skimmed`

## 🧠 Continual and Lifelong Learning

关注 Agent 如何写入、选择、压缩和遗忘经验，以及如何同时保持可塑性、稳定性和长期效率。

### Roadmaps and Surveys

- **IEEE TPAMI 2026** — [Lifelong Learning of Large Language Model Based Agents: A Roadmap](https://arxiv.org/abs/2501.07278), Junhao Zheng et al.<br>
  从感知、记忆和行动组织持续学习 Agent 文献，突出稳定性—可塑性矛盾。<br>
  [Resources](https://github.com/qianlima-lab/awesome-lifelong-llm-agent) · [Reading note](notes/continual-learning/lifelong-agent-roadmap.md) · `CL-001` · `TO_READ / skimmed`

### Benchmarks and Memory

- **arXiv 2025** — [LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners](https://arxiv.org/abs/2505.11942), Junhao Zheng et al.<br>
  评估交互式环境中的顺序任务与经验回放，揭示更多记忆不一定带来更好表现。<br>
  [Code](https://github.com/caixd-220529/LifelongAgentBench) · [Reading note](notes/continual-learning/lifelongagentbench.md) · `CL-002` · `TO_READ / skimmed`

## 🪞 Agent Metacognition

关注 Agent 是否知道自己会什么、何时可能失败，以及如何据此求助、路由、验证和修正行为。

### Calibration and Self-Knowledge

- **AAAI 2025** — [Decoupling Metacognition from Cognition: A Framework for Quantifying Metacognitive Ability in LLMs](https://ojs.aaai.org/index.php/AAAI/article/view/34723), Guoqing Wang et al.<br>
  区分任务能力与判断自身答案是否可靠的能力，为拒答、求助和验证路由提供量化基础。<br>
  [Code](https://github.com/Angelo3357/DMC) · [Reading note](notes/metacognition/dmc.md) · `MC-001` · `TO_READ / skimmed`

### Reflection and Epistemic Agency

- **ICML 2025** — [Reflection-Bench: Evaluating Epistemic Agency in Large Language Models](https://proceedings.mlr.press/v267/li25cu.html), Lingyu Li et al.<br>
  将 epistemic agency 拆分为七类能力，用于定位预测、记忆、信念更新和元反思等薄弱环节。<br>
  [Code](https://github.com/AI45Lab/ReflectionBench) · [Reading note](notes/metacognition/reflection-bench.md) · `MC-002` · `TO_READ / abstract-only`

## 🏷 Reading Status

| Status | Meaning |
|---|---|
| `TO_READ` | 已收录，本人尚未阅读 |
| `SKIMMED` | 本人已速读摘要、图表和结论 |
| `DEEP_READ` | 本人已通读并完成结构化笔记 |
| `REPRODUCING` | 正在验证或复现关键结果 |
| `REPRODUCED` | 已得到并记录可解释的复现结果 |
| `DROPPED` | 当前证据不足以继续投入 |

Evidence 由浅到深为：`abstract-only → skimmed → full-paper → reproduced`。完整进度与下一步见 [Paper Tracker](papers.md)。

## ➕ Add a Paper

新发现的论文先加入 [inbox](inbox.md)，写明它可能改变的研究判断；也可以提交 [Paper intake issue](https://github.com/Aveouter/awesome-agent-research/issues/new?template=paper.yml)。所有修改都通过 Pull Request 完成，具体维护规范见 [Repository Guide](docs/repository-guide.md)。
