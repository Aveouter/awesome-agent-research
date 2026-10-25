# IDEA-003：Skill-guided Heterogeneous Coevolution for Few-shot Generalization

- **状态**：研究设想 / 待验证（非已有方法或已证实结论）
- **记录日期**：2026-10-25
- **方向**：LLM Agent × 领域专用模型 × Few-shot Prompt Tuning × Skill Coevolution
- **灵感**：*Heterogeneous Agentic Coevolution*（HACE，ICLR 2027 在审稿件）；以及人类通过语言指导、规则和少量示例学习新任务的现象
- **核心目标**：提高少样本**泛化性**（尤其跨环境/跨任务），而不仅是训练集拟合效果或标注利用率；同时考虑有限计算预算

## 1. 原始想法与研究动机

一些科学领域缺少足够的标注数据，但人类专家可以利用长期积累的概念、操作流程、规则、反例和少量任务示例完成新任务。这里的“少样本”依赖强先验，并非从零学习。自然语言可以承载部分人类程序性知识；LLM 有机会将其组织为可迁移的 **Skills**，再用于指导专用模型学习。

想探索的不是“LLM 生成更多训练样本”，而是：

> **能否利用 LLM 构造、验证与迭代修正人类可理解的 Skills，让专用模型在极少标签下学到更稳定、更可迁移的规律？专用模型的反馈能否反过来提升 Skill Agent 的指导能力？**

在 HACE 中，Agent 通过相对预测增益筛选训练经验，Specialist 利用真实标签训练，Harness 优化交互与课程，Agent 再通过筛选的正增益响应自训练。对于 1/4/8/16-shot，依赖“继续筛选已有标注样本”的空间受到限制；值得将优化对象扩展为 **Skill → 表征/Prompt 归纳偏置 → 跨样本泛化**。

## 2. 核心区别：从预测贡献到学习贡献

- **原 HACE**：Agent 是否在某个样本上超过 Specialist？其探索如何帮助选择训练数据？
- **拟议 Skill-HACE**：Agent 生成的某个 Skill 是否能改善 Specialist 在**独立未见任务/样本**上的学习效果？即使 Agent 自己的领域预测不如 Specialist，仍可能提供有价值的知识先验。
- **避免混淆**：如果 LLM 参数始终冻结，只更新 Skill 库、Harness 和专用模型，称为“技能与模型协同适应”更准确；若还通过验证反馈对 LLM 的 Skill 生成策略做参数更新，才更接近双模型参数协同进化。

## 3. 假设（可证伪）

- **H1：技能先验与泛化**。经过任务验证的程序性 Skills（判断步骤、适用条件、反例、不变性）可以比同预算的纯类别描述/普通 Prompt 更稳定地改善小样本泛化，尤其是跨环境测试。
- **H2：双向反馈有效**。基于 Specialist 错误与独立任务反馈修正 Skill，比一次性静态生成 Skill 更有效；收益不能仅由更长 Prompt、更多候选或更多 LLM Token 解释。
- **H3：学习收益优于预测增益**。用“Skill 对 Specialist 的独立学习收益”作为 Agent 反馈，比用 Agent 自身预测的局部正确率作为筛选依据更适合小样本场景。
- **H4（可选）：计算约束**。在固定 Token/GPU-hours 下，对 Skill 验证和 Prompt 更新进行自适应预算分配，能获得更好的性能—成本前沿。

## 4. 方法草案：Generalization-aware Skill-HACE

**对象**：通用 LLM Skill Agent $A_\theta$、冻结主干的领域 Specialist $S_\phi$（仅训练 Soft Prompt 或轻量 Adapter）、Skill 库 $\mathcal K_t$、交互/选择 Harness $H_t$。

**Skill 表示**：$s=(C,P,I,E,V)$，分别为概念（concepts）、操作步骤（procedures）、已验证的不变性/约束（invariances）、例外与反例（exceptions）、可执行验证方式（verification）。自然语言规则必须经过领域知识或任务反馈验证，不能直接视为科学事实。

**一轮协同过程**：

1. Skill Agent 根据领域背景、少量 support 样本和 Specialist 的错误模式，提出/改写 Skills；不直接把 LLM 的输出当作真实标签。
2. Harness 选择 Skill、组合规则、注入位置（文本 Prompt / Soft Prompt 初始值 / Adapter / 可微约束）及验证预算。
3. 冻结 Specialist backbone，在 support set 上训练少量 Prompt/Adapter 参数，构造 $S_{\phi(s,H)}$。
4. 使用元训练阶段**独立的 query 样本/任务**评价技能边际收益和稳定性，并对错误 Skill 作淘汰或修订；同一目标任务的最终 test set 不参与反馈。
5. 用已验证的有效/无效 Skill 编辑轨迹改进 Agent 的技能生成策略（第一版可固定 LLM 参数，仅更新 Skill 库；后续再用 ReST/LoRA），进入下一轮。

概念性学习收益奖励：

$$
r(s; \tau)=\widehat R_{Q_\tau}(S_{\mathrm{base}})
-\widehat R_{Q_\tau}(S_{\mathrm{with}\ s})
-\lambda\,\mathrm{Cost}(s).
$$

其中 $Q_\tau$ 是该**元训练任务**独立于 support set 的 query 数据；$\widehat R$ 为风险（越小越好）；该奖励需要用足够多任务估计，不应在仅有的 4 个标签上反复选择。

建议训练目标（具体形式待设计）：

$$
\mathcal L=\mathcal L_{\mathrm{few\text{-}shot}}
+\alpha \mathcal L_{\mathrm{skill\text{-}grounding}}
+\beta \mathcal L_{\mathrm{valid\text{-}invariance}}
+\gamma\mathcal L_{\mathrm{prior}}.
$$

这些额外项需明确**可计算定义**；特别是不变性约束只能来自已验证的标签保持变换。

## 5. 泛化性怎么衡量

至少分开评估三类目标：

1. **同分布未见样本**：support 之外的独立 query/test 样本；
2. **跨环境泛化**：设备、批次、采集条件或数据来源变化（leave-one-domain-out）；
3. **跨任务/类别泛化**：在多个历史任务上元训练技能生成策略，测试全新任务/类别（meta-test）。

**数据约束**：若目标问题总共只有 4 个标签、没有相关历史任务、无可靠无标签结构或可验证领域约束，则不能仅靠 LLM 对话可靠判断泛化。需要明确外部先验与反馈的来源；不能用测试集参与自适应搜索。

## 6. 最小验证实验

- **起步任务**：人类判别知识可用语言清楚描述、且有环境/设备变化的科学图像分类（如材料显微缺陷）；具体数据集和合法不变性须先核验。
- **Specialist**：冻结 CLIP 或合适的领域视觉基础模型；优化 Soft Prompt 或小型 Adapter。
- **设定**：1/4/8/16-shot；多任务或多域 episodic meta-train，独立 meta-validation / meta-test。
- **基线**：无 Skill 的 Prompt Tuning（如 CoOp）、静态 LLM Skill、随机/错误 Skill、HACE 风格样本选择、动态 Skill 修订、完整 Skill + Harness 共同优化。保持 backbone、标注预算、候选搜索次数与 LLM Token 预算可比。
- **指标**：IID / OOD 准确率或宏 F1、泛化 gap、跨任务迁移、不同 shot 的学习曲线、稳定性、GPU-hours、输入/输出 Token。
- **消融**：Concept-only vs. Procedural Skill；有/无例外、验证器、不变性、Skill 修订、Harness 搜索、Agent 参数更新。
- **反证条件**：与静态 Skill 或随机 Skill 相比无稳定收益；提升仅来自更多搜索/参数/Token；OOD 下降；技能无可验证的中间表示对齐；在未参与优化的新任务上收益消失。

## 7. 理论切入点（待证明）

- **Skill-conditioned prior / PAC-Bayes**：在独立于目标 query/test 的历史任务上形成 Skill 先验，分析其对 Prompt/Adapter 假设空间复杂度和泛化界的影响。
- **先验失配和负迁移**：技能约束过强或错误时，刻画偏差增加的条件，并设计回退到无 Skill 模型的保守机制。
- **自适应 Skill 搜索的统计代价**：多轮使用验证反馈会增加过拟合风险；可考虑元任务样本拆分、稳定性分析或统一置信界，不能直接套用固定先验泛化界。
- **成本感知选择（延伸）**：以单位 Token / GPU-hour 的预期泛化增益作为决策指标，在可分析假设下研究 bandit regret 或预算受限的样本/技能选择界。

## 8. 相关工作与边界

- **HACE**：异构 Agent 与 Specialist 在 Harness 下交替优化；本文思想来源，但原论文并没有提出这种 Skill 驱动的 few-shot 泛化方案。
- **LaBo**：LLM 产生语言概念辅助少样本视觉学习；提醒“LLM 概念增强”本身不构成新颖性。
- **CoCoBMs / BC-LLM**：动态概念选择、概念先验及不确定性相关研究；需进一步核查与这里的技能验证/共同适应之间的差异。
- **CoOp / CoCoOp / KgCoOp**：few-shot prompt tuning 与泛化的重要基线。

**尚待回答**：真正能否迁移的是 *procedural skill*，还是更长的类别描述？是否需要 LLM 参数更新，还是 Skill Library + Harness 已足够？如何在弱标签反馈下确认技能真的可泛化？

## 9. 下一步

先做**静态 Skill vs. 经过反馈修订的 Skill**、在严格独立 OOD / meta-test 上的最小实验。如果在固定训练与推理预算下确有提升，再实现 Harness 进化和 Agent LoRA 更新，并开展理论分析。

> 本文件仅记录研究假设与初步实验构想，未开展训练、未验证结果，也不代表 HACE 作者的主张。
