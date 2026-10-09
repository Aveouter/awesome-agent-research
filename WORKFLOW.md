# Research Workflow

这套流程用于把“看到论文”稳定地转化为“形成研究判断、完成复现、产生可投稿的问题”。默认每周处理 2–3 篇论文，避免为了维护仓库而维护仓库。

## 1. 生命周期

```text
发现论文
   ↓
INBOX：只记录链接和收录理由
   ↓ 每周筛选
TO_READ：进入 papers.md，分配唯一 ID
   ↓ 20–30 分钟速读
SKIMMED ─────────────→ DROPPED
   ↓ 值得继续
DEEP_READ：完成结构化笔记
   ├─ 普通论文 → 更新概念或跨论文综合
   └─ 核心论文 → extract → critic → design → spec → audit
                                      ↓ 有关键结果需要验证
                                  REPRODUCING
   ↓ 得到可解释的结果
REPRODUCED
   ↓
更新方向地图 / 形成研究假设 / 写作引用
```

状态只能按上述方向迁移。重新关注 `DROPPED` 论文时，先写明新证据，再改回 `TO_READ`。

恢复已放弃论文时使用 `transition <ID> TO_READ --reason "..."`，理由会写入总表的“下一步”列。

状态与证据等级是两个维度：状态表示本人完成到了哪一步；`evidence_level` 表示当前页面实际核对了多少原始材料。

```text
abstract-only → skimmed → full-paper → reproduced
```

例如，AI 根据全文建立了辅助导读时，页面可以是 `skimmed` evidence，但本人的状态仍是 `TO_READ`。

## 2. Capture：收集

发现论文后，在 `inbox.md` 追加一行：

- 使用论文主页、会议页面或 arXiv 等原始来源。
- 写一句“为什么与当前研究有关”，不要只保存标题。
- 暂时不要建笔记，不下载 PDF 到仓库。

也可以使用 GitHub 的 **Paper intake** issue 表单远程收集，周整理后关闭 issue。

## 3. Triage：每周筛选

每篇按 0–2 分快速判断，总分 0–10：

| 维度 | 0 分 | 1 分 | 2 分 |
|---|---|---|---|
| 方向相关性 | 无关 | 间接相关 | 直接影响当前问题 |
| 新颖性 | 已知做法 | 局部变化 | 新问题或新机制 |
| 证据质量 | 较弱 | 基本充分 | 强基线、消融和统计完整 |
| 可复现性 | 数据/代码不可得 | 部分可得 | 代码数据完整、成本可承受 |
| 研究价值 | 只适合了解 | 可作相关工作 | 可产生实验或反驳当前判断 |

- `7–10`：进入 `papers.md`，计划精读。
- `4–6`：只速读；除非出现新证据，不投入复现。
- `0–3`：标记 `DROPPED` 或不进入总表。

论文 ID 按方向递增：`MA-###`、`CL-###`、`MC-###`；跨方向论文使用 `X-###`。ID 一旦分配不再复用。

## 4. Skim：速读

建议顺序：摘要 → 图 1 → 实验表格 → 结论与局限 → 引言。目标不是理解全部公式，而是回答：

1. 它声称解决什么问题？
2. 最强证据是什么？
3. 与哪个强基线相比？
4. 最大限制或不公平因素是什么？
5. 是否值得精读、复现或引用？

完成后把状态改为 `SKIMMED`，并至少填写笔记中的“一句话结论”和“初步证据”。

## 5. Deep read：精读

从 `templates/paper-note.md` 复制笔记，文件名使用小写 kebab-case。精读完成的定义：

- 能不看摘要，用自己的话解释问题、方法和假设。
- 记录至少一个关键结果，并注明对应表格或图编号。
- 检查数据、基线、指标、消融和评测方式。
- 明确区分“作者的主张”和“自己的推断”。
- 写出最大局限、复现成本，以及它如何改变个人方向判断。
- 更新 `references/library.bib`。

全部完成后才能将状态设为 `DEEP_READ`。

## 6. Full analysis：核心论文分析链

参考 ACautomata/researcher 的两层科研技能设计，但在个人仓库中只对少量核心论文运行：

```text
主笔记 → extract → critic → design → spec → audit
```

产物放在 `artifacts/<paper-id>/`，从 `templates/` 复制对应模板。阶段边界如下：

- `extract`：提取实验目标、设置、主结果、消融、效率和证据位置；只记录事实，不进行完整批判。
- `critic`：检查 claim—机制—证据链，提出具体、重要、可验证的质疑；不直接写完整实验方案。
- `design`：把 critic 中的高优先级问题转成小规模、可控实验；每项必须有反证条件。
- `spec`：把设计翻译成执行任务、配置与结果格式；未知代码路径使用明确占位，不臆造。
- `audit`：只读检查结构完整性、证据分级、阶段边界和跨阶段一致性；区分必须修复与建议改进。

没有 `extract` 不进入 `critic`，没有 `critic` 不进入 `design`。只有用户要求实现或确定准备复现时才写 `spec`，避免产生无人执行的工程文档。

## 7. Reproduce：复现

复现前先建立 **Experiment** issue，并把问题写成可证伪假设。每次只做一个最小实验：

```text
experiments/<paper-id>-<short-name>/
├── README.md
├── configs/
├── scripts/
└── results/
```

`README.md` 必须记录模型版本、数据、随机种子、命令、GPU/API、Token、时间、费用、原论文结果和复现结果。大型模型、数据和原始轨迹不进入 Git。

如果代码能够运行但无法解释与原论文的差异，仍保持 `REPRODUCING`；只有结果可解释且失败案例已记录时，才设为 `REPRODUCED`。

## 8. Synthesize：形成研究产出

每完成一篇精读或复现，都检查三处：

- `research/direction-map.md`：是否有证据支持或推翻当前方向判断？
- `research/idea-backlog.md`：能否形成“假设—实验—反证条件”？
- `concepts/`、`entities/`：是否出现值得跨论文复用的稳定概念或实体？
- `syntheses/`：是否能形成 method、dataset、metric、result 对齐的跨论文比较？
- 当周日志：本周最重要的判断变化是什么？

“改一个 prompt”“多加一个 Agent”不单独算研究想法。一个合格想法必须说明对照组、预算、指标，以及出现什么结果就应放弃。

## 9. 每周与每月节奏

### 每周

- 周一：清理 inbox，选择 2–3 篇。
- 周二至周四：至少一篇精读或一个最小复现实验。
- 周五：更新总表、idea backlog 和 weekly log。
- 周末：只补遗漏，不无限扩充待读列表。

### 每月

- 汇总各方向新增证据、论文数量和复现进度。
- 删除长期无价值的待读项。
- 选出下月唯一主问题，而不是同时推进多个宽泛方向。

## 10. Git 约定

本地资料与仓库职责见 [文献文件与 Git 边界](docs/storage-boundaries.md)。`D:\paper` 不初始化为 Git 仓库，也不作为本仓库的子目录或链接导入。PDF、全文提取结果和 Zotero 数据只存本地。

首次使用克隆时执行 `python3 scripts/install_git_hooks.py`，启用提交和推送前检查；不要使用 `--no-verify` 绕过。新克隆不会自动安装 hooks。共享研究规则由 `AGENTS.md` 维护，`CLAUDE.md` 只引用，不复制 workflow。

所有修改，包括日常笔记、元数据、实验代码和仓库维护，都必须从最新 `main` 建立独立分支，通过 Pull Request 和自动检查后再合并。不得直接推送 `main`。

分支命名：

- `paper/MA-003-short-title`
- `experiment/MA-001-failure-router`
- `research/idea-003-short-name`
- `codex/paper-git-boundaries`：工具与规则维护示例。

每篇论文单独 PR，公共规则维护单独 PR。并行任务采用独立 worktree；共享总表与引用文件整合前核对最新基准。

提交前缀：

- `notes:` 新增或更新论文笔记
- `experiment:` 复现代码与结果
- `research:` 方向判断与研究想法
- `chore:` 仓库维护

提交或发起 Pull Request 前运行：

```bash
python3 .agents/skills/run-agent-paper-workflow/scripts/workflow.py validate
python3 scripts/check_git_boundary.py --staged
```

GitHub 会在 push 和 Pull Request 时自动执行相同检查。
