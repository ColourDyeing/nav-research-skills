"""Generate four reproducible style examples. ALL DATA ARE SYNTHETIC."""
from pathlib import Path
import argparse

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, PercentFormatter
import numpy as np
import pandas as pd

from sci_style import apply_style, new_figure, export_figure, ecdf, COLORS, LINESTYLES


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--language', choices=('zh', 'en'), default='zh')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    apply_style(language=args.language)
    en = args.language == 'en'
    rng = np.random.default_rng(20261027)
    t = np.arange(0, 180.01, 0.5)
    phase = 2 * np.pi * t / t[-1]
    truth = np.column_stack((32 * np.sin(phase), 22 * np.cos(phase)))
    names = ['GNSS', 'GNSS/IMU', 'GNSS/IMU/Wi-Fi']
    errors = {}
    for i, name in enumerate(names):
        scale = [1.9, 1.05, 0.62][i]
        noise = rng.normal(0, scale * 0.24, (len(t), 2))
        drift = scale * np.column_stack((0.8 * np.sin(t / 11 + i * 0.3), 0.65 * np.cos(t / 16 + i * 0.4)))
        event = np.exp(-0.5 * ((t - 95) / 9) ** 2)[:, None] * np.array([[2.6, 1.8]]) * scale
        errors[name] = drift + noise + event
    frame = pd.DataFrame({'time_s': t, 'truth_e_m': truth[:, 0], 'truth_n_m': truth[:, 1]})
    metrics = []
    provenance = {'data_kind': 'SYNTHETIC DEMO ONLY / 仅用于样式演示的模拟数据',
                  'seed': 20261027, 'coordinate_frame': 'local ENU / m',
                  'time_alignment': 'all methods share the same synthetic epochs',
                  'filtering': 'none', 'n_epochs': len(t),
                  'source_script': str(Path(__file__).resolve())}
    for i, name in enumerate(names):
        err = errors[name]
        horizontal = np.linalg.norm(err, axis=1)
        prefix = f'method_{i + 1}'
        frame[f'{prefix}_e_error_m'] = err[:, 0]
        frame[f'{prefix}_n_error_m'] = err[:, 1]
        frame[f'{prefix}_horizontal_error_m'] = horizontal
        metrics.append({'method': name, 'sample_count': len(t),
                        'horizontal_rmse_m': np.sqrt(np.mean(horizontal ** 2)),
                        'p50_m': np.quantile(horizontal, 0.5, method='linear'),
                        'p95_m': np.quantile(horizontal, 0.95, method='linear')})
    frame.to_csv(args.output / 'synthetic_navigation.csv', index=False, encoding='utf-8-sig')
    pd.DataFrame(metrics).to_csv(args.output / 'synthetic_metrics.csv', index=False, encoding='utf-8-sig')

    fig, ax = new_figure(content='moderate', height_cm=8.6)
    for i, name in enumerate(names):
        ax.plot(t, np.linalg.norm(errors[name], axis=1), color=COLORS[i], linestyle=LINESTYLES[i], label=name)
    ax.set(xlim=(0, 180), ylim=(0, None), xlabel='Time / s' if en else '时间 / s',
           ylabel='Horizontal error / m' if en else '水平误差 / m',
           title='Horizontal error (synthetic)' if en else '水平定位误差（模拟数据）')
    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.yaxis.set_major_locator(MaxNLocator(5))
    ax.legend(loc='upper right')
    export_figure(fig, args.output / '01_horizontal_error', provenance=provenance)
    plt.close(fig)

    fig, ax = new_figure(content='moderate', height_cm=10.2)
    ax.plot(truth[:, 0], truth[:, 1], color='#303030', linestyle='--', linewidth=1.35,
            label='Reference' if en else '参考轨迹')
    for i, name in enumerate(names):
        estimate = truth + errors[name]
        ax.plot(estimate[:, 0], estimate[:, 1], color=COLORS[i], linestyle=LINESTYLES[i], label=name)
    ax.plot(truth[0, 0], truth[0, 1], marker='o', color='#303030', linestyle='none', markersize=4)
    ax.set(xlabel='East / m', ylabel='North / m',
           title='Trajectory comparison (synthetic)' if en else '平面轨迹对比（模拟数据）')
    ax.set_aspect('equal', adjustable='box')
    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.yaxis.set_major_locator(MaxNLocator(5))
    ax.legend(loc='center')  # The closed-loop interior is empty; keep the compact margins.
    export_figure(fig, args.output / '02_trajectory', provenance=provenance)
    plt.close(fig)

    fig, ax = new_figure(content='moderate', height_cm=8.6)
    for i, name in enumerate(names):
        x, y = ecdf(np.linalg.norm(errors[name], axis=1))
        # Include zero probability before the minimum and one after the maximum.
        ax.step(np.r_[0, x], np.r_[0, y], where='post', color=COLORS[i], linestyle=LINESTYLES[i], label=name)
    ax.set(xlim=(0, None), ylim=(0, 1.01),
           xlabel='Horizontal error / m' if en else '水平误差 / m',
           ylabel='Cumulative probability / %' if en else '累计概率 / %',
           title='Error CDF (synthetic)' if en else '水平误差 CDF（模拟数据）')
    ax.yaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=0))
    ax.yaxis.set_major_locator(MaxNLocator(5))
    ax.xaxis.set_major_locator(MaxNLocator(6))
    ax.legend(loc='lower right')
    export_figure(fig, args.output / '03_error_cdf', provenance={**provenance, 'CDF': 'exact empirical step; no smoothing'})
    plt.close(fig)

    fig, ax = new_figure()  # A simple single curve fits the compact 84 mm width.
    ax.plot(t, np.linalg.norm(errors[names[-1]], axis=1), color=COLORS[2])
    ax.set(xlim=(0, 180), ylim=(0, None), xlabel='Time / s' if en else '时间 / s',
           ylabel='Error / m' if en else '水平误差 / m',
           title='Fusion error (synthetic)' if en else '融合误差（模拟）')
    ax.xaxis.set_major_locator(MaxNLocator(4))
    ax.yaxis.set_major_locator(MaxNLocator(4))
    export_figure(fig, args.output / '04_compact_error', provenance=provenance)
    plt.close(fig)
    print(f'Synthetic examples saved: {args.output.resolve()}')


if __name__ == '__main__':
    main()
