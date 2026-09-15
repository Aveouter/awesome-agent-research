# When Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-Correction of LLMs

## Metadata

- ID：MC-004
- Authors：Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, Rui Zhang
- Year / Venue：2024，Transactions of the Association for Computational Linguistics
- Paper：https://aclanthology.org/2024.tacl-1.78/
- Tags：self-correction, self-evaluation, external feedback, metacognition, critical survey
- Status：TO_READ（AI 摘要级导读已建，本人待精读）
- Evidence level：abstract-only
- Read date：

> 下面只依据 ACL Anthology 元数据与摘要整理，尚未核对正文、图表和引用覆盖范围。

## 一句话结论

这篇批判性综述提醒我们：没有可靠外部反馈时，提示式 LLM 自我纠错通常缺少普遍有效的证据；元认知系统必须认真区分“自我判断”和“可验证反馈”。

## 为什么备选

- 它不是继续罗列反思方法，而是追问这些方法在什么条件下真的成立。
- 作者按反馈来源和研究问题重组文献，并提供实验设计检查表。
- 与 MC-003 互补：前者讲信号如何控制，本文检查控制所依赖的反馈是否可信。

## 明日精读问题

1. 作者如何定义 intrinsic self-correction，哪些常见设置其实使用了外部信息？
2. 哪些任务天然可验证，因此不能代表开放环境中的 Agent？
3. 性能提升是否来自更多采样或更大计算预算，而非真正的自我纠错？
4. 论文的实验检查表能否迁移到反思 Agent 和多 Agent critic/verifier？

## 读完应产出

提炼一份“自我纠错实验最低证据标准”，以后评审 reflection、critic 和 verifier 方法时复用。
