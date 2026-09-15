# Awesome Agent Research

A curated paper list and evidence-backed research workspace for reliable, adaptive AI agents.

本仓库持续整理三个相互关联的方向：**多 Agent 协同**、**Agent 持续学习**与 **Agent 元认知**。当前研究主线是：利用元认知进行能力评估、路由和验证，通过持续学习积累经验，从而构建可靠、自适应的多 Agent 系统。

[论文总表](papers.md) · [明日综述阅读包](reports/2026-09-16-survey-reading-pack.md) · [阅读工作流](WORKFLOW.md) · [研究方向图](research/direction-map.md) · [仓库使用说明](docs/repository-guide.md) · [BibTeX](references/library.bib)

> [!NOTE]
> 论文状态表示本人阅读进度，Evidence 表示笔记实际核对材料的深度；AI 辅助导读不等于本人已经读过。

## 📣 Updates

- **2026-09** — 收录 ICML 2026 的 MoRAM 与跨方向自改进 Agent 工作 Mendel Gödel Machine。
- **2026-09** — 整理三个方向的综述阅读包：每个方向 1 篇主读、1 篇备选。
- **2026-09** — 建立首批 6 篇核心论文导读，覆盖多 Agent 失败分析、协同评测、持续学习与元认知评测。
- **2026-09** — 加入结构化阅读、审稿式批判、实验设计、复现与质量审计工作流。

## 📚 Table of Contents

- [Multi-Agent Collaboration](#-multi-agent-collaboration)
  - [Surveys and Taxonomies](#surveys-and-taxonomies)
  - [Reliability and Failure Analysis](#reliability-and-failure-analysis)
  - [Evaluation and Coordination](#evaluation-and-coordination)
- [Continual and Lifelong Learning](#-continual-and-lifelong-learning)
  - [Roadmaps and Surveys](#roadmaps-and-surveys)
  - [Methods and Memory](#methods-and-memory)
  - [Benchmarks](#benchmarks)
- [Agent Metacognition](#-agent-metacognition)
  - [Surveys and Control](#surveys-and-control)
  - [Calibration and Self-Knowledge](#calibration-and-self-knowledge)
  - [Reflection and Epistemic Agency](#reflection-and-epistemic-agency)
- [Cross-Cutting Agent Self-Improvement](#-cross-cutting-agent-self-improvement)
  - [Recursive Self-Improving Agents](#recursive-self-improving-agents)
- [Reading Status](#-reading-status)
- [Add a Paper](#-add-a-paper)

## 🤝 Multi-Agent Collaboration

关注多 Agent 系统的失败机理、通信结构、任务分配、验证机制，以及性能与协作成本之间的权衡。

### Surveys and Taxonomies

- **IJCAI 2024 Survey Track** — [Large Language Model Based Multi-agents: A Survey of Progress and Challenges](https://www.ijcai.org/proceedings/2024/890), Taicheng Guo et al.<br>
  从应用环境、Agent profile、通信、能力发展与评测资源建立全局地图，适合作为多 Agent 方向的第一篇综述。<br>
  [Resources](https://github.com/taichengguo/LLM_MultiAgents_Survey_Papers) · [Reading note](notes/multi-agent/llm-multi-agent-survey.md) · `MA-003` · `TO_READ / abstract-only`

- **arXiv 2025** — [Multi-Agent Collaboration Mechanisms: A Survey of LLMs](https://arxiv.org/abs/2501.06322), Khanh-Tung Tran et al.<br>
  围绕参与者、协作类型、结构、策略与协调协议细分协同机制，作为主综述的机制层补充。<br>
  [Reading note](notes/multi-agent/collaboration-mechanisms-survey.md) · `MA-004` · `TO_READ / abstract-only`

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

- **ACM TOIS 2025** — [A Survey on the Memory Mechanism of Large Language Model-based Agents](https://doi.org/10.1145/3748302), Zeyu Zhang et al.<br>
  系统整理 Agent 记忆的设计、管理与评测，将持续学习中最可落地的模块单独展开。<br>
  [Preprint](https://arxiv.org/abs/2404.13501) · [Resources](https://github.com/nuster1128/LLM_Agent_Memory_Survey) · [Reading note](notes/continual-learning/agent-memory-survey.md) · `CL-004` · `TO_READ / abstract-only`

### Methods and Memory

- **ICML 2026** — [Little by Little: Continual Learning via Incremental Mixture of Rank-1 Associative Memory Experts](https://arxiv.org/abs/2506.21035), Haodong Lu et al.<br>
  MoRAM 将持续学习重写为可复用 rank-1 记忆原子的增量扩展，并使用基于内在 key 的自激活替代显式路由器。<br>
  [Project](https://artificer-ai-lab.github.io/MoRAM/) · [Code](https://github.com/Artificer-AI-Lab/MoRAM) · [Reading note](notes/continual-learning/moram.md) · `CL-003` · `TO_READ / abstract-only`

### Benchmarks

- **arXiv 2025** — [LifelongAgentBench: Evaluating LLM Agents as Lifelong Learners](https://arxiv.org/abs/2505.11942), Junhao Zheng et al.<br>
  评估交互式环境中的顺序任务与经验回放，揭示更多记忆不一定带来更好表现。<br>
  [Code](https://github.com/caixd-220529/LifelongAgentBench) · [Reading note](notes/continual-learning/lifelongagentbench.md) · `CL-002` · `TO_READ / skimmed`

## 🪞 Agent Metacognition

关注 Agent 是否知道自己会什么、何时可能失败，以及如何据此求助、路由、验证和修正行为。

### Surveys and Control

- **Findings of ACL 2026** — [From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantification in Large Language Models](https://aclanthology.org/2026.findings-acl.2064/), Jiaxin Zhang et al.<br>
  把不确定性从离线指标推进为推理预算、工具调用、信息检索和自我纠错的在线控制信号。<br>
  [Reading note](notes/metacognition/uncertainty-as-active-signal-survey.md) · `MC-003` · `TO_READ / abstract-only`

- **TACL 2024** — [When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs](https://aclanthology.org/2024.tacl-1.78/), Ryo Kamoi et al.<br>
  批判性梳理自我纠错何时成立，提醒区分模型自身反馈、外部反馈与训练带来的收益。<br>
  [Reading note](notes/metacognition/self-correction-critical-survey.md) · `MC-004` · `TO_READ / abstract-only`

### Calibration and Self-Knowledge

- **AAAI 2025** — [Decoupling Metacognition from Cognition: A Framework for Quantifying Metacognitive Ability in LLMs](https://ojs.aaai.org/index.php/AAAI/article/view/34723), Guoqing Wang et al.<br>
  区分任务能力与判断自身答案是否可靠的能力，为拒答、求助和验证路由提供量化基础。<br>
  [Code](https://github.com/Angelo3357/DMC) · [Reading note](notes/metacognition/dmc.md) · `MC-001` · `TO_READ / skimmed`

### Reflection and Epistemic Agency

- **ICML 2025** — [Reflection-Bench: Evaluating Epistemic Agency in Large Language Models](https://proceedings.mlr.press/v267/li25cu.html), Lingyu Li et al.<br>
  将 epistemic agency 拆分为七类能力，用于定位预测、记忆、信念更新和元反思等薄弱环节。<br>
  [Code](https://github.com/AI45Lab/ReflectionBench) · [Reading note](notes/metacognition/reflection-bench.md) · `MC-002` · `TO_READ / abstract-only`

## 🧬 Cross-Cutting Agent Self-Improvement

收录连接持续适应、元层控制与 Agent 工作流演化的跨方向研究。

### Recursive Self-Improving Agents

- **arXiv 2026** — [Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution](https://arxiv.org/abs/2608.07645), Changzhi Liu et al.<br>
  MGM 利用同一 Agent 跨任务以及不同谱系 Agent 之间的比较证据，指导编码 Agent 递归修改自身工作流。<br>
  [Project](https://reallcz.github.io/MGM/) · [Code](https://github.com/RealLcz/MGM) · [Reading note](notes/cross-cutting/mendel-godel-machine.md) · `X-001` · `TO_READ / abstract-only`

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
