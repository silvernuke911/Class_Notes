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

# # -- scalarfield
# x = y = np.linspace(-np.pi, np.pi, 200)
# X, Y = np.meshgrid(x, y, indexing='ij')
# F = np.sin(X) * np.sin(Y)

# plt.figure(figsize=(2.5, 2.5), dpi=300)
# im = plt.imshow(F.T, extent=[-np.pi, np.pi, -np.pi, np.pi], 
#                 cmap='inferno', origin='lower')
# plt.grid(False)
# plt.xlabel(r'$x$', fontsize=9)
# plt.ylabel(r'$y$', fontsize=9)

# # Colorbar with same height as plot box
# # cbar = plt.colorbar(im, shrink=1.0, fraction=0.046, pad=0.04)
# # cbar.ax.tick_params(labelsize=9)

# # Add ticks to colorbar
# # cbar.set_ticks([-0.5, 0, 0.5])
# # Or for automatic ticks:
# # cbar.ax.locator_params(nbins=5)

# # Set tick parameters for axes
# # plt.tick_params(axis='both', which='major', labelsize=9)

# plt.savefig(r"..\images\scalarfield.pdf", bbox_inches='tight')
# print("Scalar field image saved")

# # -- vectorfield

# x = np.linspace(-np.pi, np.pi, 200)
# y = np.linspace(-np.pi, np.pi, 200)
# X2, Y2 = np.meshgrid(x, y)
# Z = X2 + 1j*Y2

# epsilon = 1e-8
# F2 = 1j / (Z**2 + epsilon)

# Ex = np.real(F2)
# Ey = -np.imag(F2)
# magnitude = np.sqrt(Ex**2 + Ey**2)
# mmax = 10
# magnitude[magnitude > mmax] = mmax

# plt.figure(figsize = (2.5,2.5), dpi=300)
# stream = plt.streamplot(X2, Y2, Ex, Ey, color=magnitude, cmap='inferno',
#                         density=2, linewidth=1, arrowsize=0.5)
# plt.xlabel(r'$x$')
# plt.ylabel(r'$y$')
# plt.grid(False)
# plt.gca().set_aspect('equal')
# plt.savefig(r"..\images\vectorfield.pdf")
# print("Vector field image saved")

# # -- Scalar field and gradient
# # Create data
# x = y = np.linspace(-np.pi, np.pi, 200)
# X, Y = np.meshgrid(x, y, indexing='xy')  # Use 'xy' for streamplot compatibility
# F = np.sin(X) * 2 * np.sin(Y)  # Scalar field φ

# # Compute gradient 
# Fx = np.gradient(F, x, axis=1)  # ∂φ/∂x
# Fy = np.gradient(F, y, axis=0)  # ∂φ/∂y

# # Create figure with 2 subplots
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3), dpi=300)

# # First plot: Scalar field 
# im1 = ax1.imshow(F, extent=[-np.pi, np.pi, -np.pi, np.pi], 
#                  cmap='inferno', origin='lower')
# ax1.grid(False)
# ax1.set_xlabel(r'$x$')
# ax1.set_ylabel(r'$y$')
# ax1.set_title(r'$\phi = \sin(x)\cdot 2\sin(y)$')
# ax1.set_xlim(-np.pi, np.pi)
# ax1.set_ylim(-np.pi, np.pi)
# # ax1.tick_params(axis='both', which='major', direction='out')
# # ax1.tick_params(axis='both', which='minor', direction='out')
# ax1.set_xticks([-3,-2,-1,0,1,2,3])
# ax1.set_yticks([-3,-2,-1,0,1,2,3])
# ax1.set_aspect('equal')

# # Second plot: Gradient field 
# magnitude = np.sqrt(Fx**2 + Fy**2)
# stream = ax2.streamplot(X, Y, Fx, Fy, color=magnitude, cmap='inferno',
#                         density=2, linewidth=1, arrowsize=0.8)
# ax2.grid(False)
# ax2.set_xlabel(r'$x$')
# ax2.set_ylabel(r'$y$')
# ax2.set_title(r'$\nabla \phi$')
# ax2.set_xlim(-np.pi, np.pi)
# ax2.set_ylim(-np.pi, np.pi)
# ax2.set_xticks([-3,-2,-1,0,1,2,3])
# ax2.set_yticks([-3,-2,-1,0,1,2,3])
# ax2.set_aspect('equal')

# # Adjust layout and show
# plt.tight_layout()
# plt.savefig(r"..\images\gradient.pdf")
# print("Gradient field image saved")

# -- Divergence
x = y = np.linspace(-2,2,200)
X,Y = np.meshgrid(x,y)
R = np.sqrt(X*X+Y*Y)

eps=1e-12
Fpos = -1/(R**2+eps)
Fneg =  1/(R**2+eps)

Fposx = np.gradient(Fpos,x, edge_order = 2, axis=1)
Fposy = np.gradient(Fpos,y, edge_order = 2, axis=0)
Fnegx = np.gradient(Fneg,x, edge_order = 2, axis=1)
Fnegy = np.gradient(Fneg,y, edge_order = 2, axis=0)

vmin,vmax = 0,50
magpos = np.sqrt(Fposx**2+Fposy**2)
magpos[magpos>vmax]=vmax
magneg = np.sqrt(Fnegx**2+Fnegy**2)
magneg[magneg>vmax]=vmax
fig, ax = plt.subplots(1,2, figsize = (6,3),dpi=300)
ax[0].streamplot(X,Y,Fposx,Fposy,color=magpos, cmap='inferno', density=1.5, linewidth=1, arrowsize=0.8)
ax[1].streamplot(X,Y,Fnegx,Fnegy,color=magneg, cmap='inferno', density=1.5, linewidth=1, arrowsize=0.8)
ax[0].set_title('Positive divergence (source)')
ax[1].set_title('Negative divergence  (sink) ')
for axs in ax:
    axs.set_xlabel(r'$x$')
    axs.set_ylabel(r'$y$')
    axs.set_xticks(np.arange(-2,2.5,1))
    axs.set_yticks(np.arange(-2,2.5,1))
    axs.set_xlim(x.min(), x.max())
    axs.set_ylim(y.min(), y.max())
    axs.set_aspect('equal')
    axs.grid(False)
plt.tight_layout()
plt.savefig(r"..\images\divergence.pdf")
print("Divergence field image saved")
# -- curl
x = y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)
R = np.sqrt(X*X + Y*Y)

eps = 1e-12

# True 1/r^2 magnitude decay for tangential fields
# Unit tangent vector components
Fpos_x = -Y / (R + eps)
Fpos_y = X / (R + eps)

Fneg_x = Y / (R + eps)  
Fneg_y = -X / (R + eps)

# # Apply 1/r^2 magnitude scaling
magnitude_factor = 1 / (R**2 + eps)
Fpos_x *= magnitude_factor
Fpos_y *= magnitude_factor
Fneg_x *= magnitude_factor  
Fneg_y *= magnitude_factor

vmin, vmax = 0, 20
magpos = np.sqrt(Fpos_x**2 + Fpos_y**2)
magpos[magpos > vmax] = vmax
magneg = np.sqrt(Fneg_x**2 + Fneg_y**2)
magneg[magneg > vmax] = vmax

fig, ax = plt.subplots(1, 2, figsize=(6, 3), dpi=300)
ax[0].streamplot(X, Y, Fpos_x, Fpos_y, color=magpos, cmap='inferno', 
                 density=1.5, linewidth=1, arrowsize=0.8)
ax[1].streamplot(X, Y, Fneg_x, Fneg_y, color=magneg, cmap='inferno', 
                 density=1.5, linewidth=1, arrowsize=0.8)
ax[0].set_title('Positive curl')
ax[1].set_title('Negative curl')
for axs in ax:
    axs.set_xlabel(r'$x$')
    axs.set_ylabel(r'$y$')
    axs.set_xlim(x.min(), x.max())
    axs.set_ylim(y.min(), y.max())
    axs.set_xticks(np.arange(-2,2.5,1))
    axs.set_yticks(np.arange(-2,2.5,1))
    axs.set_aspect('equal')
    axs.grid(False)
plt.tight_layout()
plt.savefig(r"..\images\curl.pdf")
print("Curl field image saved")

# -- Laplacian
from mpl_toolkits.axes_grid1 import make_axes_locatable

# Create data
x = y = np.linspace(-np.pi, np.pi, 200)
X, Y = np.meshgrid(x, y, indexing='xy')
F = np.sin(X) * np.sin(Y)

# Compute gradient ∇φ
Fx = np.gradient(F, x, axis=1)
Fy = np.gradient(F, y, axis=0)

# Compute Laplacian ∇²φ
Fxx = np.gradient(Fx, x, axis=1)
Fyy = np.gradient(Fy, y, axis=0)
laplacian = Fxx + Fyy

# Create figure with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 3), dpi=300)

# First plot: Scalar field φ
im1 = ax1.imshow(F, extent=[-np.pi, np.pi, -np.pi, np.pi], 
                 cmap='inferno', origin='lower', vmin=-2, vmax=2)
ax1.grid(False)
ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$y$')
ax1.set_title(r'$\phi = \sin(x)\cdot \sin(y)$')
# ax1.tick_params(axis='both', which='major', direction='out')
# ax1.tick_params(axis='both', which='minor', direction='out')
ax1.set_aspect('equal')

# Colorbar for first plot - matches y-axis height, on the right edge
divider1 = make_axes_locatable(ax1)
cax1 = divider1.append_axes("right", size="5%", pad=0.05)
cbar1 = plt.colorbar(im1, cax=cax1)
cbar1.ax.tick_params(labelsize=9)

# Second plot: Laplacian ∇²φ
im2 = ax2.imshow(laplacian, extent=[-np.pi, np.pi, -np.pi, np.pi], 
                 cmap='inferno', origin='lower', vmin=-2, vmax=2)
ax2.grid(False)
ax2.set_xlabel(r'$x$')
ax2.set_ylabel(r'$y$')
ax2.set_title(r'$\nabla^2 \phi$')
# ax2.tick_params(axis='both', which='major', direction='out')
# ax2.tick_params(axis='both', which='minor', direction='out')
ax2.set_aspect('equal')

# Colorbar for second plot - matches y-axis height, on the right edge
divider2 = make_axes_locatable(ax2)
cax2 = divider2.append_axes("right", size="5%", pad=0.05)
cbar2 = plt.colorbar(im2, cax=cax2)
cbar2.ax.tick_params(labelsize=9)

# Adjust layout and show
plt.tight_layout()
plt.savefig(r"..\images\lpc.pdf")
print("Laplacian field image saved")
