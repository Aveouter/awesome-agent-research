# Analysis Artifacts

> 可选扩展 / 历史资料；普通阅读不依赖本目录，既有记录保留。

普通论文只需要 `notes/` 下的主笔记。只有锚点论文、直接竞争工作或准备复现的论文才建立：

```text
artifacts/<paper-id>/
├── extract.md   # 实验事实与证据，不批判
├── critic.md    # claim—机制—证据链与可验证质疑
├── design.md    # 低成本验证实验
├── spec.md      # 可执行工程规格
└── audit.md     # 只读质量审计
```

从 `templates/` 复制对应模板。缺少上游阶段时，不凭空生成下游产物。
