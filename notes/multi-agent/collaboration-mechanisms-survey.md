# Multi-Agent Collaboration Mechanisms: A Survey of LLMs

## Metadata

- ID：MA-004
- Authors：Khanh-Tung Tran, Dung Dao, Minh-Duong Nguyen, Quoc-Viet Pham, Barry O'Sullivan, Hoang D. Nguyen
- Year / Venue：2025，arXiv
- Paper：https://arxiv.org/abs/2501.06322
- Tags：multi-agent, collaboration, coordination, communication, survey
- Status：TO_READ（AI 摘要级导读已建，本人待精读）
- Evidence level：abstract-only
- Read date：

> 下面只依据 arXiv 元数据与摘要整理，尚未核对正文、图表和引用覆盖范围。

## 一句话结论

这篇综述把 LLM 多 Agent 协同拆成参与者、协作类型、组织结构、协作策略和协调协议五个维度，适合把宽泛的“多 Agent 协同”压缩成可比较的设计选择。

## 为什么备选

- 比 MA-003 更聚焦 collaboration mechanism，可作为机制层的第二视角。
- taxonomy 直接暴露可做消融的变量，例如中心化或分布式、合作或竞争、角色式或模型式策略。
- 当前只有 arXiv 版本，阅读时要额外检查引用覆盖、选择标准与分类重叠。

## 明日精读问题

1. 五个维度能否完整描述现有系统，还是混合了系统结构与任务设定？
2. 不同协调协议的收益是否在相同模型、预算和任务难度下比较？
3. 是否讨论通信压缩、错误传播、共识失败和规模扩展成本？
4. 与 MA-003 对照后，哪套 taxonomy 更适合指导实验变量设计？

## 读完应产出

把两个综述的分类法对齐成一张表，并标记哪些维度已有强基线、哪些仍缺可靠评测。
