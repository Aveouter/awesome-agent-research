# MultiAgentBench

## Metadata

- ID：MA-002
- Year / Venue：2025，ACL
- Paper：https://aclanthology.org/2025.acl-long.421/
- Code：https://github.com/ulab-uiuc/MARBLE
- Tags：multi-agent, benchmark, topology, coordination
- Status：TO_READ（AI 导读已建，本人待精读）

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
