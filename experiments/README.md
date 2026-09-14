# Experiments

每个复现实验建立独立目录：

```text
experiments/<paper-id>-<short-name>/
├── README.md       # 目标、环境、命令、结果和结论
├── configs/        # 可提交的小型配置
├── scripts/        # 运行与评测脚本
└── results/        # 只提交汇总表，不提交大型原始输出
```

实验记录必须包含：

- Git commit、模型完整名称、提示词或配置版本。
- 随机种子、样本数量、重复次数。
- GPU/API、耗时、Token 和估算费用。
- 原论文结果、复现结果及偏差解释。
- 失败样例，不能只保存平均分。

大型数据集、模型权重、原始轨迹和密钥不得提交到 Git。
