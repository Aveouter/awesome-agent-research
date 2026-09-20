# Why Do Multi-Agent LLM Systems Fail?

## Metadata

- ID：MA-001
- Year / Venue：2025，NeurIPS Datasets and Benchmarks
- Paper：https://arxiv.org/abs/2503.13657
- Code：https://github.com/multi-agent-systems-failure-taxonomy/MAST
- Tags：multi-agent, failure taxonomy, evaluation, reliability
- Status：DEEP_READ（用户已确认阅读完成）
- Read date：具体日期未提供；2026-09-21 确认已读完
- Evidence level：skimmed

- AI evidence checked：2026-09-21；关键正文及所列图表/附录，非逐项全文审阅。

## 原有导读（保留；本次核验与更正见后文）

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

## 2026-09-21：原文核验与研究判断

### 1. 来源、问题与方法

正文依据 [arXiv v3](https://arxiv.org/html/2503.13657v3)，会议信息另由 [NeurIPS 官方页面](https://papers.nips.cc/paper_files/paper/2025/hash/b1041e52d3be19f0a9bc491657488e4a-Abstract-Datasets_and_Benchmarks_Track.html)核实。以下页码指 v3 PDF，不能直接套用其他版本。

作者用执行轨迹归纳失败类别，再验证标注一致性、扩展自动标注、开展工作流干预。贡献是诊断框架与数据资源；不是已验证的在线路由算法。既有导读的总体方向保留，但其“失败原因”应理解为可观察标签，不能自动解释成因果根因。

### 2. 可追溯证据

| 作者报告 | 原文位置 | 使用边界 |
|---|---|---|
| 1642 条轨迹、7 个 MAS；14 类模式归入三大类 | 表 1，p.3；§4，p.7 | 框架、模型和任务并不全部相同 |
| few-shot o1 标注 accuracy 0.94、F1 0.80、κ 0.77 | 表 2，p.6 | 自动标注仍有漏检；不能只报 accuracy |
| AG2/GSM-Plus/GPT-4：baseline 84.75±1.94、改 prompt 89.75±1.44、新拓扑 85.50±1.18 | 表 5，p.27；H.1，p.26 | 200 题、6 次重复；新拓扑比较的 p=0.4，不显著 |
| ChatDev/ProgramDev-v0：25.0→34.4→40.6（accuracy，%） | 表 5、H.2，p.27 | 32 题；不是表 1 的 ProgramDev-v2 |

旧导读的 41%–86.7% 为作者跨系统配置的失败率描述（p.2、图 5），不构成同一任务、等预算的系统排行榜。表 5 的 ChatDev 改善应表述为 9.4 / 15.6 个百分点，不能混成相对百分比。

### 3. 批判性判断（个人推断）

- 高标注一致性回答“能否一致命名”，没有单独回答“修改这个因素能否修复任务”。应把诊断效度与干预收益分开。
- 改 prompt 与新拓扑都可能改变推理长度、工具使用、验证次数。相同模型不等于相同预算，表 5 不足以证明组织结构在等预算下优于额外推理。
- 完整失败轨迹带有结局信息；直接拿其标签训练执行前求助决策，会造成可用信息范围错配。在线用途必须限制为决策时可见的前缀。
- H.3 对拓扑变化的概括，不能覆盖 H.1 中 GPT-4 的不显著结果；应逐模型、逐指标解读。

### 4. 复现可行性与证据缺口

已核对[官方代码仓库](https://github.com/multi-agent-systems-failure-taxonomy/MAST)入口，未执行 notebook、下载完整数据或验证环境。当前 README 的数据命名与论文 MAST-Data 名称不同，复现前须固定数据 revision、题目 ID、模型快照与系统 commit。不能把仓库存在写成可运行性通过。

建议从 AG2 数学子实验开始，先核对 prompt 干预在预算匹配后是否仍有收益。原文表 5 未报告逐配置 Token/费用；附录 K 的标注器费用不是运行干预的总费用。当前 API 价格、可用模型与本地算力尚未核实，因此预计费用和时间待预跑测量。实际结果：未运行。

### 5. 与个人研究的关系及下一步

个人推断：为 IDEA-001 提供失败观测语言，但还缺“失败可预测”到“协作能救回”的证据；为 IDEA-002 提供候选标签，尚不能证明标签具有迁移价值。暂不修改方向地图的既有判断。

本轮按核心论文推进至 [extract](../../artifacts/MA-001/extract.md) → [critic](../../artifacts/MA-001/critic.md) → [design](../../artifacts/MA-001/design.md)，并做 [audit](../../artifacts/MA-001/audit.md)。尚未确定实施，按 WORKFLOW §6 不生成 spec，也不建立复现状态。

### 阅读进度确认

2026-09-21，用户确认已阅读完成，本人工作进度更新为 DEEP_READ。Evidence level 仍为 skimmed，表示当前笔记已留存证据的核验范围；未据阅读状态自动升级证据或复现状态。
