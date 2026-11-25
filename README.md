<div align="center">

# 🛰️ nav-research-skills

**面向导航领域的 AI Skills · 从文献调研到实验结果展示**

🧭 多源融合导航　·　📡 定位与感知　·　📊 科研可视化　·　🤝 研究协作

<p>
  <img src="https://img.shields.io/badge/AI-Skills-334155?style=flat-square" alt="AI Skills">
  <img src="https://img.shields.io/badge/Focus-Navigation-0369a1?style=flat-square" alt="Focus: Navigation">
  <img src="https://img.shields.io/badge/Research-Visualization-0f766e?style=flat-square" alt="Research Visualization">
</p>

以导航科研需求为起点，也适用于其他科研领域的数据展示、工程表达与工作衔接。

</div>

---

## 项目定位

本仓库由 **ColourDyeing** 维护，汇集自主制作的导航科研技能与第三方实用技能，面向导航、定位、多源感知及其他相关科研领域的研究者。

将反复调整的绘图样式、工程插画要求和研究协作流程沉淀为可复用的 AI 工作说明，减少重复沟通，让精力更多地用于研究本身。当前主要围绕 Codex 工作流整理；在其他 AI 工具中的使用取决于其技能、脚本和图像工具支持。

| 方向 | 关注的问题 | 可拓展的科研用途 |
| :--- | :--- | :--- |
| 文献研究 | 单篇论文的证据在哪里？不同技术路线在哪些条件下可比？ | 文献精读、书单整理、课题设计 |
| 科研绘图 | 导航轨迹、ENU 误差、误差分布与多算法对比 | 实验结果可视化、统一图表样式、批量生成数据草图 |
| 学术插画 | 定位场景、多源感知、系统关系与工程部署 | 工程场景表达、技术路线展示、学术汇报配图 |
| 研究协作 | 查找适合任务的技能、保存持续研究的上下文 | 工具发现、项目交接、跨会话继续工作 |

## 收录技能

**自制技能的作者为 ColourDyeing；第三方技能保留原作者署名与许可证。** 下表中的技能名链接到仓库内的完整说明。

| Skill | 简介 | 作者 / 归属 | 版本 |
| :--- | :--- | :--- | :--- |
| [find-skills](find-skills/SKILL.md) | 检索、比较和安装适合任务的技能，连接 Skills CLI 与技能生态 | **Vercel** · 第三方收录 | 以收录内容为准 |
| [nav-sciplot](nav-sciplot/SKILL.md) | 基于 Matplotlib 与 SciencePlots 的导航科研绘图，支持中英文、自定义样式及 SVG / PDF / PNG 导出 | **ColourDyeing** · 自制 | **V2.0** · 2026-11-16 |
| [nav-illustrations](nav-illustrations/SKILL.md) | 面向导航与工程研究的学术插画，覆盖单体场景、局部组合和全页系统示意图 | **ColourDyeing** · 自制 | **V2.0** · 2026-11-16 |
| [nav-reader](nav-reader/SKILL.md) | 导航中英文文献精读，支持多种原文入口、单张 Markdown 精读卡、可通过调用实时更新**个人研究画像和文献阅读历史** | **ColourDyeing** · 自制 | **V1.0** · 2026-11-25 |
| [nav-reasearch](nav-reasearch/SKILL.md) | 围绕指定方向编排快速入门书单，按阅读顺序串起经典代表作与近期前沿论文，附原文、入选依据和精读问题 | **ColourDyeing** · 自制 | **V1.0** · 2026-11-25 |
| [nav-error-presentation](nav-error-presentation/SKILL.md) | 将已有导航误差序列和统计结果整理为英文误差图与三线表，统一单位、图例和导出样式 | **zack2026art** · [社区贡献 PR #1](https://github.com/ColourDyeing/nav-research-skills/pull/1) | **V1.0** · 2026-11-24 |
| [session-handoff](session-handoff/SKILL.md) | 将目标、进度、关键决策和后续任务整理为交接文档，便于继续研究工作 | **OneWave AI** · 第三方收录 | 以收录内容为准 |

### 使用说明

| 想完成的任务 | 可以直接发给 AI 的请求 |
| :--- | :--- |
| **nav-reasearch** · 快速进入一个研究方向 | `$nav-reasearch` 我刚开始研究城市 GNSS 多路径抑制。请从建立概念、掌握基线到了解前沿，排一份入门书单。区分代表作与近三年的前沿论文，每篇附原文、推荐理由和阅读时要回答的问题。 |
| **nav-reader** · 精读书单中的一篇论文 | `$nav-reader` 请精读这篇论文，把方法、实验条件和主要结论整理为一张精读卡。指出哪些图表支持结论，以及方法在哪些场景失效。 |
| **nav-sciplot** · 批量绘制实验结果 | `$nav-sciplot` 根据这两组定位结果和真值绘制轨迹与水平误差 CDF。复用已有 Python 环境和项目配色，通过 `StyleConfig` 统一样式，按需补依赖，并附独立复现包。 |
| **nav-illustrations** · 制作工程示意图 | `$nav-illustrations` 为这页汇报制作全页系统示意图，从同类案例选取构图参考，把标签和技术连线保留为可编辑元素。只需解释一个场景或局部机理时，可指定单体场景或局部组合模式。 |
| **nav-error-presentation** · 排版已有误差结果 | `$navigation-error-presentation` 比较两套拟动态 PPP 解在五个静态站的表现。按东、北、天三个方向绘制逐历元误差折线组图，并用三线表列出同历元 RMSE。 |
| **find-skills** · 寻找工具 | `$find-skills` 帮我找适合检查论文图表的技能，列出来源和适用范围。 |
| **session-handoff** · 交接研究进度 | `$session-handoff` 把本轮实验的已验证结论、关键文件和下一步写进交接文档。 |

nav-reader 首次使用时按需在本机创建 `private/`，保存读者自己的研究画像与阅读历史。共享包通过空的 `.gitkeep` 保留目录结构，个人档案只保存在本机。整目录重装前先备份自己的档案。详见[档案维护说明](nav-reader/references/reading-records.md)。

### nav-sciplot · 科研绘图案例

<p align="center">
  <img src="nav-sciplot/assets/navigation-results-example.png" alt="nav-sciplot 科研绘图案例：轨迹、可见卫星数、水平误差与高程误差" width="760">
</p>

<p align="center"><em>nav-sciplot 案例展示 · 导航轨迹与多算法误差对比</em></p>

### nav-illustrations · 插画效果参考

<p align="center">
  <img src="nav-illustrations/assets/single-scenes/4.png" alt="nav-illustrations 多源融合导航插画参考案例" width="760">
</p>

<p align="center"><em>nav-illustrations 案例素材 · 用于构图与表达参考</em></p>

### nav-error-presentation · 误差图与三线表案例

五个虚构静态站采用两套模拟精密单点定位（PPP）解。每列对应一个站，三行依次为东、北、天方向。蓝线和橙线分别表示两套解的逐历元误差，采样间隔为 1 分钟。下表使用每站全部 1,440 个共同历元（含初始化阶段），给出 E、N、U、水平和三维 RMSE。图表均使用厘米。

![五个虚构静态站的拟动态 PPP 模拟案例，含 ENU 误差折线组图和共同历元 RMSE 三线表](nav-error-presentation/assets/simulated-kinematic-ppp.png)

### 第三方技能原文

| Skill | 原作者 | 原文链接 | 许可 |
| :--- | :--- | :--- | :--- |
| find-skills | Vercel | https://github.com/vercel-labs/skills/tree/main/skills/find-skills | [MIT](find-skills/LICENSE) |
| session-handoff | OneWave AI | https://github.com/OneWave-AI/claude-skills/tree/main/session-handoff | [MIT](session-handoff/LICENSE) |

第三方技能的原始贡献归原作者所有。本仓库收录版本与上游可能存在差异，最新内容及维护说明请以原项目为准。

## 更多科研技能项目

以下项目来自共享手册中的拓展推荐，**未打包收录在本仓库中**。作者栏使用项目维护者的 GitHub 账号。

| 项目 | 作者 / 维护者 | 主要方向 |
| :--- | :--- | :--- |
| **nature-skills** | Yuan1z0825 | 学术阅读、写作润色、科研绘图与汇报表达 |
| **ARS-Codex** · academic-research-skills-codex | Imbad0202 | 面向 Codex 的学术研究流程，覆盖文献、研究问题、论文与修订 |
| **CCFA-Skills** | mikubaka88 | 面向 CCF-A 研究与写作，覆盖选题、文献、实验设计、可视化及审稿回复 |

- **nature-skills**：https://github.com/Yuan1z0825/nature-skills
- **ARS-Codex**：https://github.com/Imbad0202/academic-research-skills-codex
- **CCFA-Skills**：https://github.com/mikubaka88/CCFA-Skills

## 仓库与交流

**维护者：ColourDyeing**

- **GitHub**：https://github.com/ColourDyeing/nav-research-skills

欢迎通过 Issues 或合并请求反馈需求、改进技能和补充科研案例。贡献第三方内容时，请注明原作者、原文链接及适用许可证；个人数据、本机环境记录和临时输出不纳入共享内容。

## 署名与许可

`nav-sciplot`、`nav-illustrations`、`nav-reader` 和 `nav-reasearch` 由 ColourDyeing 制作和维护。`nav-error-presentation` 由 zack2026art 贡献。`find-skills` 与 `session-handoff` 分别来自 Vercel 和 OneWave AI，并保留各自的 MIT 许可证。

本仓库尚未声明统一许可证。第三方技能遵循各自许可证；自制技能及参考素材的使用、修改与再分发范围，不因仓库公开而自动获得统一授权。需要进一步使用或分发时，请联系维护者确认相应内容的许可。
