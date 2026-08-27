import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 10,
    "axes.titlesize": 10,
    "axes.labelsize": 10,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
})
def draw_reference_frame(center, scale, tick_spacing, tick_length, label):

    S = scale * square + center

    # Reference frame
    plt.plot(S.T[0], S.T[1], color='k', lw=1)

    # Axes through center
    plt.plot(
        [S[:, 0].min(), S[:, 0].max()],
        [center[1], center[1]],
        color='k', ls='--', lw=0.5
    )

    plt.plot(
        [center[0], center[0]],
        [S[:, 1].min(), S[:, 1].max()],
        color='k', ls='--', lw=0.5
    )

    # x-axis ticks
    x_ticks = np.arange(
        S[:, 0].min(),
        S[:, 0].max() + tick_spacing,
        tick_spacing
    )

    for x in x_ticks:
        plt.plot(
            [x, x],
            [center[1] - tick_length / 2,
             center[1] + tick_length / 2],
            color='k',
            lw=0.5
        )

    # y-axis ticks
    y_ticks = np.arange(
        S[:, 1].min(),
        S[:, 1].max() + tick_spacing,
        tick_spacing
    )

    for y in y_ticks:
        plt.plot(
            [center[0] - tick_length / 2,
             center[0] + tick_length / 2],
            [y, y],
            color='k',
            lw=0.5
        )
    
    plt.annotate(
        label,
        xy = center + [0.4,-0.4],
        ha='center',
        va='center'
    )

plt.figure(figsize=(4,1.5),dpi=300)
plt.gca().set_aspect('equal')
square = 0.5 * np.array([
    [ 1,  1],
    [ 1, -1],
    [-1, -1],
    [-1,  1],
    [ 1,  1],
]) # square of sidelength 1

S1 = np.array([-2,0])
draw_reference_frame(
    center=S1,
    scale=2,
    tick_spacing=0.2,
    tick_length=0.1,
    label = r"$S$"
)
S2 = np.array([1,0.5])
draw_reference_frame(
    center=S2,
    scale=2,
    tick_spacing=0.2,
    tick_length=0.1,
    label = r"$S'$"
)

v = 2 * (S2 - S1) / np.linalg.norm(S2-S1)

plt.arrow(
    S2[0],
    S2[1],
    v[0],
    v[1],
    linewidth=0.75,
    head_width=0.05,
    color='k',
    length_includes_head=True
)
plt.annotate(
    "$v$",
    xy = S2 + 0.75*v + [0,0.2],
    ha='center',
    va='center'
)
plt.annotate(
    "$v=0$",
    xy = S1 - [0,1.2],
    ha='center',
    va='center'
)
plt.ylim(-1.3,None)
plt.axis("Off")
plt.tight_layout()

img1 = r"..\images\frames_in_motion.pdf"
plt.savefig(img1)
os.startfile(img1)

fig, ax = plt.subplots(1, 3, figsize=(4, 2), dpi=300)

# --------------------------------------------------
# Lorentzian: kappa = (0, infinity)
# --------------------------------------------------
lim = 1

ax[1].fill(
    [-lim, 0, lim],
    [lim, 0, lim],
    color='yellow',
    alpha=0.5
)
ax[1].fill(
    [-lim, 0, lim],
    [-lim, 0, -lim],
    color='yellow',
    alpha=0.5
)

# Cone boundaries
ax[1].plot([-lim, lim], [-lim, lim], color='yellow', lw=1)
ax[1].plot([-lim, lim], [lim, -lim], color='yellow', lw=1)

# --------------------------------------------------
# Galilean: kappa = infinity
# --------------------------------------------------

ax[0].plot([-lim, lim], [0, 0], color='yellow', lw=2)
# Entire spacetime plane
ax[0].patch.set_facecolor('yellow')
ax[0].patch.set_alpha(0.5)

# --------------------------------------------------
# Carrollian: kappa = 0
# --------------------------------------------------
# Degenerate light cone: t-axis
ax[2].plot([0, 0], [-lim, lim], color='yellow', lw=2)

# --------------------------------------------------
# Common formatting
# --------------------------------------------------
for a in ax:
    a.set_aspect('equal')
    a.set_xlabel(r'$x$')
    a.set_ylabel(r'$t$')
    a.set_xlim(-lim,lim)
    a.set_ylim(-lim,lim)
    # Axes through origin
    a.axhline(0, color='k', lw=0.5)
    a.axvline(0, color='k', lw=0.5)

    # Remove tick labels
    a.set_xticks([])
    a.set_yticks([])

# Titles below the figures
ax[1].set_title(
    r'Lorentzian, $\kappa=(0,\infty)$',
    fontsize=9,
    y=-0.5
)

ax[0].set_title(
    r'Galilean, $\kappa=\infty$',
    fontsize=9,
    y=-0.5
)

ax[2].set_title(
    r'Carrollian, $\kappa=0$',
    fontsize=9,
    y=-0.5
)

plt.tight_layout()

img2 = r"..\images\cones_types_of_relativity.pdf"
plt.savefig(img2, bbox_inches='tight')
os.startfile(img2)
