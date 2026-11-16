# 默认排版与样式配置

这些是默认预设，用户指定的字体、字号、期刊和版心优先。通过 `StyleConfig` 统一覆盖，避免只改 rcParams 导致导出记录与图形不一致。

- Python + Matplotlib + SciencePlots，先加载 `['science', 'no-latex', 'grid']`，再应用字体等覆盖设置。不要让随后调用的 seaborn 全局主题覆盖样式。
- 默认中文宋体 SimSun，西文和数字 Times New Roman，使用 `apply_style()`（等同 `apply_style(language='zh')`），按 `font.family = ['Times New Roman', 'SimSun']` 逐字符回退，不能把整段混合文字都设为宋体。只有用户指定全英文图时，使用 `apply_style(language='en')`，所有标题、坐标轴、图例和注释翻译成英文，字体统一 Arial（`font.family = ['Arial']`）。导出前验证当前模式所需字体，缺失时明确报告，不静默替换。无外部 LaTeX 依赖；数学公式的西文也匹配当前模式的 Times New Roman 或 Arial，少见符号允许数学字体补字并说明。
- 主标题与各子图标题 13 pt；坐标轴名、刻度、图例、图例标题、注释、色条文字、面板标号等其余文字 11 pt。不要为了塞下内容降低字号。
- 单图不默认铺满 A4 版心，按内容选择尽可能小而清晰的尺寸：简单单图优先 **84 mm** 宽（`new_figure()`），多算法、长图例等中等内容优先 **129 mm** 宽（`new_figure(content='moderate')`）；两者是优先档位，可以根据实际内容选其他较小宽度。高度按曲线、文字和纵横比调整，轨迹可接近正方形。保持 13/11 pt，先调整刻度数量、图例位置、标题换行或拆图；84 mm 太挤时再升至 129 mm，不能为追求小尺寸降低字号，也不能先画大图再缩小来伪装小尺寸。
- 组图或内容较多时可按需要增大，默认整张画布上限为 **15.9 × 24.5 cm**（包括标题、轴名、图例和留白）；`new_figure(多行, 多列)` 使用组图宽度，密集单图可用 `content='dense'`。这是上限而非目标尺寸。按 A4 21 × 29.7 cm、四周 2.54 cm 页边距，正文为 15.92 × 24.62 cm，略留余量；若 Word 模板不同，以其真实版心为准。用户明确指定尺寸时优先。
- 屏幕展示宽度与物理尺寸分开。640 px 预览不是 640/96 英寸的强制画布宽度。DPI 不决定矢量图的印刷宽度；Word 中保持原尺寸插入才能保持 13/11 pt。
- 默认 SVG（保留文字）+ PDF（嵌入 TrueType 子集）+ 240 dpi PNG。SVG 在另一台机器上需要当前语言模式的相同字体；跨设备优先 PDF，必要时额外输出文字转路径的 SVG，不能替换可编辑版本。期刊要求更高 DPI 时遵从要求。
- 用 constrained layout 调整布局，导出使用 `bbox_inches=None` 保持物理尺寸；禁止用 `bbox_inches='tight'` 意外扩大画布。过密时调整留白、换行或拆图，再检查尺寸。


## 自定义配置

```python
from sci_style import StyleConfig, apply_style, new_figure, export_figure

config = StyleConfig(
    language="en",
    western_font="DejaVu Sans",  # 用户明确选用的替代字体
    title_pt=12, text_pt=10,
    simple_width_cm=8.9, max_width_cm=18.0,
)
apply_style(config=config)
fig, ax = new_figure()
# 绘图后 export_figure(fig, ...) 自动记录这份配置。
```

`language` 控制中英文模式；`western_font`、`chinese_font` 控制字体；`title_pt`、`text_pt` 控制字号；`simple_width_cm`、`moderate_width_cm`、`max_width_cm`、`max_height_cm` 控制尺寸。未指定字体时保留原默认值。字体缺失时报告缺失字体，由用户指定替代方案，不静默替换，也不随包分发商业字体。

每张图保存建图时的配置。请先应用配置、再建图和绘图；中途切换配置时先完成当前图的导出。`allow_oversize=True` 仅用于明确要求超出配置上限的尺寸，建图与导出都需要传入。
