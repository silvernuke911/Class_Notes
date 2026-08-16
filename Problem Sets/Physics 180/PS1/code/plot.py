import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
# for aesthetic plots
def science_plot(fontsize=11, scistyle=True, show_latex=True):
    # Default settings (applied to both 2D and 3D)
    if scistyle:
        import scienceplots
        plt.style.use(['science', 'grid', 'notebook'])

    if show_latex:
        plt.rcParams.update({
            # LaTeX Use
            'text.usetex': True,      # Use LaTeX for text rendering
            'font.family': 'serif',   # Set font family to serif
        })

    plt.rcParams.update({
        # Font sizes
        'font.size': fontsize,         # General font size
        'axes.titlesize': fontsize,    # Font size of the axes title
        'axes.labelsize': fontsize,    # Font size of the axes labels
        'xtick.labelsize': fontsize,   # Font size of the x-axis tick labels
        'ytick.labelsize': fontsize,   # Font size of the y-axis tick labels
        'legend.fontsize': fontsize,   # Font size of the legend
        'figure.titlesize': fontsize,  # Font size of the figure title

        # Legend
        'legend.fancybox': False,      # Disable the fancy box for legend
        'legend.edgecolor': 'k',       # Set legend border color to black
    })

    # # Grid settings
    # "grid.linestyle": "--",
    # "grid.color": "gray",
    # "grid.linewidth": 1,
    # "axes.grid": True,

    # # Minor grid (default, but may be overridden for 3D)
    # "xtick.minor.visible": True,
    # "ytick.minor.visible": True,

    # # Tick settings (both major & minor)
    # "xtick.direction": "in",
    # "ytick.direction": "in",
    # "xtick.top": True,
    # "xtick.bottom": True,
    # "ytick.left": True,
    # "ytick.right": True,

    # 'colorbar.ticks.direction': 'out',

    # # Major ticks
    # "xtick.major.width": 1,
    # "ytick.major.width": 1,
    # "xtick.major.size": 5,
    # "ytick.major.size": 5,

    # # Minor ticks
    # "xtick.minor.width": 1,
    # "ytick.minor.width": 1,
    # "xtick.minor.size": 2.5,
    # "ytick.minor.size": 2.5,

    # # Spine (border) width
    # "axes.linewidth": 1
science_plot()


# SEMF coefficients from [1]
a1 = 15.56  # MeV
a2 = 17.23
a3 = 0.697
a4 = 93.14
a5 = 12.00

def Z(A):
    return (a4 * A) / (2 * (a3 * A**(2/3) + a4))

def B(A):
    volume  =   a1 * A
    surface = - a2 * A**(2/3)
    coloumb = - a3 * Z(A)**2 / A**(1/3)
    assym   = - a4 * (Z(A) - A/2)**2 / A
    pairing = 0
    return volume + surface + coloumb + assym + pairing

A = np.linspace(0,250,1000)

BA = B(A) / A

BA62 = B(61.665)/61.665 
print(BA62)

data = pd.read_csv("stable_nuclides_AME2020.csv")
A_dat = data["A"]
BA_dat = data["binding_energy_per_nucleon_MeV"] 

plt.figure(figsize=(5, 3), dpi=300)
plt.scatter(61.665, BA62, color='b', s=10, zorder=3)
plt.plot(A, BA, 'r-', lw=1, label="SEMF plot", zorder=2)
plt.scatter(A_dat, BA_dat, color='k', s=2, label="Actual data", zorder=1)
plt.xlim(A.min(), 210)
plt.ylim(0, 10)
plt.xlabel("$A$")
plt.ylabel("$B/A$ [MeV]")
plt.legend(loc="lower right", fontsize = 9)

# Add annotation with arrow
plt.annotate(
    r'Peak at $A=62$, $Z = 27 \to \text{Ni}^{62}$',  # Text label
    xy=(61.665, BA62),              # Point to point to (blue dot)
    xytext=(85, 6.5),               # Position of text (adjust these values)
    arrowprops=dict(
        arrowstyle='->',            # Arrow style
        color='black',              # Arrow color
        lw=1,                     # Line width
    ),
    fontsize=8,
    ha='center',                   # Horizontal alignment
    bbox=dict(
        boxstyle='square,pad=0.3',   
        facecolor='white',
        edgecolor='black',
        alpha=0.9
    )
)

plt.savefig("BAplot.pdf")
print("Plot saved")
