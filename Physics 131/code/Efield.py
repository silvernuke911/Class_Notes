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

# Constants
q = 1.0
e0 = 1.0
k = 1 / (4 * np.pi * e0)

# Grid
x = np.linspace(-5, 5, 25)
y = np.linspace(-5, 5, 25)
X, Y = np.meshgrid(x, y)

# Avoid singularities at origin
epsilon = 1e-12
r = np.sqrt(X**2 + Y**2 + epsilon**2)

# rhat (unit vector field) = (x/r, y/r)
rhat = np.array([X / r,   # rhat_x = x/r
                 Y / r])  # rhat_y = y/r

# E = (1/4πe₀) * q * rhat / r^2
E = k * q / r**2 * rhat 

# Extract components
Ex = E[0, :, :]
Ey = E[1, :, :]

# Magnitude for coloring
magnitude = np.sqrt(Ex**2 + Ey**2)

# Create figure
fig, ax = plt.subplots(figsize=(2, 2), dpi = 300)

# Streamplot with inferno colormap
stream = ax.streamplot(X, Y, Ex, Ey, 
                       color=magnitude,
                       cmap='inferno',
                       linewidth=1.5,
                       density=0.5,
                       arrowsize=1,
                       arrowstyle='->')

# No colorbar

# Equal aspect and limits
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Grid and labels
# ax.grid(True, alpha=0.3, linestyle='--')
ax.grid()
# ax.set_xlabel('$x$', fontsize=12)
# ax.set_ylabel('$y$', fontsize=12)
ax.set_xticks([])
ax.set_yticks([])
# Mark the charge
ax.plot(0, 0, 'ro', markersize=6)
ax.text(0.3, 0.3, '+$q$', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig("efield.pdf")

# Print shapes to verify
print(f"rhat shape: {rhat.shape}")  # (2, Ny, Nx)
print(f"E shape: {E.shape}")        # (2, Ny, Nx)
print(f"r shape: {r.shape}")        # (Ny, Nx)


#=====================================
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
q = 1.0
e0 = 0.01
k = 1 / (4 * np.pi * e0)

def electric_field_2d(state, t):
    """Compute E at position (x, y)"""
    x, y = state
    r = np.sqrt(x**2 + y**2)
    if r < 1e-10:
        return [0, 0]
    # E = k*q*rhat/r^2
    Ex = k * q * x / r**3
    Ey = k * q * y / r**3
    return [Ex, Ey]

def trace_field_line(start_point, steps=1000, ds=0.01):
    """Trace a field line from start_point"""
    t = np.linspace(0, steps*ds, steps)
    # Integrate in both directions
    pos_forward = odeint(electric_field_2d, start_point, t)
    pos_backward = odeint(electric_field_2d, start_point, -t)
    # Combine (reverse backward)
    pos_backward = pos_backward[::-1]
    return np.vstack([pos_backward[:-1], pos_forward])

def add_arrows_to_line(line, ax, n_arrows=3, arrow_length=0.3, color='k'):
    """Add arrows along a field line"""
    # Select evenly spaced points along the line
    indices = np.linspace(0, len(line)-1, n_arrows+2, dtype=int)[1:-1]
    
    for idx in indices:
        # Get position and direction
        x, y = line[idx]
        
        # Compute electric field direction at this point
        Ex, Ey = electric_field_2d([x, y], 0)
        magnitude = np.sqrt(Ex**2 + Ey**2)
        if magnitude > 0:
            # Normalize
            Ex = Ex / magnitude
            Ey = Ey / magnitude
            # Add arrow
            ax.arrow(x, y, Ex*arrow_length, Ey*arrow_length, 
                    head_width=0.15, head_length=0.15, 
                    fc=color, ec=color, 
                    linewidth=1.0, length_includes_head=True)

# Create figure
fig, ax = plt.subplots(figsize=(2, 2), dpi=300)

# Define starting points for field lines (around the charge)
num_lines = 16
angles = np.linspace(0, 2*np.pi, num_lines, endpoint=False)
radius = 0.3  # Start just outside the charge
start_points = np.array([[radius*np.cos(th), radius*np.sin(th)] for th in angles])

# Trace and plot each field line with arrows
for start in start_points:
    line = trace_field_line(start, steps=2000, ds=0.02)
    ax.plot(line[:, 0], line[:, 1], linewidth=1.5, color='k')
    # Add 2 arrows per line
    add_arrows_to_line(line, ax, n_arrows=2, arrow_length=0.3, color='k')

# Equal aspect and limits
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xticks([])
ax.set_yticks([])
ax.grid()

# Mark the charge
ax.plot(0, 0, 'ro', markersize=6)
ax.text(0.3, 0.3, '+$q$', fontsize=12)

plt.tight_layout()
plt.savefig("Efieldline.pdf")
