---
name: nav-sciplot
description: 从导航定位数据快速绘制轨迹、误差时序或经验分布，适用于给一份数据直接看图，也支持按明确比较要求制作论文组图。
---

# 导航定位科研绘图

用户给一份导航数据说“帮我看看这份数据”时，直接读字段和样本，选最有信息的一到两张图并生成预览。快速预览默认显示全程。坐标轴和色条默认写作“量名 (单位)”。有位置坐标就画轨迹，缺真值也可以展示路径；有误差序列就画时序，缺时间用原始样本序号并如实标轴。多方法有可比误差样本时可补阶梯 ECDF，缺阈值直接画分布。无需用户先选模式、图型、研究问题、配色、阈值或期刊。

用户指定的期刊、字体、尺寸和样式优先；默认使用中文宋体与 Times New Roman，全英文 Arial，标题 13 pt、其余文字 11 pt。

## 环境与资源

- 基本依赖统一维护在 `environment.yml`，已验证 Python 3.12；环境选择、创建与复用遵循下节规则。不修改系统 Python 或 Conda base 环境。
- Excel、HDF5、坐标转换和科学计算分别按需安装 openpyxl、h5py、pyproj、scipy。字体需单独准备；缺失时通过 `StyleConfig` 显式指定替代字体，不静默替换。
- 原有 `requirements-lock.txt` 和 `conda-win-64-explicit.txt` 仅为作者环境快照，后者不含 pip 绘图库；常规安装使用 `environment.yml`。共享时排除缓存、临时输出和个人数据。
- 绘图前阅读 [references/style.md](references/style.md)，通过 `scripts/sci_style.py` 的 `StyleConfig`、`apply_style()`、`new_figure()` 和 `export_figure()` 统一控制样式、尺寸和导出。
- 涉及时间对齐、坐标转换、统计或缺测时阅读 [references/navigation.md](references/navigation.md)。
- `scripts/demo_navigation.py --output <目录>` 生成单图样张与闭环轨迹组图。追加 `--paper` 可用同一组模拟数据生成论文组图，比较峰值附近的误差变化与全程误差达标比例。两种模式均支持 `--language en`。

- 六方案模拟配色样张可运行 `scripts/demo_palette.py --output <目录>`。如需复现 v3 的局部时序，追加 `--until 35`。英文版追加 `--language en`。图题仅写主题，时段、样本数和模拟数据说明见配套图注。

## 环境复用与本机记录

1. 本次明确指定的环境优先；否则先读取本技能目录的 `environment.local.json`，使用其中的 `python_path` 绝对路径。验证解释器可运行且能够导入本次所需依赖后直接绘图，不重复询问、不重建环境、不例行升级依赖。记录不存在或失效时，再查找已有可用的独立环境；不要仅因当前 PATH 中没有 Python 就认定环境不存在。
2. 确实没有可用环境时，说明缺少什么，并建议创建专用虚拟环境，给出拟用路径和方式（已有 Conda 时可使用 `environment.yml`，否则可使用 venv 并安装其中的基本依赖）。取得用户允许后才创建和安装；已有对这次操作的明确授权时不重复询问。用户未同意时不创建。
3. 创建或选定环境后，验证解释器和基本依赖，成功后才写入 `environment.local.json`，至少保存 `python_path`（绝对路径）和 `manager`（`conda` 或 `venv`）；后续调用直接使用这个解释器，不依赖终端激活状态。该文件是首次配置后产生的本机记录，不是共享包的一部分；Git 和手工打包均需排除。若记录无法写入，明确说明无法持久记住，不宣称已经保存。
4. 环境记录失效时优先查找和复用其他可用环境并更新记录；只有确需创建或重建时才再次提示，不自动删除旧环境。缺少任务专用依赖时只补齐所需项，不因缺少可选包而重建整个环境。字体缺失与 Python 环境缺失分别处理。

## 既有项目复用

优先沿用项目已有的绘图脚本和显式样式配置，本次用户要求优先；没有既有配置时才使用本技能默认值。复用环境和样式不省略新数据的单位、时间基准、坐标系及统计口径检查。

## 工作流程

1. 检查数据字段、单位、时间基准、参考真值和坐标系。优先从文件确认；能独立生成的图先生成。仅当未知信息实质影响用户明确要求的结果且文件无法解答时，问一个具体问题。没有数据时仅制作明确标为模拟数据的示例，不编造实验结论。
2. 配色或图型演示可并列展示多种画法。仅当用户明确提出投稿、论文组图或具体比较要求时，应用论文结果图规则，先用一句话明确正文要支持的比较，再按需选面板。例如，用时序定位误差峰值，用阶梯 ECDF 读取给定阈值内的比例。只保留有助于回答问题的面板，不默认使用六宫格。按导航参考说明各面板的参考来源、时间窗口和有效样本，单图优先在轴内空白处放局部图例，跨面板共享图例放在子图之外的公共位置。
3. 应用默认或用户指定配置。单图优先 84/129 mm 宽，组图默认不超过 15.9 × 24.5 cm；拥挤时调整刻度、图例、换行、尺寸或拆图，不擅自缩小选定字号。字体缺失应报告并明确替代方案。
4. 生成可执行脚本。相对输入路径以脚本位置为基准；导入技能辅助脚本时使用当前 skill 的真实路径，不写死作者本机路径。交付独立复现包时同时附带所需辅助脚本和配置，避免依赖作者安装目录。
5. 使用 `export_figure()` 默认输出可编辑 SVG、嵌入字体 PDF、240 dpi PNG 和 `.figure.json`。`provenance` 记录输入文件、列映射、单位、时间对齐、过滤/抽稀、指标定义和人工参数，不把未知处理写成已完成。
6. 运行脚本，检查缺字、警告、尺寸和文字边界，打开 PNG 检查遮挡及拥挤。自动边界检查不能代替视觉验收。交付图片、复现脚本和处理说明；筛除数据时报告数量与原因。

## 调用示例

`$nav-sciplot 根据这个 CSV 绘制三种融合算法的水平误差曲线和 CDF，时间单位秒、误差单位米。`

最小结构（`skill_dir`、`input_path` 和 `output_dir` 由实际任务确定）：

```python
from pathlib import Path
import sys
import matplotlib
matplotlib.use('Agg')  # 无窗口批处理；Notebook 可省略
import matplotlib.pyplot as plt

sys.path.insert(0, str(Path(skill_dir) / 'scripts'))
from sci_style import apply_style, new_figure, export_figure

apply_style()
fig, ax = new_figure()
# 读取真实数据并绘图，物理量标注单位。
ax.set(xlabel='时间 (s)', ylabel='水平误差 (m)', title='水平定位误差')
export_figure(fig, output_dir / 'horizontal_error',
              provenance={'input_file': str(input_path)})
plt.close(fig)
```
