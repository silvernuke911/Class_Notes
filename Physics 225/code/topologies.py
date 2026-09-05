import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'

fsize = 9
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": fsize,
    "axes.titlesize": fsize,
    "axes.labelsize": fsize,
    "xtick.labelsize": fsize,
    "ytick.labelsize": fsize,
    "legend.fontsize": fsize,
})


fig1 = r'..\images\prerelativityspacetime.pdf'
plt.figure(figsize=(3,3), dpi=300)
plt.gca().set_aspect('equal')

time = np.array([0, 2])
dt   = 0.3
t    = np.arange(time[0]+dt, time[1], dt)

origin = np.array([0, 0])

square = np.array([
    [0,0],
    [1,0],
    [1,1],
    [0,1],
    [0,0]
])

# Arrow
plt.arrow(origin[0], origin[1], time[0], time[1],
          linewidth=1, head_width=0.04, head_length=0.08,
          color='k', length_includes_head=True)

for idx, ti in enumerate(t):  # Changed 'i' to 'idx'
    theta = np.deg2rad(-30)  # azimuth
    phi   = np.deg2rad(20)  # elevation

    az_transform = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    el_transform = np.array([
        [1, 0],
        [0, np.sin(phi)]
    ])
    transform = el_transform @ az_transform
    translation = np.array([[0], [ti]])  # Shape (2, 1)

    # Square
    frame1 = transform @ square.T + translation

    # Grid
    grid_size = 5
    x = np.linspace(0, 1, grid_size)
    y = np.linspace(0, 1, grid_size)
    grid_points = np.array([[xi, yi] for xi in x for yi in y]).T
    transformed_grid = transform @ grid_points + translation

    # Plot grid lines (changed inner loop variable to 'j')
    for j in range(grid_size):
        # Vertical lines
        x_vals = transformed_grid[0, j*grid_size:(j+1)*grid_size]
        y_vals = transformed_grid[1, j*grid_size:(j+1)*grid_size]
        plt.plot(x_vals, y_vals, color='gray', lw=0.5, linestyle=':')
        
        # Horizontal lines
        x_vals = transformed_grid[0, j::grid_size]
        y_vals = transformed_grid[1, j::grid_size]
        plt.plot(x_vals, y_vals, color='gray', lw=0.5, linestyle=':')

    # Square outline
    plt.plot(frame1[0], frame1[1], color='k', lw=1)

    if idx == 0:
        tlabel = r"$t$"
    elif idx == 1:
        tlabel = r"$t + dt$"
    else:
        tlabel = rf"$t + {idx}dt$"

    plt.annotate(
        tlabel,
        xy=(0, ti),
        xytext=(-0.1, ti),
        ha='right',
        va='center',
    )

    if idx == 0:
        rlabel = r"$\mathbb{R}^3(t)$"
    elif idx == 1:
        rlabel = r"$\mathbb{R}^3(t + dt)$"
    else:
        rlabel = rf"$\mathbb{{R}}^3(t + {idx}dt)$"  # Escaped braces for f-string

    plt.annotate(
        rlabel,
        xy=frame1.T[2] + [0.1,0],
        ha='left',
        va='center',
    )



plt.xlim(-0.1, 1.5)
# plt.ylim(-0.1, 2.5)  # Added ylim
plt.axis(False)
plt.tight_layout()
plt.savefig(fig1)
os.startfile(fig1)

fig2 = r'..\images\manifold_ex1.pdf'
plt.figure(figsize=(3,3), dpi=300)
plt.gca().set_aspect('equal')

theta = np.linspace(0,2*np.pi,1000)
sphere = np.array([
    np.cos(theta),
    np.sin(theta)
])

ang1 = np.deg2rad(35)
ang2 = np.deg2rad(45)

y1 = np.sin(ang1)
y2 = np.sin(ang2)

ellipse1 = np.array([
    np.sin(ang1) * np.cos(theta),
    np.sin(theta)
])


mask = (ellipse1[1] >= y1) & (ellipse1[1] <= y2) & (ellipse1[0] > 0)
ellipse1 = ellipse1[:, mask]

ellipse2 = np.array([
    np.sin(ang2) * np.cos(theta),
    np.sin(theta)
])
mask = (ellipse2[1] >= y1) & (ellipse2[1] <= y2) & (ellipse2[0] > 0)
ellipse2 = ellipse2[:, mask]

plt.plot([ellipse1[0].min(),ellipse2[0].min()], [y2,y2],'k-',lw=1)
plt.plot([ellipse1[0].max(),ellipse2[0].max()], [y1,y1],'k-',lw=1)

plt.plot(ellipse1[0],ellipse1[1],'k-',lw=1)
plt.plot(ellipse2[0],ellipse2[1],'k-',lw=1)

angs = np.arange(ang1, ang2, np.deg2rad(2))
scale = 2
# grid on an expanded part of the sphere manifold
for ang in angs:
    y3 = scale*y1
    y4 = scale*y2

    ellipse =scale* np.array([
        np.sin(ang) * np.cos(theta),
        np.sin(theta)
    ])
    mask = (ellipse[1] >= y3) & (ellipse[1] <= y4) & (ellipse[0] > 0)
    ellipse = ellipse[:, mask]
    plt.plot(ellipse[0],ellipse[1],'k-',lw=0.5)
    
    ys = scale * np.array([np.sin(ang),np.sin(ang)])
    x1 = scale * np.sin(ang1) * np.sqrt(
        1 - (ys / scale)**2
    )

    x2 = scale * np.sin(ang2) * np.sqrt(
        1 - (ys / scale)**2
    )

    plt.plot([x1, x2], [ys, ys], 'k-', lw=0.5)


plt.plot([scale*ellipse1[0].min(),scale*ellipse2[0].min()], [scale*y2,scale*y2],'k-',lw=1)
plt.plot([scale*ellipse1[0].max(),scale*ellipse2[0].max()], [scale*y1,scale*y1],'k-',lw=1)
plt.plot(scale*ellipse1[0],scale*ellipse1[1],'k-',lw=1)
plt.plot(scale*ellipse2[0],scale*ellipse2[1],'k-',lw=1)

plt.plot([ellipse1[0].min(), scale*ellipse1[0].min()], [ellipse1[1].max(), scale*ellipse1[1].max()], 'k-', lw=0.5)
plt.plot([ellipse1[0].max(), scale*ellipse1[0].max()], [ellipse1[1].min(), scale*ellipse1[1].min()], 'k-', lw=0.5)
plt.plot([ellipse2[0].min(), scale*ellipse2[0].min()], [ellipse2[1].max(), scale*ellipse2[1].max()], 'k-', lw=0.5)
plt.plot([ellipse2[0].max(), scale*ellipse2[0].max()], [ellipse2[1].min(), scale*ellipse2[1].min()], 'k-', lw=0.5)
plt.plot(sphere[0],sphere[1],'k-',lw=1)

plt.annotate(
    r"Manifold $\mathcal{M}$",
    [0,0],
    ha='center',
    va='center'
)
plt.annotate(
    r"Locally $\mathbb{R}^n$ part",
    [0.7,1.4],
    ha='right',
    va='center',
    fontsize=8
)
plt.axis(False)
plt.tight_layout()
plt.savefig(fig2)
os.startfile(fig2)



fig3 = r'..\images\preimage.pdf'

plt.figure(figsize=(3, 1), dpi=300)
plt.gca().set_aspect('equal')

sep = 3
theta = np.linspace(0, 2*np.pi, 500)


# ---------------------------------------------------------
# Blob function
# ---------------------------------------------------------

def blob(theta, scale=1, phase=0, a = 0.15, b = 0.10, c = 0.07):
    r = scale * (
        1
        + a * np.sin(2*theta + phase)
        + b * np.cos(3*theta - phase)
        + c * np.sin(5*theta + 0.5*phase)
    )

    return r*np.cos(theta), r*np.sin(theta)


# ---------------------------------------------------------
# Sets M and N
# ---------------------------------------------------------

# M
x, y = blob(theta, 1.0, 0)
plt.fill(
    x - sep, y,
    facecolor='white',
    linestyle = '-',
    edgecolor='k',
    linewidth=1
)

# N
x, y = blob(theta, 1.2, 1, a = 0.07, b = 0.1, c = 0.01)
plt.fill(
    x + sep, y,
    facecolor='white',
    edgecolor='k',
    linestyle = '-',
    linewidth=1
)


# ---------------------------------------------------------
# Sets W and O
# ---------------------------------------------------------

# W
x, y = blob(theta, 0.5, 2)

plt.fill(
    x - sep, y,
    facecolor='red',
    alpha=0.5,
    edgecolor='none'
)
plt.plot(x - sep, y, 'k--', lw=1)


# O
x, y = blob(theta, 0.5, 3, a=0.2, b=0.07, c=0.1)
plt.fill(
    0.5*x + sep + 0.1,
    y,
    facecolor='blue',
    alpha=0.5,
    edgecolor='none'
)

plt.plot(0.5*x + sep + 0.1, y, 'k--', lw=1)

# ---------------------------------------------------------
# Labels
# ---------------------------------------------------------

plt.annotate(
    "$M$",
    [-sep, 1.45],
    ha='center',
    va='center'
)

plt.annotate(
    "$N$",
    [sep, 1.45],
    ha='center',
    va='center'
)

plt.annotate(
    r"$\mathcal{W}$",
    [-sep - 0.5, -0.7],
    ha='center',
    va='center'
)

plt.annotate(
    r"$\mathcal{O}$",
    [sep + 0.7, 0],
    ha='center',
    va='center'
)


# ---------------------------------------------------------
# Arrows
# ---------------------------------------------------------

arrowsep = 0.1

plt.arrow(
    -sep,
    +arrowsep,
    +2*sep,
    0,
    color='k',
    linewidth=1,
    head_width=0.05,
    head_length=0.1,
    length_includes_head=True
)

plt.arrow(
    +sep,
    -arrowsep,
    -2*sep,
    0,
    color='k',
    linewidth=1,
    head_width=0.05,
    head_length=0.1,
    length_includes_head=True
)


# ---------------------------------------------------------
# Map labels
# ---------------------------------------------------------

plt.annotate(
    "$f$",
    [0, +arrowsep + 0.5],
    ha='center',
    va='center'
)

plt.annotate(
    "$f^{-1}$",
    [0, -arrowsep - 0.5],
    ha='center',
    va='center'
)


# ---------------------------------------------------------
# Figure formatting
# ---------------------------------------------------------

plt.ylim(-1.25, 1.5)
plt.axis(False)
plt.tight_layout()

plt.savefig(fig3)
os.startfile(fig3)


fig3 = r'..\images\charts.pdf'

plt.figure(figsize=(4, 3), dpi=300)
plt.gca().set_aspect('equal')


# =========================================================
# Manifold M
# =========================================================

theta = np.linspace(0, 2*np.pi, 500)

radius = 3

manifold = np.array([
    radius * np.cos(theta),
    radius * np.sin(theta)
])

plt.plot(
    manifold[0],
    manifold[1],
    'k-',
    lw=1
)

plt.annotate(
    r'$\mathcal{M}$',
    [-0.5, 0],
    ha='center',
    va='center'
)


# =========================================================
# Manifold O_1
# =========================================================

radius = 1
posM1 = [1,1.5]
manifoldO1 = np.array([
    radius * np.cos(theta) + posM1[0],
    radius * np.sin(theta) + posM1[1]
])

plt.fill(
    manifoldO1[0],
    manifoldO1[1],
    facecolor='red',
    alpha = 0.5,
    edgecolor='w',
    linewidth=1
)

plt.plot(
    manifoldO1[0],
    manifoldO1[1],
    'k--',
    lw=0.75
)

plt.annotate(
    r'$\mathcal{O}_1$',
    posM1,
    ha='center',
    va='center'
)


# =========================================================
# Manifold O_2
# =========================================================

radius = 1.25
posM2 = [1.6,0]
manifoldO2 = np.array([
    radius * np.cos(theta) + posM2[0],
    radius * np.sin(theta) + posM2[1]
])

plt.fill(
    manifoldO2[0],
    manifoldO2[1],
    facecolor='blue',
    alpha = 0.5,
    edgecolor='w',
    linewidth=1
)
plt.plot(
    manifoldO2[0],
    manifoldO2[1],
    'k--',
    lw=0.75
)

plt.annotate(
    r'$\mathcal{O}_2$',
    posM2,
    ha='center',
    va='center'
)


# =========================================================
# Coordinate axes
# =========================================================

def draw_axis(
    pos,
    axisname,
    azimuth=-135,
    elevation=30,
    axislen=1
):

    # Convert degrees -> radians
    azimuth = np.deg2rad(azimuth)
    elevation = np.deg2rad(elevation)

    # Original coordinate axes
    ax1 = np.array([1, 0])
    ax2 = np.array([0, 1])
    ax3 = np.array([0, 1])

    # Azimuthal rotation
    az_transform = np.array([
        [np.cos(azimuth), -np.sin(azimuth)],
        [np.sin(azimuth),  np.cos(azimuth)]
    ])

    # Elevation projection
    el_transform = np.array([
        [1, 0],
        [0, np.sin(elevation)]
    ])

    # Transform axes
    ax1 = el_transform @ az_transform @ ax1
    ax2 = el_transform @ az_transform @ ax2
    ax3 = el_transform @ ax3

    axes = [ax1, ax2, ax3]
    labels = ['1', '2', 'n']

    for ax, label in zip(axes, labels):

        # Normalize so axislen is the actual arrow length
        ax = ax / np.linalg.norm(ax)

        plt.arrow(
            pos[0],
            pos[1],
            axislen * ax[0],
            axislen * ax[1],
            color='k',
            linewidth=1,
            head_width=0.05,
            head_length=0.1,
            length_includes_head=True
        )

        plt.annotate(
            rf'$\mathbf{{{axisname}}}_{{{label}}}$',
            [
                pos[0] + 1.3 * axislen * ax[0],
                pos[1] + 1.3 * axislen * ax[1]
            ],
            ha='center',
            va='center'
        )

axis1pos = [5.5,2]
draw_axis(
    axis1pos,
    'x',
    azimuth=-135,
    elevation=30,
    axislen=1
)
axis2pos = [5.5,-2]
draw_axis(
    axis2pos,
    'y',
    azimuth=-120,
    elevation=30,
    axislen=1
)
# ================================================
# Images
# ================================================

x, y = blob(theta, 0.5,0)
plt.fill(
    x + axis1pos[0], y + axis1pos[1],
    facecolor='red',
    alpha = 0.5,
    edgecolor='k',
    linewidth=1
)
plt.plot(x + axis1pos[0],y + axis1pos[1], 'k-',lw=1)

x, y = blob(theta, 0.6,1.5, 0.1, 0.2, 0.05)
plt.fill(
    0.9 * x + axis2pos[0], y + axis2pos[1],
    facecolor='blue',
    alpha = 0.5,
    edgecolor='k',
    linewidth=1
)
plt.plot(0.9 * x + axis2pos[0],y + axis2pos[1], 'k-',lw=1)

# ================================================
# Maps
# ================================================
Ox1_vec = np.array(axis1pos) - np.array(posM1)
Ox2_vec = np.array(axis2pos) - np.array(posM2)
plt.arrow(
    posM1[0] + Ox1_vec[0] * 0.2,
    posM1[1] + Ox1_vec[1] * 0.2,
    Ox1_vec[0] * 0.6,
    Ox1_vec[1] * 0.6,
    linewidth=1,
    head_width=0.05,
    head_length=0.1,
    color='k',
    length_includes_head=True
)
plt.arrow(
    posM2[0] + Ox2_vec[0] * 0.2,
    posM2[1] + Ox2_vec[1] * 0.2,
    Ox2_vec[0] * 0.6,
    Ox2_vec[1] * 0.6,
    linewidth=1,
    head_width=0.05,
    head_length=0.1,
    color='k',
    length_includes_head=True
)
plt.annotate(
    r"$\psi_1$",
    np.array(posM1) + Ox1_vec/2 + np.array([0,0.4]),
    ha='center',
    va='center'
)
plt.annotate(
    r"$\psi_2$",
    np.array(posM2) + Ox2_vec/2 + np.array([0,0.4]),
    ha='center',
    va='center'
)
plt.annotate(
    r"$\psi_1[\mathcal{O}_1]$",
    axis1pos + np.array([0,- 1]),
    ha='center',
    va='center'
)
plt.annotate(
    r"$\psi_2[\mathcal{O}_2]$",
    axis2pos + np.array([0,- 1.2]),
    ha='center',
    va='center'
)
# =========================================================
# Formatting
# =========================================================

plt.axis(False)
plt.tight_layout()

plt.savefig(fig3)
os.startfile(fig3)

fig3 = r'..\images\differential_manifolds.pdf'

plt.figure(figsize=(4, 3), dpi=300)
plt.gca().set_aspect('equal')


# =========================================================
# Manifold M
# =========================================================

theta = np.linspace(0, 2*np.pi, 500)

radius = 3

manifold = np.array([
    radius * np.cos(theta),
    radius * np.sin(theta)
])

plt.plot(
    manifold[0],
    manifold[1],
    'k-',
    lw=1
)

plt.annotate(
    r'$\mathcal{M}$',
    [-0.5, 0],
    ha='center',
    va='center'
)


# =========================================================
# Manifold O_1
# =========================================================

radius = 1
posM1 = [1,1.5]
manifoldO1 = np.array([
    radius * np.cos(theta) + posM1[0],
    radius * np.sin(theta) + posM1[1]
])

plt.fill(
    manifoldO1[0],
    manifoldO1[1],
    facecolor='red',
    alpha = 0.5,
    edgecolor='w',
    linewidth=1
)

plt.plot(
    manifoldO1[0],
    manifoldO1[1],
    'k--',
    lw=0.75
)

plt.annotate(
    r'$\mathcal{O}_1$',
    posM1,
    ha='center',
    va='center'
)


# =========================================================
# Manifold O_2
# =========================================================

radius = 1.25
posM2 = [1.6,0]
manifoldO2 = np.array([
    radius * np.cos(theta) + posM2[0],
    radius * np.sin(theta) + posM2[1]
])

plt.fill(
    manifoldO2[0],
    manifoldO2[1],
    facecolor='blue',
    alpha = 0.5,
    edgecolor='w',
    linewidth=1
)
plt.plot(
    manifoldO2[0],
    manifoldO2[1],
    'k--',
    lw=0.75
)

plt.annotate(
    r'$\mathcal{O}_2$',
    posM2,
    ha='center',
    va='center'
)


# =========================================================
# Coordinate axes
# =========================================================

def draw_axis(
    pos,
    axisname,
    azimuth=-135,
    elevation=30,
    axislen=1
):

    # Convert degrees -> radians
    azimuth = np.deg2rad(azimuth)
    elevation = np.deg2rad(elevation)

    # Original coordinate axes
    ax1 = np.array([1, 0])
    ax2 = np.array([0, 1])
    ax3 = np.array([0, 1])

    # Azimuthal rotation
    az_transform = np.array([
        [np.cos(azimuth), -np.sin(azimuth)],
        [np.sin(azimuth),  np.cos(azimuth)]
    ])

    # Elevation projection
    el_transform = np.array([
        [1, 0],
        [0, np.sin(elevation)]
    ])

    # Transform axes
    ax1 = el_transform @ az_transform @ ax1
    ax2 = el_transform @ az_transform @ ax2
    ax3 = el_transform @ ax3

    axes = [ax1, ax2, ax3]
    labels = ['1', '2', 'n']

    for ax, label in zip(axes, labels):

        # Normalize so axislen is the actual arrow length
        ax = ax / np.linalg.norm(ax)

        plt.arrow(
            pos[0],
            pos[1],
            axislen * ax[0],
            axislen * ax[1],
            color='k',
            linewidth=1,
            head_width=0.05,
            head_length=0.1,
            length_includes_head=True
        )

        plt.annotate(
            rf'$\mathbf{{{axisname}}}_{{{label}}}$',
            [
                pos[0] + 1.3 * axislen * ax[0],
                pos[1] + 1.3 * axislen * ax[1]
            ],
            ha='center',
            va='center'
        )

axis1pos = [5.5,3]
draw_axis(
    axis1pos,
    'x',
    azimuth=-135,
    elevation=30,
    axislen=1
)
axis2pos = [5.5,-2]
draw_axis(
    axis2pos,
    'y',
    azimuth=-120,
    elevation=30,
    axislen=1
)
# ================================================
# Images
# ================================================

x, y = blob(theta, 0.5,0)
plt.fill(
    x + axis1pos[0], y + axis1pos[1],
    facecolor='red',
    alpha = 0.5,
    edgecolor='k',
    linewidth=1
)
plt.plot(x + axis1pos[0],y + axis1pos[1], 'k-',lw=1)

x, y = blob(theta, 0.2,0, 0.1,0.1)
plt.fill(
    x + axis2pos[0]-0.4, y + axis2pos[1]+0.3,
    facecolor='red',
    alpha = 0.5,
    edgecolor='k',
    linewidth=1
)
x, y = blob(theta, 0.6,1.5, 0.1, 0.2, 0.05)
plt.fill(
    0.9 * x + axis2pos[0], y + axis2pos[1],
    facecolor='blue',
    alpha = 0.5,
    edgecolor='k',
    linewidth=1
)
plt.plot(0.9 * x + axis2pos[0],y + axis2pos[1], 'k-',lw=1)

# ================================================
# Maps
# ================================================
Ox1_vec = np.array(axis1pos) - np.array(posM1)
Ox2_vec = np.array(axis2pos) - np.array(posM2)
plt.arrow(
    posM1[0] + Ox1_vec[0] * 0.2,
    posM1[1] + Ox1_vec[1] * 0.2,
    Ox1_vec[0] * 0.6,
    Ox1_vec[1] * 0.6,
    linewidth=1,
    head_width=0.05,
    head_length=0.1,
    color='k',
    length_includes_head=True
)
plt.arrow(
    posM2[0] + Ox2_vec[0] * 0.2,
    posM2[1] + Ox2_vec[1] * 0.2,
    Ox2_vec[0] * 0.6,
    Ox2_vec[1] * 0.6,
    linewidth=1,
    head_width=0.05,
    head_length=0.1,
    color='k',
    length_includes_head=True
)
plt.annotate(
    r"$\psi_1$",
    np.array(posM1) + Ox1_vec/2 + np.array([0,0.4]),
    ha='center',
    va='center'
)
plt.annotate(
    r"$\psi_2$",
    np.array(posM2) + Ox2_vec/2 + np.array([0,0.4]),
    ha='center',
    va='center'
)
plt.annotate(
    r"$\psi_1[\mathcal{O}_1]$",
    axis1pos + np.array([0,- 1]),
    ha='center',
    va='center'
)
plt.annotate(
    r"$\psi_2[\mathcal{O}_2]$",
    axis2pos + np.array([0,- 1.2]),
    ha='center',
    va='center'
)
# Differentiability
plt.annotate(
    r"$\mathcal{O}_1 \cap \mathcal{O}_2$",
    [1.2,0.85],
    ha='center',
    va='center',
    rotation = 20,
    fontsize = 8
)
# intersection blobs

x, y = blob(theta, 0.2,0, 0.05)
plt.fill(
    x + axis1pos[0]-0.3, y + axis1pos[1]-0.3,
    facecolor='blue',
    alpha = 0.5,
    edgecolor='k',
    linewidth=1
)

# --------------------------------------------------
# Labels

plt.annotate(
    r"$\psi_1[\mathcal{O}_1 \cap \mathcal{O}_2]$",
    [4,3.5],
    ha='center',
    va='center',
    rotation = 0,
    fontsize = 6
)

plt.annotate(
    r"$\psi_2[\mathcal{O}_1 \cap \mathcal{O}_2]$",
    [3,-2.5],
    ha='center',
    va='center',
    rotation = 0,
    fontsize = 6
)
plt.annotate(
    r"$\mathbf{x}(\mathbf{y})$",
    [6.2,0.5],
    ha='center',
    va='center',
    rotation = 0,
    fontsize = 9
)
plt.annotate(
    r"$\psi_2^{-1}[\mathcal{O}_1\cap\mathcal{O}_2]$",
    [3.9,0.2],
    ha='center',
    va='center',
    rotation = -29,
    fontsize = 6
)
plt.annotate(
    r"$\psi_1[\mathcal{O}_1\cap\mathcal{O}_2]$",
    [3.6,1.5],
    ha='center',
    va='center',
    rotation = 20,
    fontsize = 6
)
plt.plot([4,4.8],[3.3,2.8],'k--',lw=0.5)
plt.plot([3,4.7],[-2.3,-1.8],'k--',lw=0.5)

plt.arrow(
    5,-0.8,
    2 - 5, 0.9- -0.8,
    linewidth=1,
    head_width=0.05,
    head_length=0.1,
    color='k',
    length_includes_head=True
)
plt.arrow(
    2,1.2,
    5-2,2.2-1.2,
    linewidth=1,
    head_width=0.05,
    head_length=0.1,
    color='k',
    length_includes_head=True
)
plt.arrow(
    5.75,-1.3,
    6-5.75,0--1.3,
    linewidth=1,
    head_width=0.05,
    head_length=0.1,
    color='k',
    length_includes_head=True
)
plt.arrow(
    6,1,
    5.75-6, 1.8-1,
    linewidth=1,
    head_width=0.05,
    head_length=0.1,
    color='k',
    length_includes_head=True
)
# =========================================================
# Formatting
# =========================================================

plt.axis(False)
# plt.grid(which='both')
plt.tight_layout()

plt.savefig(fig3)
os.startfile(fig3)

fig3 = r'..\images\sterographicprojection.pdf'

plt.figure(figsize=(4, 2.8), dpi=300)
ax = plt.gca()
ax.set_aspect('equal')


# =========================================================
# 3D -> 2D projection
# =========================================================

azimuth = np.deg2rad(-10)
elevation = np.deg2rad(25)

# Rotation about z
R_az = np.array([
    [np.cos(azimuth), -np.sin(azimuth), 0],
    [np.sin(azimuth),  np.cos(azimuth), 0],
    [0,                0,               1]
])

# Projection corresponding to your elevation convention
R_el = np.array([
    [1, 0, 0],
    [0, np.sin(elevation), np.cos(elevation)],
    [0, 0, 1]
])


def project(P):
    """
    Transform a 3D point P into the 2D plotting plane.
    """
    P_rot = R_az @ P
    P_plot = R_el @ P_rot

    return P_plot[:2]


# =========================================================
# Sphere S^2
# =========================================================

theta = np.linspace(0, 2*np.pi, 360)

S2 = np.array([
    np.cos(theta),
    np.sin(theta)
])


# =========================================================
# Important 3D points
# =========================================================

N_3d = np.array([0, 0, 1])
S_3d = np.array([0, 0, -1])


N = project(N_3d)
S = project(S_3d)


# =========================================================
# Plane
# =========================================================

plane_scale = 3

plane_coords = np.array([
    [-1, -1],
    [ 1, -1],
    [ 1,  1],
    [-1,  1],
    [-1, -1]
])

# Plane lies at z = -1
plane_3d = np.column_stack([
    plane_scale * plane_coords[:, 0],
    plane_scale * plane_coords[:, 1],
    -np.ones(len(plane_coords))
])

plane_plot = np.array([
    project(P)
    for P in plane_3d
]).T


# =========================================================
# Grid on the plane
# =========================================================

grid = np.arange(-plane_scale, plane_scale + 1, 1)

for u in grid:

    line_3d = np.column_stack([
        np.full(2, u),
        [-plane_scale, plane_scale],
        [-1, -1]
    ])

    line_plot = np.array([
        project(P)
        for P in line_3d
    ]).T

    plt.plot(
        line_plot[0],
        line_plot[1],
        'k--',
        lw=0.5,
        alpha=0.5,
        zorder=0
    )


for v in grid:

    line_3d = np.column_stack([
        [-plane_scale, plane_scale],
        np.full(2, v),
        [-1, -1]
    ])

    line_plot = np.array([
        project(P)
        for P in line_3d
    ]).T

    plt.plot(
        line_plot[0],
        line_plot[1],
        'k--',
        lw=0.5,
        alpha=0.5,
        zorder=0
    )


# Plane boundary
plt.plot(
    plane_plot[0],
    plane_plot[1],
    'k-',
    lw=1,
    zorder=0
)


# =========================================================
# Sphere and equator
# =========================================================

plt.fill(
    S2[0],
    S2[1],
    facecolor='white',
    edgecolor='none',
    alpha=0.5,
    zorder=1
)

plt.plot(
    S2[0],
    S2[1],
    'k-',
    lw=1,
    zorder=3
)

x = S2[0]
y = np.sin(elevation) * S2[1]

y_front = y.copy()
y_back = y.copy()

y_front[S2[1] > 0] = np.nan
y_back[S2[1] <= 0] = np.nan

plt.plot(
    x,
    y_back,
    'k--',
    lw=0.5,
    zorder=0
)

plt.plot(
    x,
    y_front,
    'k--',
    lw=0.5,
    zorder=4
)


# =========================================================
# Point P' on the plane
# =========================================================

# Intrinsic coordinates on the plane
PP = np.array([1, -1])

# Convert to 3D
PP_3d = np.array([
    PP[0],
    PP[1],
    -1
])

# Transform to plotting coordinates
PP_plot = project(PP_3d)


# =========================================================
# Find P on S^2
# =========================================================

# Line from N to P'
#
# L(t) = N + t(P' - N)

d = PP_3d - N_3d

# Solve |N + t d|^2 = 1
#
# Since |N| = 1:
#
# t = -2 (N . d) / (d . d)

t = -2 * np.dot(N_3d, d) / np.dot(d, d)

P_3d = N_3d + t * d

# Transform P into the 2D drawing
P_plot = project(P_3d)


# =========================================================
# Projection line N -> P' 
# =========================================================

plt.plot(
    [N[0], PP_plot[0]],
    [N[1], PP_plot[1]],
    'k-',
    lw=1,
    zorder=0
)

plt.plot(
    [P_plot[0], PP_plot[0]],
    [P_plot[1], PP_plot[1]],
    'k-',
    lw=1,
    zorder=3
)

# =========================================================
# Points
# =========================================================

plt.scatter(
    N[0], N[1],
    color='k',
    s=5,
    zorder=5
)

plt.scatter(
    S[0], S[1],
    color='k',
    s=5,
    zorder=0
)

plt.scatter(
    P_plot[0], P_plot[1],
    color='k',
    s=5,
    zorder=5
)

plt.scatter(
    PP_plot[0], PP_plot[1],
    color='k',
    s=5,
    zorder=5
)


# =========================================================
# Labels
# =========================================================

plt.annotate(
    r'$N$',
    N + np.array([0, 0.2]),
    ha='center',
    va='center'
)

plt.annotate(
    r'$S$',
    S + np.array([0, 0.2]),
    ha='center',
    va='center'
)

plt.annotate(
    r'$S^2$',
    [0,0],
    ha='center',
    va='center'
)

plt.annotate(
    r'$p$',
    P_plot + np.array([0.15, 0.08]),
    ha='center',
    va='center'
)

plt.annotate(
    r"$(x,y)$",
    PP_plot + np.array([0.5,0]),
    ha='center',
    va='center'
)

plt.annotate(
    r"$\mathbb{R}^2$",
    [-3,0],
    ha='center',
    va='center'
)

# =========================================================
# Formatting
# =========================================================

plt.axis('off')
plt.tight_layout()

plt.savefig(fig3)
os.startfile(fig3)
