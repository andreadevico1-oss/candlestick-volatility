import matplotlib.pyplot as plt

C_MAIN = "#65b5ff"
C_ACCENT = "#f7b65a"
C_MUTED = "#9AA0A6"
C_FOURTH = "#d79af5"
C_GREEN = "#55d5b0"

C_SERIES = [
    C_MAIN,
    C_GREEN,
    C_ACCENT,
    C_FOURTH,
    C_MUTED,
]

def apply_style():
    'Setting the dark theme for the project charts'
    plt.style.use('dark_background')

    plt.rcParams.update({
        "figure.figsize": (12, 5),
        "figure.facecolor": "#0a0a0a",
        "axes.facecolor": "#0a0a0a",
        "savefig.facecolor": "#0a0a0a",
        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "axes.grid": True,
        "grid.alpha": 0.2,
        "legend.frameon": False,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.prop_cycle": plt.cycler(color=C_SERIES),
    })