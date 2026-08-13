import matplotlib.pyplot as plt 
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 15
})

#========================== 180
def rot(theta):
    return np.array(
        [
            [ np.cos(theta), -np.sin(theta) ],
            [ np.sin(theta),  np.cos(theta) ]
        ]
    )

linewidth = 1

line1 = np.array([[0,0],[1,0]]).T
line2 = np.array([[0,0],[1,0]]).T

line1 = rot(np.deg2rad(60)) @ line1
line2 = rot(np.deg2rad(120)) @ line2 + line1[:, 1].reshape(2, 1)

line3 = np.array([[0,0],[1.2,0]]).T
line3 = rot(np.deg2rad(120)) @ line3 + np.array([2,0]).reshape(2, 1)

line3_end = line3[:, 1]

# Direction of line4
dir4 = rot(np.deg2rad(-30)) @ np.array([[0],[1]])

y_target = line2[1, 1]
L = (y_target - line3_end[1]) / dir4[1]

line4_start = line3_end.reshape(2, 1)
line4_end = line3_end.reshape(2, 1) + L * dir4

line4 = np.hstack([line4_start, line4_end])

dist = np.linalg.norm(line1[:, 1] - line3[:, 1])

# Angle between line1 endpoint and line3 endpoint
dx = line3[0, 1] - line1[0, 1]
dy = line3[1, 1] - line1[1, 1]
angle = np.arctan2(dy, dx)

sinx = np.linspace(0, dist, 200)
siny = 0.06 * np.sin(12 * np.pi * sinx / dist)

# Stack sinx and siny, rotate, then translate to line1 endpoint
sin_wave = np.vstack([sinx, siny])
sin_wave = rot(angle) @ sin_wave + line1[:, 1].reshape(2, 1)

plt.figure(figsize=(4, 4), dpi=300)
plt.gca().set_aspect("equal")
plt.plot(line1[0], line1[1], 'k-', lw = linewidth)
plt.plot(line3[0], line3[1], 'k-', lw = linewidth)
plt.plot(sin_wave[0], sin_wave[1], 'k-', lw = linewidth)

plt.arrow(line2[0, 0], line2[1, 0],
          line2[0, 1] - line2[0, 0], line2[1, 1] - line2[1, 0],
          head_width=0.025, head_length=0.05, fc='k', ec='k', lw = linewidth)

plt.arrow(line4[0, 0], line4[1, 0],
          line4[0, 1] - line4[0, 0], line4[1, 1] - line4[1, 0],
          head_width=0.025, head_length=0.05, fc='k', ec='k', lw = linewidth)

plt.text(line1.T[0][0] + 0.15, line1.T[0][1], "$e^-$",
         ha='center',  # horizontalalignment: 'center', 'left', 'right'
         va='center',  # verticalalignment: 'center', 'top', 'bottom', 'baseline'
     )


plt.text(line3.T[0][0] - 0.15, line3.T[0][1], "$e^-$",
         ha='center',  
         va='center',  
     )

plt.text(line2.T[1][0] + 0.15, line2.T[1][1], "$e^-$",
         ha='center',  
         va='center',  
     )

plt.text(line4.T[1][0] - 0.15, line4.T[1][1], "$e^-$",
         ha='center',  
         va='center',  
     )

plt.text(0.9, 1.1, r"$\gamma$",
         ha='center',  
         va='center',  
     )

plt.grid(False)
plt.axis(False)
plt.tight_layout()
plt.savefig("P180.pdf")
plt.savefig("P180.png")


#====================== 131

import numpy as np
import matplotlib.pyplot as plt

# Grid
x = np.linspace(-3, 3, 600)
y = np.linspace(-3, 3, 600)
X, Y = np.meshgrid(x, y)

# Point dipole at origin, p = p y-hat
r2 = X**2 + Y**2
r5 = r2**2.5

U = 3*X*Y / r5
V = (3*Y**2 - r2) / r5

# Mask singularity
mask = r2 < 0.001
U = np.ma.masked_where(mask, U)
V = np.ma.masked_where(mask, V)

# Plot
fig, ax = plt.subplots(figsize=(4, 4), dpi=300)

ax.streamplot(
    X, Y, U, V,
    density=1.8,
    linewidth=1,
    arrowsize=0.75,
    color='k'
)

ax.set_aspect("equal")
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

ax.axis(False)
plt.tight_layout()
plt.savefig("P131.pdf")
plt.savefig("P131.png")

# ================================== 225

# Schwarzschild radius
rs = 1.0

# Cartesian grid
x = np.linspace(-8*rs, 8*rs, 800)
y = np.linspace(-8*rs, 8*rs, 800)
X, Y = np.meshgrid(x, y)

# Radial distance, used only to define the Cartesian surface
R = np.sqrt(X**2 + Y**2)

# Flamm paraboloid
Z = 2 * np.sqrt(rs * (R - rs))

# Mask the interior of the event horizon
Z[R < rs - 0.1] = np.nan

fig = plt.figure(figsize=(4, 4), dpi=300)
ax = fig.add_subplot(111, projection="3d")

cellsize = 25
# Upper sheet
ax.plot_surface(
    X, Y, Z,
    rstride = cellsize,
    cstride = cellsize,
    facecolor='white',
    edgecolor='black',
    linewidth=0.5
)

# Lower sheet
ax.plot_surface(
    X, Y, -Z,
    rstride = cellsize,
    cstride = cellsize,
    facecolor='white',
    edgecolor='black',
    linewidth=0.5
)

ax.plot([0], [0], [4], 
        marker='o', 
        markersize=8,
        markerfacecolor='white',
        markeredgecolor='black',
        markeredgewidth=1,
        zorder=10)

ax.set_box_aspect((1, 1, 0.5))
ax.set_xlim(-8*rs, 8*rs)
ax.set_ylim(-8*rs, 8*rs)

ax.view_init(elev=27, azim=-60)

plt.axis(False)
plt.tight_layout()

plt.savefig("P225.pdf")
plt.savefig("P225.png")

# =============================== 225 2

import numpy as np
import matplotlib.pyplot as plt

# Schwarzschild radius
rs = 1

scale = 15/rs

# Cartesian grid
x = np.linspace(-scale * rs, scale * rs, 800)
y = np.linspace(-scale * rs, scale * rs, 800)

X, Y = np.meshgrid(x, y)

# Radial distance
R = np.sqrt(X**2 + Y**2)

# Flamm paraboloid
Z = 2 * np.sqrt(rs * (R - rs)) 

# Mask the interior of the event horizon
Z[R < rs - 0.1] = np.nan

# Figure
fig = plt.figure(figsize=(4, 4), dpi=300)
ax = fig.add_subplot(111, projection="3d")

# ============================================================
# Flamm paraboloid wireframe
# ============================================================

ax.plot_wireframe(
    X,
    Y,
    Z,
    rstride=20,
    cstride=20,
    color="k",
    linewidth=0.75,
    zorder = 1
)

# ============================================================
# White disk with black outline - using scatter
# ============================================================
# White filled circle with black edge - use plot instead
ax.plot([0], [0], [6], 
        marker='o', 
        markersize=8,
        markerfacecolor='white',
        markeredgecolor='black',
        markeredgewidth=1,
        zorder=10)

# ============================================================
# Axes / projection
# ============================================================

ax.set_box_aspect((2*scale, 2*scale, np.nanmax(Z)))

ax.set_xlim(-scale * rs, scale * rs)
ax.set_ylim(-scale * rs, scale * rs)

ax.view_init(
    elev=27,
    azim=-57.5
)

plt.axis(False)
plt.tight_layout()

# ============================================================
# Save
# ============================================================

plt.savefig(
    "P225_2.pdf"
)

plt.savefig(
    "P225_2.png",
    bbox_inches="tight",
    pad_inches=0.25
)

