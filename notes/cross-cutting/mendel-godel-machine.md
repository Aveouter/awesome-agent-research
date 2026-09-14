# Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution

## Metadata

- ID：X-001
- Authors：Changzhi Liu, Yilun Liu, Sikuan Yan, Volker Tresp, Yunpu Ma
- Institutions：UESTC, LMU Munich, MCML
- Year / Venue：2026，arXiv
- Paper：https://arxiv.org/abs/2608.07645
- Project：https://reallcz.github.io/MGM/
- Code：https://github.com/RealLcz/MGM
- Tags：self-improving agents, coding agents, comparative evolution, Gödel machine, agent adaptation
- Status：TO_READ（仅完成元数据与摘要收录，本人待阅读）
- Evidence level：abstract-only

## 收录理由

MGM 把 Agent 自我改进从“根据单次失败改代码”扩展为利用跨任务、跨谱系的比较证据进行修改，与持续学习、元层诊断和多 Agent 间能力迁移都有直接联系。

## 摘要级导读

作者提出 Mendel Gödel Machine，在常见的单轨迹 clonal mutation 之外，引入 reaction-norm mutation 与 cross-lineage hybridization：前者比较同一 Agent 在多个任务上的轨迹，后者利用不同谱系 Agent 在相同任务上的表现差异来指导自我修改。论文报告了理论分析、受控模拟，以及 SWE-bench 与 Polyglot 上的编码 Agent 实验。

以上仅来自论文摘要和官方项目元数据，具体实验协议、计算预算、基线实现和安全边界尚未核对原文。

## 精读时重点质疑

1. MGM 与 Darwin Gödel Machine、Huxley Gödel Machine 的比较是否严格控制模型、任务评估次数、Token 和搜索预算？
2. 三种修改算子的增益能否通过消融稳定复现，还是高度依赖归档规模、采样策略或特定基础模型？
3. 跨任务和跨模型迁移是否足以排除 benchmark-specific scaffold hacking？
4. “比较证据改善故障定位”的理论模型与真实代码 Agent 的复杂修改之间存在多大差距？
5. 递归修改自身代码时，如何防止安全约束、评测协议和验证逻辑被共同优化掉？

## 下一步

精读方法、预算控制和迁移实验，并绘制 MGM 与 DGM、HGM 的状态、归档及修改算子对照表。
