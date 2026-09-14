# Domain Language

本文件定义仓库内术语，防止把阅读、证据和实验混成同一件事。

## Paper ID

论文的持久身份：`MA-###`（多 Agent）、`CL-###`（持续学习）、`MC-###`（元认知）、`X-###`（跨方向）。ID 分配后不复用。

## Status

人的工作进度：`TO_READ`、`SKIMMED`、`DEEP_READ`、`REPRODUCING`、`REPRODUCED`、`DROPPED`。AI 生成了摘要不代表用户已经完成阅读。

## Evidence level

当前页面所依据材料的深度，而不是可信度评分：

- `abstract-only`：仅核对摘要或元数据页。
- `skimmed`：核对全文关键章节、图表和结论，但没有逐项审阅。
- `full-paper`：通读正文与关键附录，主要数字可定位。
- `reproduced`：除全文外，至少一个关键实验得到可解释的复现结果。

## Paper note

一篇论文唯一的人类可读主页面，回答问题、方法、证据、局限、复现成本及与个人研究的关系。

## Analysis artifact

核心论文的阶段性产物，位于 `artifacts/<paper-id>/`。包括 `extract.md`、`critic.md`、`design.md`、`spec.md`、`audit.md`。它们不能相互越权。

## Claim

论文或个人提出的、可以被证据支持或反驳的陈述。记录时必须区分来源和证据强度。

## Research hypothesis

可以通过实验被证伪的关系判断，至少包含自变量、对照、指标和反证条件。功能愿望或“换一个 prompt”不属于研究假设。

## Reproduction

在明确配置、预算和评价协议下验证论文的关键结果。代码能够启动不等于完成复现；结果差异必须得到记录和解释。

## Synthesis

跨多篇论文对齐问题、假设、数据、指标和结果后形成的判断。Synthesis 应引用主笔记或原始来源，不能形成 wiki-to-wiki 的无来源引用循环。
