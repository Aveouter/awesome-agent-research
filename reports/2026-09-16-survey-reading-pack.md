# 2026-09-16 三方向综述阅读包

目标不是一天读完六篇，而是用三篇主读建立地图，再用三篇备选补关键机制。所有新增导读目前都是 `abstract-only`；只有本人完成阅读后才更新 Status。

## 明日主读（约 2.5–3 小时）

| 顺序 | 方向 | 论文 | 建议时间 | 必须带走的问题 |
|---|---|---|---:|---|
| 1 | 多 Agent 协同 | [MA-003：LLM Multi-agents Survey](../notes/multi-agent/llm-multi-agent-survey.md) | 45 分钟 | 多 Agent 的基本组成、任务类型和评测缺口是什么？ |
| 2 | Agent 持续学习 | [CL-001：Lifelong Agent Roadmap](../notes/continual-learning/lifelong-agent-roadmap.md) | 60 分钟 | 感知、记忆、行动如何共同实现适应，而不仅是存历史？ |
| 3 | Agent 元认知 | [MC-003：Uncertainty as Active Signal](../notes/metacognition/uncertainty-as-active-signal-survey.md) | 45 分钟 | 如何把“我可能不会”转成检索、工具、求助、重试或停止？ |

每篇只做四步：先看 abstract 和总览图；再读 taxonomy/definition；然后看 challenges；最后写 3 句自己的判断。遇到细节先标页码，不在第一轮陷入引用链。

## 备选补读（每篇 20–30 分钟）

| 方向 | 论文 | 补什么 |
|---|---|---|
| 多 Agent 协同 | [MA-004：Collaboration Mechanisms Survey](../notes/multi-agent/collaboration-mechanisms-survey.md) | 用五维协作 taxonomy 补主综述的机制粒度 |
| Agent 持续学习 | [CL-004：Agent Memory Survey](../notes/continual-learning/agent-memory-survey.md) | 深挖记忆写入、管理、读取与评测，警惕“记忆 = 持续学习” |
| Agent 元认知 | [MC-004：Self-Correction Critical Survey](../notes/metacognition/self-correction-critical-survey.md) | 了解自我纠错的负面结果、可靠反馈条件与实验陷阱 |

## 读完后的最小产出

在每篇 note 末尾补四项即可：

1. 一句话重新定义该方向。
2. 一个你认为最关键、但现有工作没测好的变量。
3. 一个可能成为博士课题的可证伪假设。
4. 是否值得深读：`继续 / 暂缓 / 放弃`，以及理由。

## 三个方向的连接问题

最后用 15 分钟回答：能否让元认知模块估计单 Agent 的失败风险，再决定是否调用多 Agent 协同，并把成功或失败轨迹写入持续学习记忆？如果能，最小闭环需要哪些状态、动作、反馈和成本指标？
