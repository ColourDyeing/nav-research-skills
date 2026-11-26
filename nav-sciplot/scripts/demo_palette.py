"""Reproduce the six-method v3 palette demo, using its original synthetic ENU data."""
import argparse
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

from sci_style import COLORS, LINESTYLES, apply_style, ecdf, export_figure, new_figure

NAMES = 'ABCDEF'
MARKERS = 'os^DvP'
PANELS = ('bar', 'series', 'cdf', 'trajectory', 'scatter', 'heatmap')


def simulated_data():
    rng = np.random.default_rng(42)
    t = np.arange(120)
    theta = t * 2 * np.pi / t.size
    truth = np.array([9 * np.cos(theta), 7 * np.sin(theta)]).T
    errors = []
    for i in range(len(NAMES)):
        direction = theta + i * np.pi / 3
        err = (0.45 + i * 0.32) * np.array([np.cos(direction), np.sin(2 * direction)]).T
        err += rng.normal(0, 0.09 + i * 0.025, err.shape)
        errors.append(err)
    return t, truth, np.array(errors)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--until', type=float, help='Last time in seconds to display in the series panel.')
    parser.add_argument('--language', choices=('zh', 'en'), default='zh')
    args = parser.parse_args()
    en = args.language == 'en'
    apply_style(language=args.language)
    t, truth, errors = simulated_data()
    selected = np.ones(t.size, dtype=bool) if args.until is None else t <= args.until
    if not selected.any():
        parser.error('The requested window contains no epochs.')
    shown = t[selected]
    h = np.linalg.norm(errors, axis=2)
    full = f'{t.min()}–{t.max()} s'
    window = f'{shown.min()}–{shown.max()} s'
    stats = {'data': 'v3 synthetic ENU, 1 Hz', 'seed': 42, 'common_valid_epochs': len(t),
             'full_window_s': t[[0, -1]].tolist(), 'series_window_s': shown[[0, -1]].tolist(),
             'series_epochs': len(shown), 'filtering': 'none', 'scatter_stride': 4,
             'segments': 'six consecutive 20-epoch means', 'purpose': 'palette demonstration'}
    titles = (('Horizontal RMSE', 'Error time series', 'Empirical CDF', 'Planar trajectories',
               'Error scatter', 'Segment means') if en else
              ('水平误差 RMSE', '误差时序', '经验分布', '平面轨迹', '误差散点', '分段均值'))
    method = 'Method' if en else '方案'
    horizontal = 'Horizontal error (m)' if en else '水平误差 (m)'
    labels = {'bar': (method, 'RMSE (m)'), 'series': ('Time (s)' if en else '时间 (s)', horizontal),
              'cdf': (horizontal, 'Cumulative probability' if en else '累计概率'),
              'trajectory': ('East (m)', 'North (m)') if en else ('东向 (m)', '北向 (m)'),
              'scatter': ('East error (m)', 'North error (m)') if en else ('东向误差 (m)', '北向误差 (m)')}
    group, grid = new_figure(3, 2, height_cm=23.5)
    caption = (f'Synthetic navigation data for methods A–F. Each method has {len(t)} valid epochs over {full}. '
               f'The time series shows {window} ({len(shown)} epochs). RMSE, empirical distributions and '
               '20 s segment means use the full record. The scatter plot shows every fourth epoch.'
               if en else
               f'方案 A–F 使用模拟导航数据。每个方案在 {full} 内有 {len(t)} 个有效历元。'
               f'时序图显示 {window} 的 {len(shown)} 个历元。RMSE、经验分布和每 20 s 的分段均值均由全程数据计算，'
               '散点图每四个历元取一点。')
    stats['caption'] = caption
    singles = []
    for j, (kind, title, gax) in enumerate(zip(PANELS, titles, grid.flat)):
        fig, sax = new_figure(width_cm=8.4 if kind == 'bar' else 12.9,
                              height_cm=10.5 if kind in ('trajectory', 'scatter') else 9)
        singles.append((kind, fig))
        for ax in (gax, sax):
            if kind == 'heatmap':
                blocks = h.reshape(len(NAMES), -1, 20).mean(axis=2)
                rows, cols = blocks.shape
                im = ax.imshow(blocks, cmap='viridis', vmin=0, interpolation='nearest', aspect='auto')
                ax.grid(False)
                ax.set(xticks=np.arange(cols), xticklabels=np.arange(1, cols + 1),
                       yticks=np.arange(rows), yticklabels=list(NAMES),
                       xlabel='Time segment (20 s each)' if en else '时间段（每段 20 s）', ylabel=method)
                ax.vlines(np.arange(cols - 1) + .5, -.5, rows - .5, colors='white', linewidth=.3)
                ax.hlines(np.arange(rows - 1) + .5, -.5, cols - .5, colors='white', linewidth=.3)
                ax.figure.colorbar(im, ax=ax, orientation='horizontal', label='Mean horizontal error (m)' if en else '分段平均水平误差 (m)')
            else:
                for i, name in enumerate(NAMES):
                    style = dict(color=COLORS[i], linestyle=LINESTYLES[i], label=name,
                                 linewidth=1.35 if name == 'D' else 1.15)
                    if kind == 'bar':
                        ax.bar(name, np.sqrt(np.mean(h[i] ** 2)), color=COLORS[i])
                    elif kind == 'series':
                        ax.plot(shown, h[i, selected], **style)
                    elif kind == 'cdf':
                        x, y = ecdf(h[i])
                        ax.step(np.r_[0, x, h.max()], np.r_[0, y, 1], where='post', **style)
                    elif kind == 'trajectory':
                        if name == 'D':
                            style.update(marker=MARKERS[i], markevery=16, markersize=3, markerfacecolor='white')
                        ax.plot(*(truth + errors[i]).T, **style)
                    else:
                        ax.scatter(*errors[i, ::4].T, s=14, marker=MARKERS[i], facecolors='none',
                                   edgecolors=COLORS[i], linewidths=.75, label=name)
                ax.set(xlabel=labels[kind][0], ylabel=labels[kind][1])
                if kind in ('trajectory', 'scatter'):
                    ax.set_aspect('equal', adjustable='box')
                if kind == 'cdf':
                    ax.set(xlim=(0, h.max()), ylim=(0, 1.025))
            if ax is gax:
                ax.set_title(f'({chr(97+j)}) {title}')
                if kind == 'trajectory':
                    handles = [Line2D([], [], color=line.get_color(), linestyle=LINESTYLES[i],
                                      linewidth=line.get_linewidth(), marker=MARKERS[i], markersize=4,
                                      markerfacecolor='none', label=NAMES[i]) for i, line in enumerate(ax.lines)]
                    group.legend(handles=handles, loc='outside lower center', ncols=6,
                                 handlelength=2.6, columnspacing=1.1)
            else:
                ax.set_title(title)
                if kind in ('trajectory', 'cdf'):
                    ax.legend(loc='center' if kind == 'trajectory' else 'lower right', ncols=2)
                elif kind in ('series', 'scatter'):
                    # At this width all six entries would cover traces or outliers.
                    fig.legend(*ax.get_legend_handles_labels(), loc='outside right center')

    for stem, fig in [('palette', group), *singles]:
        export_figure(fig, args.output / stem, provenance=stats)
        plt.close(fig)
    (args.output / 'caption.txt').write_text(caption + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
