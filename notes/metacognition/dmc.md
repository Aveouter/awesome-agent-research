# Decoupling Metacognition from Cognition

## Metadata

- ID：MC-001
- Year / Venue：2025，AAAI
- Paper：https://ojs.aaai.org/index.php/AAAI/article/view/34723
- Code：https://github.com/Angelo3357/DMC
- Tags：metacognition, calibration, confidence, abstention
- Status：TO_READ（AI 导读已建，本人待精读）

## 一句话结论

答得正确和知道自己是否会答是两种能力；DMC 尝试用信号检测理论将二者分离，但主要覆盖静态问答中的置信度，而不是完整 Agent 的规划与自我改进。

## 初步证据

- 在多个领域的二选一数据集上收集答案和置信度。
- 比较不同置信度提取方式，并量化认知能力与元认知能力。
- 元认知指标与 AbstainQA 中的可靠回答和合理拒答表现呈一致趋势。

## 精读时重点质疑

1. 二选一任务上的指标能否推广到开放式生成和工具使用？
2. 置信度提取方法对最终排名有多敏感？
3. 校准、失败预测和元认知是否被概念性混用？
4. 指标能否指导多 Agent 中的求助、路由和验证？

## 最小复现

先选一个小型二分类数据集和 2–3 个开源模型，复现置信度提取及 DMC 指标，再测试该指标是否能够预测“是否应该调用第二个 Agent”。
