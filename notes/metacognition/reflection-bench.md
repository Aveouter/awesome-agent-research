# Reflection-Bench

## Metadata

- ID：MC-002
- Year / Venue：2025，ICML
- Paper：https://proceedings.mlr.press/v267/li25cu.html
- Code：https://github.com/AI45Lab/ReflectionBench
- Tags：metacognition, epistemic agency, reflection, benchmark
- Status：TO_READ（AI 导读已建，本人待精读）

## 一句话结论

论文把 epistemic agency 拆成七种相互联系的能力，并发现现有模型在元反思上尤其薄弱；它适合用来界定问题，但不是现成的 Agent 改进方法。

## 七个维度

- 预测
- 决策
- 感知
- 记忆
- 反事实思考
- 信念更新
- 元反思

## 初步证据

- Benchmark 包含七项任务，强调长期相关性并尽量降低数据泄漏。
- 评估 16 个模型和三种提示策略。
- 模型表现形成明显层级，最先进模型也只表现出初步 epistemic agency。

## 精读时重点质疑

1. 七个任务是否真的测到了同一个高层构念？
2. 静态任务成绩如何对应真实 Agent 的行为？
3. 元反思失败来自能力不足，还是提示、解析和评价方式？
4. 哪个维度最适合转化为可训练、可消融的 Agent 模块？
