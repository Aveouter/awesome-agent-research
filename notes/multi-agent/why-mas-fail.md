# Why Do Multi-Agent LLM Systems Fail?

## Metadata

- ID：MA-001
- Year / Venue：2025，NeurIPS Datasets and Benchmarks
- Paper：https://arxiv.org/abs/2503.13657
- Code：https://github.com/multi-agent-systems-failure-taxonomy/MAST
- Tags：multi-agent, failure taxonomy, evaluation, reliability
- Status：TO_READ（AI 导读已建，本人待精读）

## 一句话结论

多 Agent 失败并不只是基础模型不够强，大量失败来自工作流、Agent 间信息传递和结果验证；这使“失败感知的协同控制”成为比简单增加 Agent 更具体的研究问题。

## 初步证据

- 数据包含 7 个多 Agent 系统的 1642 条执行轨迹。
- 作者总结出 14 种失败模式，分为系统设计、Agent 间失配和任务验证三类。
- 报告的系统失败率约为 41%–86.7%。
- 人工标注一致性较高，但大规模数据主要使用 LLM-as-a-Judge 扩展标注。
- 简单工作流干预能提高成功率，但没有消除所有失败。

## 精读时重点质疑

1. 失败标签描述的是表面现象还是可干预的根因？
2. LLM 标注器是否会系统性偏向某些失败类别？
3. 干预实验是否控制了 Token、调用次数和随机性？
4. 分类体系能否泛化到新的 Agent 框架和真实业务？

## 可延伸点

用在线失败诊断器动态决定继续协作、请求澄清、增加验证者或终止，并同时优化成功率与调用成本。
