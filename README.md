<div align="center">

# nav-research-skills

**面向导航领域的 AI Skills · 从科研绘图到学术表达**

多源融合导航 / 定位与感知 / 科研可视化 / 研究协作

以导航科研需求为起点，也适用于其他科研领域的数据展示、工程表达与工作衔接。

</div>

---

## 项目定位

本仓库由 **ColourDyeing** 维护，汇集自主制作的导航科研技能与第三方实用技能，面向导航、定位、多源感知及其他相关科研领域的研究者。

将反复调整的绘图样式、工程插画要求和研究协作流程沉淀为可复用的 AI 工作说明，减少重复沟通，让精力更多地用于研究本身。当前主要围绕 Codex 工作流整理；在其他 AI 工具中的使用取决于其技能、脚本和图像工具支持。

| 方向 | 关注的问题 | 可拓展的科研用途 |
| :--- | :--- | :--- |
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
| [session-handoff](session-handoff/SKILL.md) | 将目标、进度、关键决策和后续任务整理为交接文档，便于继续研究工作 | **OneWave AI** · 第三方收录 | 以收录内容为准 |

### 自制技能 · V2.0 更新

- **nav-sciplot**：新增环境复用与本机环境记录，通过 `StyleConfig` 集中管理样式，支持按需依赖与独立复现包。
- **nav-illustrations**：扩展三种插画组织模式，按分类目录选择参考案例，增强可编辑标签和技术连线的交付。

科研绘图侧重快速、批量的数据可视化与样式复用；投稿前仍需结合期刊要求精调。插画侧重技术关系和视觉表达，具体交付形式取决于可用的图像与演示文稿工具。

### 科研绘图案例

<p align="center">
  <img src="nav-sciplot/assets/navigation-results-example.png" alt="nav-sciplot 科研绘图案例：轨迹、可见卫星数、水平误差与高程误差" width="760">
</p>

<p align="center"><em>nav-sciplot 案例展示 · 导航轨迹与多算法误差对比</em></p>

### 插画效果参考

<p align="center">
  <img src="nav-illustrations/assets/single-scenes/4.png" alt="nav-illustrations 多源融合导航插画参考案例" width="760">
</p>

<p align="center"><em>nav-illustrations 案例素材 · 用于构图与表达参考</em></p>

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

`nav-sciplot` 与 `nav-illustrations` 由 ColourDyeing 制作和维护；`find-skills` 与 `session-handoff` 分别来自 Vercel 和 OneWave AI，并保留各自的 MIT 许可证。

本仓库尚未声明统一许可证。第三方技能遵循各自许可证；自制技能及参考素材的使用、修改与再分发范围，不因仓库公开而自动获得统一授权。需要进一步使用或分发时，请联系维护者确认相应内容的许可。
