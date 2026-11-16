"""Shared scientific-figure defaults. Physical dimensions include all decorations."""
from __future__ import annotations

from dataclasses import dataclass, asdict

import importlib.metadata
import json
import math
from pathlib import Path
import warnings

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.text import Text
from cycler import cycler
import numpy as np
import scienceplots  # noqa: F401: registers the SciencePlots styles

MAX_WIDTH_CM = 15.9
MAX_HEIGHT_CM = 24.5
SINGLE_WIDTHS_CM = {'simple': 8.4, 'moderate': 12.9, 'dense': MAX_WIDTH_CM}
COLORS = ('#0072B2', '#D55E00', '#009E73', '#CC79A7', '#E69F00', '#555555')
LINESTYLES = ('-', '--', '-.', ':', '-', '--')


@dataclass(frozen=True)
class StyleConfig:
    language: str = 'zh'
    western_font: str | None = None
    chinese_font: str = 'SimSun'
    title_pt: float = 13
    text_pt: float = 11
    simple_width_cm: float = 8.4
    moderate_width_cm: float = 12.9
    max_width_cm: float = 15.9
    max_height_cm: float = 24.5

    def __post_init__(self):
        if self.language not in ('zh', 'en'):
            raise ValueError("language must be 'zh' or 'en'.")
        for key in ('title_pt', 'text_pt', 'simple_width_cm', 'moderate_width_cm',
                    'max_width_cm', 'max_height_cm'):
            value = getattr(self, key)
            if not math.isfinite(value) or value <= 0:
                raise ValueError(f'{key} must be finite and positive.')
        for font in (self.western, self.chinese_font):
            if not isinstance(font, str) or not font.strip():
                raise ValueError('Font names must be nonempty strings.')

    @property
    def western(self):
        return self.western_font if self.western_font is not None else (
            'Arial' if self.language == 'en' else 'Times New Roman')


_ACTIVE_CONFIG = StyleConfig()


def check_fonts(language='zh', *, config=None) -> dict[str, str]:
    """Chinese/mixed: Times New Roman + SimSun; explicitly English: Arial."""
    if language not in ('zh', 'en'):
        raise ValueError("language must be 'zh' (default/mixed) or 'en' (English-only).")
    config = config or StyleConfig(language=language)
    paths = {}
    for name in ((config.western,) if config.language == 'en' else (config.western, config.chinese_font)):
        try:
            paths[name] = str(font_manager.findfont(name, fallback_to_default=False))
        except ValueError as exc:
            raise RuntimeError(f'Required font is missing: {name}. Install it before plotting.') from exc
    return paths


def apply_style(language=None, *, config=None) -> dict[str, str]:
    global _ACTIVE_CONFIG
    if config is not None and language is not None and language != config.language:
        raise ValueError('language conflicts with config.language.')
    config = config or StyleConfig(language=language or 'zh')
    fonts = check_fonts(config=config)
    western = config.western
    plt.style.use(['science', 'no-latex', 'grid'])
    mpl.rcParams.update({
        'font.family': list(fonts),
        'font.size': config.text_pt,
        'font.weight': 'normal',
        'axes.titlesize': config.title_pt,
        'figure.titlesize': config.title_pt,
        'axes.titleweight': 'normal',
        'figure.titleweight': 'normal',
        'figure.labelsize': config.text_pt,
        'axes.labelsize': config.text_pt,
        'axes.labelweight': 'normal',
        'xtick.labelsize': config.text_pt,
        'ytick.labelsize': config.text_pt,
        'legend.fontsize': config.text_pt,
        'legend.title_fontsize': config.text_pt,
        'text.usetex': False,
        'mathtext.fontset': 'custom',
        'mathtext.rm': western,
        'mathtext.it': western + ':italic',
        'mathtext.bf': western + ':bold',
        'mathtext.sf': western,
        'mathtext.tt': western,
        'mathtext.cal': western + ':italic',
        'mathtext.fallback': 'stix',
        'axes.unicode_minus': False,
        'figure.figsize': (config.simple_width_cm / 2.54, 6.3 / 2.54),
        'figure.dpi': 120,
        'savefig.dpi': 240,
        'savefig.bbox': None,
        'savefig.facecolor': 'white',
        'figure.facecolor': 'white',
        'axes.facecolor': 'white',
        'pdf.fonttype': 42,
        'ps.fonttype': 42,
        'svg.fonttype': 'none',
        'axes.prop_cycle': cycler(color=COLORS) + cycler(linestyle=LINESTYLES),
        'lines.linewidth': 1.15,
        'lines.markersize': 4,
        'axes.linewidth': 0.7,
        'axes.edgecolor': '#333333',
        'axes.axisbelow': True,
        'axes.grid': True,
        'axes.grid.which': 'major',
        'grid.color': '#B0B0B0',
        'grid.alpha': 0.35,
        'grid.linewidth': 0.5,
        'grid.linestyle': '--',
        'xtick.direction': 'in',
        'ytick.direction': 'in',
        'xtick.top': False,
        'ytick.right': False,
        'xtick.minor.visible': False,
        'ytick.minor.visible': False,
        'legend.frameon': False,
        'legend.handlelength': 2.0,
        'legend.borderaxespad': 0.4,
        'axes.titlepad': 9,
        'axes.labelpad': 5,
        'figure.constrained_layout.use': True,
        'figure.constrained_layout.w_pad': 0.055,
        'figure.constrained_layout.h_pad': 0.055,
    })
    _ACTIVE_CONFIG = config
    return fonts


def _validate_size(width_cm, height_cm, allow_oversize=False, config=None):
    config = config or _ACTIVE_CONFIG
    if not all(math.isfinite(v) and v > 0 for v in (width_cm, height_cm)):
        raise ValueError('Figure dimensions must be finite and positive.')
    if not allow_oversize and (width_cm > config.max_width_cm + 1e-6 or height_cm > config.max_height_cm + 1e-6):
        raise ValueError(f'Configured limit is {config.max_width_cm} x {config.max_height_cm} cm. Split the figure or use an explicit user-requested size.')


def new_figure(nrows=1, ncols=1, *, content='simple', width_cm=None, height_cm=None, allow_oversize=False, **kwargs):
    """Single panel: 84/129 mm by content; groups/dense figures may use A4 width."""
    if content not in SINGLE_WIDTHS_CM:
        raise ValueError("content must be 'simple', 'moderate', or 'dense'.")
    config = _ACTIVE_CONFIG
    widths = {'simple': config.simple_width_cm, 'moderate': config.moderate_width_cm, 'dense': config.max_width_cm}
    group = nrows * ncols > 1
    width_cm = (config.max_width_cm if group else widths[content]) if width_cm is None else float(width_cm)
    if height_cm is None:
        height_cm = (9.5 if nrows == 1 else 6.8 * nrows + 1.0) if group else max(6.3, width_cm * 0.65)
    else:
        height_cm = float(height_cm)
    _validate_size(width_cm, height_cm, allow_oversize)
    if any(k in kwargs for k in ('figsize', 'layout', 'constrained_layout')):
        raise ValueError('Use width_cm/height_cm; layout is constrained.')
    fig, axes = plt.subplots(nrows, ncols, figsize=(width_cm / 2.54, height_cm / 2.54),
                             layout='constrained', **kwargs)
    fig._sci_config = config
    fig._sci_rc = dict(mpl.rcParams)
    return fig, axes


def ecdf(values):
    """Exact step ECDF; caller must explicitly handle and document invalid samples."""
    values = np.asarray(values, dtype=float)
    if values.ndim != 1 or not values.size or not np.isfinite(values).all():
        raise ValueError('ECDF requires a nonempty finite 1D sample; document any filtering first.')
    ordered = np.sort(values)
    # Repeating the minimum creates the initial vertical jump from probability 0.
    return np.r_[ordered[0], ordered], np.r_[0.0, np.arange(1, values.size + 1) / values.size]


def _check_text(fig):
    """Check physical text extents; inspect the rendered figure for internal overlaps."""
    with warnings.catch_warnings():
        warnings.filterwarnings('error', message=r'Glyph .* missing from font.*')
        fig.canvas.draw()
    renderer = fig.canvas.get_renderer()
    boundary = fig.bbox
    suppressed_ticks = set()
    for ax in fig.axes:
        for axis in (ax.xaxis, ax.yaxis):
            transform = axis.get_transform()
            limits = sorted(transform.transform(axis.get_view_interval()))
            for tick in axis.get_major_ticks() + axis.get_minor_ticks():
                loc = float(transform.transform([tick.get_loc()])[0])
                if loc < limits[0] - 1e-8 or loc > limits[1] + 1e-8:
                    suppressed_ticks.update((id(tick.label1), id(tick.label2)))
    outside = []
    for artist in fig.findobj(match=Text):
        if not artist.get_visible() or not artist.get_text().strip():
            continue
        # Tick labels outside axis limits are present but are not actually drawn.
        if id(artist) in suppressed_ticks:
            continue
        bbox = artist.get_window_extent(renderer)
        if (bbox.x0 < boundary.x0 - 1 or bbox.y0 < boundary.y0 - 1 or
                bbox.x1 > boundary.x1 + 1 or bbox.y1 > boundary.y1 + 1):
            outside.append(artist.get_text())
    if outside:
        raise ValueError(f'Text extends outside the canvas; fix layout: {outside[:6]}')


def export_figure(fig, stem, *, provenance=None, dpi=240, formats=('svg', 'pdf', 'png'), allow_oversize=False):
    """Export without tight cropping, then write a small reproducibility manifest."""
    width_cm, height_cm = (float(x) * 2.54 for x in fig.get_size_inches())
    config = getattr(fig, '_sci_config', _ACTIVE_CONFIG)
    _validate_size(width_cm, height_cm, allow_oversize, config=config)
    language = config.language
    fonts = check_fonts(config=config)
    with mpl.rc_context(getattr(fig, '_sci_rc', {})):
        _check_text(fig)
    stem = Path(stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    formats = tuple(formats)
    if not formats or any(f not in ('svg', 'pdf', 'png') for f in formats):
        raise ValueError('Supported formats: svg, pdf, png.')
    paths = []
    for fmt in formats:
        target = Path(str(stem) + '.' + fmt)
        with mpl.rc_context({**getattr(fig, '_sci_rc', {}), 'savefig.bbox': None}):
            fig.savefig(target, format=fmt, dpi=dpi, bbox_inches=None, facecolor='white')
        paths.append(str(target.resolve()))
    manifest = {
        'size_cm': [round(width_cm, 5), round(height_cm, 5)],
        'style_defaults': {'title_pt': config.title_pt, 'other_text_pt': config.text_pt}, 'png_dpi': dpi,
        'style_config': asdict(config),
        'font_files': fonts,
        'language_mode': language,
        'svg_text': 'editable; destination computer must have ' + ' and '.join(fonts),
        'versions': {name: importlib.metadata.version(name) for name in ('matplotlib', 'SciencePlots', 'numpy')},
        'files': paths,
        'provenance': provenance or {},
    }
    Path(str(stem) + '.figure.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
    return paths
