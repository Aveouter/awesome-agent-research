# MultiAgentBench

## Metadata

- ID：MA-002
- Year / Venue：2025，ACL
- Paper：https://aclanthology.org/2025.acl-long.421/
- Code：https://github.com/ulab-uiuc/MARBLE
- Tags：multi-agent, benchmark, topology, coordination
- Status：TO_READ（AI 导读已建，本人待精读）
- Evidence level：skimmed

- AI evidence checked：2026-09-21；关键正文及所列图表/附录，非逐项全文审阅。

## 原有导读（保留；本次核验与更正见后文）

## 一句话结论

协作分数高并不保证任务成功，增加 Agent 数量也不保证变好；基础模型能力、任务匹配和协作成本必须一起评估。

## 初步证据

- 覆盖研究、Minecraft、数据库、编码、谈判和狼人杀六类环境。
- 比较星形、树形、网状和链式通信结构，以及不同规划策略。
- 部分场景中 Agent 从 1 个增加到 3 个有所帮助，继续增加反而因协调复杂度下降。
- 论文同时测任务表现与协作过程，但部分过程指标依赖 LLM-as-a-Judge。

## 精读时重点质疑

1. 是否与同等推理预算的单 Agent 和 best-of-N 公平比较？
2. “协作能力”指标是否真正预测任务成功？
3. 结论是任务特定的，还是跨场景稳定？
4. 模型能力、拓扑和 Agent 数量之间是否有充分消融？

## 可延伸点

根据任务难度和 Agent 能力画像，动态决定单 Agent、多 Agent、角色和拓扑，而不是使用固定工作流。

## 2026-09-21：原文核验与研究判断

### 1. 来源、问题与方法

核对 [ACL 正式版 PDF](https://aclanthology.org/2025.acl-long.421.pdf) 的 §§3–5、§8 及附录 A.3/A.6/A.7；以下使用会议印刷页码。元数据与[官方 BibTeX](https://aclanthology.org/2025.acl-long.421.bib)一致，本次不改文献身份。

作者构建 MultiAgentBench，并用 MARBLE 组织环境、Agent、通信、记忆和评价。其价值在于把任务表现与协作过程分开测量；它不是已经证明动态路由优于等预算单 Agent 的工作。

### 2. 可追溯证据

| 作者报告 | 位置 | 解读限制 |
|---|---|---|
| Minecraft：Llama-3.1-70B 的 TS=0.21、CS=75.00；GPT-4o-mini 的 TS=33.60、CS=61.50 | 表 1，p.8586 | TS 与 CS 是不同指标，不能互作成功率 |
| Research 人数消融使用 1/3/5/7 Agent，选取 20 篇至少有 7 位主作者的论文 | §5、图 8，p.8587 | 不是六类环境上的通用扩展规律 |
| 人机评分 Pearson r：Communication 0.8057、Planning 0.2685 | A.3、表 6，p.8595 | 两项有效性证据明显不同 |
| KPI 为各 Agent 里程碑贡献比例的平均 | §3.3，p.8584 | 分母含人数 N，不能等同最终成功率 |

### 3. 对原导读的补充与更正

原导读“继续增加反而下降”未说明指标，过于笼统：图 8 的 KPI、CS、TS 必须分别解读。本次不从图形估算未经确认的点值。

个人推断：在里程碑数量和总贡献计数不变时，KPI 会随 N 增大机械性下降。因此人数比较需要同时记录总完成量，不能仅凭 KPI 下降归因于协调复杂度。

§3.3 把 coding 归为规则评价，但 A.7（pp.8608–8609）描述的是多维五分评分流程；本次未核实代码最终如何落实，故不能将 Coding TS 当作隐藏测试 pass@1。Research TS 同样不是客观答题准确率。A.3 表 5 将无通信记为 -1，而 §3.3 写 0；须核对实现与统计口径。

### 4. 批判性判断（个人推断）

- 通信表现与执行能力可能脱钩。必须分别验证 CS 与人工评分一致、CS 与任务结果相关这两个命题。
- 主实验比较模型，拓扑实验集中在 Research。不能由此给其他环境选定“最佳拓扑”。
- 图 5 报告缩放后的 Token usage；有成本展示不等于有总预算匹配。原文未报告本研究所需的等预算 best-of-N 对照。
- 能说服评分器的协作文本，不一定产生可执行结果。CS 可作诊断，不宜未经验证直接用作优化奖励。

### 5. 复现可行性与最小验证

[官方 MARBLE 仓库](https://github.com/ulab-uiuc/MARBLE)入口已核对，尚未安装或执行。优先检查 Database 的数据与评分：A.6.4（p.8608）采用两个预测根因中一个正确即可命中的规则，不可冒称 top-1 accuracy。Research 适合检查评分器，但不作为客观任务成功的唯一依据。

建议先固定已有输出做评分与指标审计，再开展模型调用。模型/API、Token 上限和当前费用待预跑确认；全套环境运行成本本次未核实。实际结果：未运行。

### 6. 与个人研究的关系及下一步

个人推断：IDEA-001 首轮需要一项客观且口径固定的任务指标，CS 仅作辅助；不新增“CS 高则路由收益高”的假设。方向地图已有强单 Agent、best-of-N、成本要求，本次保留并补足其依据。

核心论文产物：[extract](../../artifacts/MA-002/extract.md) → [critic](../../artifacts/MA-002/critic.md) → [design](../../artifacts/MA-002/design.md) → [audit](../../artifacts/MA-002/audit.md)。未确定实施，暂不生成 spec；本人状态仍为 TO_READ。
