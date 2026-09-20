# MA-004 与 MA-003：从综述分类到实验变量

- 日期：2026-09-21；两篇核验深度均为关键章节阅读（skimmed）。本文件不依赖另一篇 PR 合并。
- 来源：[MA-003 正式版 §3、表 1–2](https://www.ijcai.org/proceedings/2024/0890.pdf)；[MA-004 v1 §§3–4、表 2–5](https://arxiv.org/html/2501.06322v1)。
- 主笔记：[MA-003](../notes/multi-agent/llm-multi-agent-survey.md)、[MA-004](../notes/multi-agent/collaboration-mechanisms-survey.md)。本文件直接核对原文；若 MA-003 笔记仍为摘要级，不将本文件的证据深度反推给该笔记。

## Method、dataset、metric、result 对齐

| 维度 | MA-003 | MA-004 | 可比较性边界 |
|---|---|---|---|
| Method | 从环境、profile、通信、能力获取描述系统 | 从 channel 属性与编排描述协作 | 相互补充，不是一一替代 |
| Dataset | 表 2 罗列评测资源 | 讨论应用与评测挑战 | 无统一评测数据交集的实证分析 |
| Metric | 按应用梳理评价需求 | 强调整体表现及协作层评价 | 未建立共同数值标尺 |
| Result | 分类框架与研究地图 | 机制分类与开放问题 | 不提供方法优越性的统一实验排名 |

## 分类对齐及个人建议

| MA-003 视角 | MA-004 对应 | 转成实验记录时的注意点 |
|---|---|---|
| Agent profile | actors / role-based strategy | 区分身份描述、实际能力和路由规则 |
| communication paradigm | collaboration type | Debate 是过程，合作/竞争是目标关系，不强制等同 |
| communication structure/content | structure / channel | 分别记录谁能通信与交换什么信息 |
| environment / feedback / adjustment | agent environment 与协作阶段 | 记录反馈何时可见，记忆是否跨任务保留 |
| 动态系统相关描述 | static / dynamic orchestration | 动态人数、边、角色、停止分别标注 |

个人判断：两篇都不能证明哪个维度已有“最强基线”。应为选定变量补查直接原始实验，统一模型、数据、预算及指标后再比较。首轮建议固定其他维度，只改变一个控制动作；这是一项实验设计建议，不是两篇综述的结论。

证据缺口：本次未做系统性竞争工作检索，未逐篇复核综述引用的实验数字，不能宣称研究空白或复现成功。
