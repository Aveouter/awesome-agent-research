# LifelongAgentBench

## Metadata

- ID：CL-002
- Year：2025
- Paper：https://arxiv.org/abs/2505.11942
- Code：https://github.com/caixd-220529/LifelongAgentBench
- Tags：lifelong learning, benchmark, memory, replay
- Status：TO_READ（AI 导读已建，本人待精读）
- Evidence level：skimmed

## 一句话结论

历史经验回放有时能显著改善小模型，但更多记忆也会带来无关信息、上下文成本和性能下降，因此记忆选择比无限积累更值得研究。

## 初步证据

- 包含数据库、操作系统和知识图谱三个可交互环境。
- 按顺序提供任务，并允许 Agent 利用之前成功轨迹。
- 在部分数据库任务上，经验回放带来明显提升；在另一些模型和环境中，增益很小或随记忆增加而下降。
- 长历史轨迹会产生上下文开销，部分设置可能出现 OOM。

## 精读时重点质疑

1. 论文测试的是“持续学习”，还是主要测试 in-context replay？
2. 成功轨迹是否比失败轨迹更有价值？
3. 任务顺序、技能重合度和检索策略是否影响结论？
4. 能否用一个环境和小模型完成低成本复现？

## 可延伸点

学习何时写入、检索、压缩和遗忘记忆，并依据失败类别而不是单纯语义相似度选择经验。
