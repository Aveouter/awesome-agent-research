# Little by Little: Continual Learning via Incremental Mixture of Rank-1 Associative Memory Experts

## Metadata

- ID：CL-003
- Authors：Haodong Lu, Chongyang Zhao, Minhui Xue, Lina Yao, Kristen Moore, Dong Gong
- Year / Venue：2026，ICML
- Paper：https://arxiv.org/abs/2506.21035
- OpenReview：https://openreview.net/forum?id=P247k4ELcn
- Project：https://artificer-ai-lab.github.io/MoRAM/
- Code：https://github.com/Artificer-AI-Lab/MoRAM
- Tags：continual learning, associative memory, rank-1 adapter, mixture of experts, MoRAM
- Status：TO_READ（仅完成元数据与摘要收录，本人待阅读）
- Evidence level：abstract-only

## 收录理由

MoRAM 直接对应持续学习中的稳定性—可塑性问题，并把 LoRA 的低秩更新解释成可检索的原子记忆；它可能为 Agent 的参数记忆扩展、选择性激活和遗忘控制提供一个可实验的实现路径。

## 摘要级导读

作者报告，现有 MoE-LoRA 持续学习方法会因专家粒度较粗而出现冗余、干扰和路由歧义。MoRAM 将每个 rank-1 adapter 视为 key–value 形式的细粒度记忆单元，通过基于内在 key 的自激活进行内容寻址，并在新任务到来时增量增加记忆原子、冻结旧原子。论文在 CLIP 与 LLM 持续学习任务上评估该方法。

以上仅来自论文摘要和官方项目元数据，实验数值、对照公平性及机制解释尚未核对原文。

## 精读时重点质疑

1. 在参数量、激活 rank 和训练预算一致时，性能提升究竟来自 rank-1 粒度、自激活路由还是单纯容量增长？
2. 随任务数量增加，记忆原子的存储、检索和推理成本如何扩展？
3. 冻结旧原子能否真正避免遗忘，还是把冲突转移到新原子的路由与组合上？
4. X-TAIL 与 TRACE 的任务顺序、数据访问假设和指标是否符合真实 Agent 的持续学习场景？

## 下一步

通读方法与实验章节，优先核对 router ablation、容量控制、长任务序列结果，以及旧知识复用是否有独立证据。
