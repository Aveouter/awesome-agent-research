# A Survey on the Memory Mechanism of Large Language Model-based Agents

## Metadata

- ID：CL-004
- Authors：Zeyu Zhang, Quanyu Dai, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Jieming Zhu, Zhenhua Dong, Ji-Rong Wen
- Year / Venue：2025，ACM Transactions on Information Systems
- Paper：https://doi.org/10.1145/3748302
- Preprint：https://arxiv.org/abs/2404.13501
- Resources：https://github.com/nuster1128/LLM_Agent_Memory_Survey
- Tags：agent memory, memory management, evaluation, lifelong learning, survey
- Status：TO_READ（AI 摘要级导读已建，本人待精读）
- Evidence level：abstract-only
- Read date：

> 下面只依据官方元数据与摘要整理，尚未核对正文、图表和引用覆盖范围。

## 一句话结论

这篇综述把 Agent 记忆从模糊的“存历史”拆成设计、管理、使用和评测问题，是把持续学习路线图落实到可实现模块的合适补充。

## 为什么备选

- CL-001 负责持续学习全景，本篇深入其中最成熟也最容易混淆的记忆模块。
- 摘要明确覆盖记忆的定义、必要性、设计、评测、应用、限制和未来方向。
- 期刊版本可作为稳定引用，但记忆并不等于持续学习；需要检查它是否真的产生跨任务适应，而非仅仅检索历史。

## 明日精读问题

1. 作者采用狭义还是广义的 Agent memory 定义？参数更新是否属于记忆？
2. 记忆的写入、组织、压缩、遗忘和读取分别有哪些设计选择？
3. 现有评测是否区分记住、迁移、泛化和避免灾难性遗忘？
4. 哪些方法只是增加上下文，哪些方法会从多条轨迹抽象可复用经验？

## 读完应产出

画出 `experience → write → manage → retrieve → act → feedback` 闭环，并在每一环标出至少一个可测指标。
