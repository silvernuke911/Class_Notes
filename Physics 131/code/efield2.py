import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
# for aesthetic plots
def science_plot(fontsize=9, scistyle=True, show_latex=True):
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

def electric_field(x, y, charges):
    """
    Calculate electric field at (x,y) due to multiple charges
    charges: list of (q, x0, y0) tuples
    """
    Ex = np.zeros_like(x)
    Ey = np.zeros_like(y)
    
    for q, x0, y0 in charges:
        # Distance vector components
        dx = x - x0
        dy = y - y0
        # Distance squared
        r2 = dx**2 + dy**2
        # Avoid division by zero at charge locations
        r2 = np.maximum(r2, 1e-12)
        # Coulomb's law: E = k*q/r^2 * r_hat
        # Using k = 1 for simplicity
        Ex += q * dx / r2**1.5
        Ey += q * dy / r2**1.5
    
    return Ex, Ey

plt.figure(figsize = (1.75, 1.75),dpi = 300)

# Define the grid
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Figure 1 (left): Charges at x = +1 and x = -1 with q = +1 and q = -1
charges = [(1, 1, 0), (-1, -1, 0)]  # (charge, x_position, y_position)
Ex, Ey = electric_field(X, Y, charges)

plt.streamplot(X, Y, Ex, Ey, 
               color = np.log(np.sqrt(Ex**2 + Ey**2)+1),
               cmap = 'inferno',
               linewidth = 0.5,
               density = 0.8,
               zorder = 1,
               arrowsize = 0.5
               )
plt.scatter(1,0,color='b',s=25,zorder = 3)
plt.annotate(
        "$+$",
        xy = [1,0],
        ha='center',
        va='center',
        zorder = 3,
        fontsize= 8
        )
plt.scatter(-1,0,color='r',s=25,zorder = 3)
plt.annotate(
        "$-$",
        xy = [-1,0],
        ha='center',
        va='center',
        zorder = 3,
        fontsize= 8
        )
plt.grid(False)
plt.xticks([])
plt.yticks([])
# plt.axis(False)
plt.tight_layout()
plt.savefig(r"..\images\oppositecharges.pdf")

plt.figure(figsize = (1.75, 1.75),dpi = 300)

# Define the grid
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Figure 1 (left): Charges at x = +1 and x = -1 with q = +1 and q = -1
charges = [(1, 1, 0), (1, -1, 0)]  # (charge, x_position, y_position)
Ex, Ey = electric_field(X, Y, charges)

plt.streamplot(X, Y, Ex, Ey, 
               color = np.log(np.sqrt(Ex**2 + Ey**2)+1),
               cmap = 'inferno',
               linewidth = 0.5,
               density = 0.8,
               zorder = 1,
               arrowsize = 0.5
               )
plt.scatter(1,0,color='b',s=25,zorder = 3)
plt.annotate(
        "$+$",
        xy = [1,0],
        ha='center',
        va='center',
        zorder = 3,
        fontsize= 8
        )
plt.scatter(-1,0,color='b',s=25,zorder = 3)
plt.annotate(
        "$+$",
        xy = [-1,0],
        ha='center',
        va='center',
        zorder = 3,
        fontsize= 8
        )
plt.grid(False)
plt.xticks([])
plt.yticks([])
# plt.axis(False)
plt.tight_layout()
plt.savefig(r"..\images\equalcharges.pdf")

# # Create figure with two subplots
# fig, ax = plt.subplots(1, 2, figsize=(12, 5))


# # Plot streamlines for figure 1
# strm1 = ax[0].streamplot(X, Y, Ex1, Ey1, 
#                          color=np.log(np.sqrt(Ex1**2 + Ey1**2) + 1),
#                          cmap='viridis', linewidth=1.5, density=1.2)
# ax[0].set_xlabel('x')
# ax[0].set_ylabel('y')
# ax[0].set_aspect('equal')
# ax[0].grid(True, alpha=0.3)
# # Mark charge positions
# ax[0].scatter([1, -1], [0, 0], color=['red', 'blue'], s=100, zorder=5)
# ax[0].text(1.1, 0.1, '+q', fontsize=12, color='red')
# ax[0].text(-1.1, 0.1, '-q', fontsize=12, color='blue')
# ax[0].set_xlim(-3, 3)
# ax[0].set_ylim(-3, 3)

# # Figure 2 (right): Charges at x = +1 and x = -1 with q = +1 and q = +1
# charges2 = [(1, 1, 0), (1, -1, 0)]  # (charge, x_position, y_position)
# Ex2, Ey2 = electric_field(X, Y, charges2)

# # Plot streamlines for figure 2
# strm2 = ax[1].streamplot(X, Y, Ex2, Ey2,
#                          color=np.log(np.sqrt(Ex2**2 + Ey2**2) + 1),
#                          cmap='viridis', linewidth=1.5, density=1.2)
# ax[1].set_title('Charges: +q at x=1, +q at x=-1')
# ax[1].set_xlabel('x')
# ax[1].set_ylabel('y')
# ax[1].set_aspect('equal')
# ax[1].grid(True, alpha=0.3)
# # Mark charge positions
# ax[1].scatter([1, -1], [0, 0], color='red', s=100, zorder=5)
# ax[1].text(1.1, 0.1, '+q', fontsize=12, color='red')
# ax[1].text(-1.1, 0.1, '+q', fontsize=12, color='red')
# ax[1].set_xlim(-3, 3)
# ax[1].set_ylim(-3, 3)

# # Add colorbar for field strength
# plt.colorbar(strm1.lines, ax=ax, label='Log(Field Strength)')

# plt.tight_layout()
# plt.show()
