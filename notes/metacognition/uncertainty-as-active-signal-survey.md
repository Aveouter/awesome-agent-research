# From Passive Metric to Active Signal: The Evolving Role of Uncertainty Quantification in Large Language Models

## Metadata

- ID：MC-003
- Authors：Jiaxin Zhang, Wendi Cui, Zhuohang Li, Lifu Huang, Bradley A. Malin, Caiming Xiong, Chien-Sheng Wu
- Year / Venue：2026，Findings of ACL
- Paper：https://aclanthology.org/2026.findings-acl.2064/
- Tags：uncertainty, confidence, metacognition, tool use, self-correction, survey
- Status：TO_READ（AI 摘要级导读已建，本人待精读）
- Evidence level：abstract-only
- Read date：

> 下面只依据 ACL Anthology 元数据与摘要整理，尚未核对正文、图表和引用覆盖范围。

## 一句话结论

这篇综述最值得看的不是如何“测置信度”，而是如何把不确定性变成 Agent 是否继续推理、调用工具、检索信息或自我纠错的控制信号。

## 为什么主读

- 直接连接元认知的 monitoring 与 control，而不是停留在自信分数的相关性分析。
- 摘要覆盖高级推理、自主 Agent 和强化学习三个前沿，能观察同一信号如何驱动不同决策。
- 论文给出设计模式，适合继续发展成低成本动态路由或协同控制研究。

## 明日精读问题

1. 哪些不确定性估计能在线使用，额外调用和延迟分别是多少？
2. 信号是否真正预测失败，还是只与答案风格或模型规模相关？
3. 如何把连续置信度转成离散动作：回答、重试、检索、工具调用、求助或拒答？
4. 控制策略如何避免过度谨慎、循环反思和预算失控？

## 读完应产出

整理一个 `monitoring signal → threshold/policy → control action → utility/cost` 表，并挑一个可与多 Agent 路由结合的实验。
