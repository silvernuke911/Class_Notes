
import numpy as np
import matplotlib.pyplot as plt 

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

science_plot(scistyle=False)

# == POINT CHARGE 
plt.figure(figsize=(2, 2), dpi=300)
plt.gca().set_aspect("equal")

q = np.array([0, 0])
P = np.array([1, 2])

# Plot points
plt.scatter(q[0], q[1], color='k', s=5)
plt.scatter(P[0], P[1], color='k', s=5)

# Arrow from q to P
plt.arrow(q[0], q[1], P[0]*0.93, P[1]*0.93, 
          head_width=0.05, lw= 1, fc='k', ec='k')

# Annotations
plt.annotate(r'$q$', xy=q + [0.15,0], ha='center', va='center',fontsize=8)
plt.annotate(r'$P$', xy=P + [0.15,0], ha='center', va='center',fontsize=8)
r_mid = (P - q) / 2  
plt.annotate(r'$\mathbf{r}_{qP}$', xy=r_mid + [-0.15,0.2], ha='center', va='center',fontsize=8)
# plt.tight_layout()
plt.axis(False)
plt.xlim(-0.05,1.2)
plt.ylim(-0.05,2.1)
plt.savefig(r"..\images\pointcharge.pdf")


# == LINE CHARGE 
plt.figure(figsize=(2, 2), dpi=300)
plt.gca().set_aspect("equal")

l1 = np.array([0,0])
l2 = np.array([1.2,2])
L = np.vstack([l1,l2]).T
plt.annotate(r'$L$', xy= l1 + (0.15,0), ha='center',va='center',fontsize=8)
plt.annotate(r'$\lambda$', xy= l2 + (0.15,0), ha='center',va='center',fontsize=8)
for i in range(1,8):
    pt = l2 * i/8
    offset = 0.03 * np.array([-l2[1],l2[0]]) 
    plt.annotate(r'$+$', xy = pt + offset, ha='center',va='center',fontsize=8)
plt.plot(L[0],L[1],'k-',lw=0.8)

q = l2 / 2 
lhat = l2 / np.linalg.norm(l2)
q1 = q - 0.1 * lhat 
q2 = q + 0.1 * lhat
dq = np.vstack([q1,q2]).T
plt.plot(dq[0],dq[1],'k-',lw=2)
plt.annotate(r'$dq$', xy=q + [0.15,-0.1], ha='center', va='center',fontsize=8)

P = np.array([2,1.2])
plt.annotate(r'$P$', xy=P + [0.15,0.15], ha='center', va='center',fontsize=8)
plt.scatter(P[0], P[1],s=5,c='k')

rqP = P - q 
plt.arrow(q[0], q[1], 0.9 * rqP[0], 0.9 * rqP[1], 
          head_width=0.05, lw=1, fc='k', ec='k')
midpoint = q + 0.5 * rqP + [0,0.15]

plt.annotate(r'$\mathbf{r}_{qP}$', xy=midpoint, 
             ha='center', va='center', fontsize=8)

plt.annotate(r'$dq = \lambda\,dl$', xy=[1.5, 0.5], 
             ha='center', va='center', fontsize=8)

plt.annotate(r'$\displaystyle q = \int_L \lambda\,dl$', xy=[1.5, 0.15], 
             ha='center', va='center', fontsize=8)

plt.xlim(-0.05,2.2)
plt.ylim(-0.1,2.2)
plt.axis(False)
plt.tight_layout()
plt.savefig(r"..\images\linecharge2.pdf")

#== SURFACE CHARGE

plt.figure(figsize=(2, 2), dpi=300)
plt.gca().set_aspect("equal")

# Shear matrix
shear_mat = np.array([
    [1, 0],
    [0.5, 1]
])

l = 2
w = 1.5

# Sheared surface
surface = np.array([
    [0, 0],
    [l, 0],
    [l, w],
    [0, w],
    [0, 0]
])
surface = shear_mat @ surface.T
surf = surface

for i in range(4):
    plt.plot(surf[0][i:i+2], surf[1][i:i+2], 'k-', lw=1)

dS_center = np.array([l, w]) / 2
dS_center_sheared = shear_mat @ dS_center 

center_col = dS_center_sheared[:, None]  

dS = (surface - center_col) * 0.15 + center_col  
dS_T = dS

for i in range(4):
    plt.plot(dS_T[0][i:i+2], dS_T[1][i:i+2], 'k-', lw=1)

dx = 0.25
S_i = np.arange(dx, l, dx)
S_j = np.arange(dx, w, dx)

grid_points = np.array([[i, j] for i in S_i for j in S_j]).T
sheared_grid = shear_mat @ grid_points

for k in range(sheared_grid.shape[1]):
    x, y = sheared_grid[0, k], sheared_grid[1, k]
    if not (abs(x - dS_center_sheared[0]) < 0.01 and abs(y - dS_center_sheared[1]) < 0.01):
        plt.annotate(r"$+$", xy=[x, y], va='center', ha='center', fontsize=8)

P = np.array([3, 3])
plt.scatter(P[0], P[1], c='k', s=5)
plt.annotate(r'$P$', xy=P + [0.15,-0.2], ha='center', va='center',fontsize=8)

rqP = P - dS_center_sheared
plt.arrow(dS_center_sheared[0], dS_center_sheared[1], 
          0.9 * rqP[0], 0.9 * rqP[1],
          head_width=0.05, lw=1, fc='k', ec='k')

midpoint = dS_center_sheared + 0.7 * rqP + [0.1,- 0.3]

plt.annotate(r'$\mathbf{r}_{qP}$', xy=midpoint, 
             ha='center', va='center', fontsize=8)

plt.annotate(r'$S$', xy=surface.T[0] + [0.15,0.2], 
             ha='center', va='center', fontsize=8)
plt.annotate(r'$dS$', xy=dS_center_sheared + [0.0,0.25], 
             ha='center', va='center', fontsize=8)

plt.annotate(r'$\sigma$', xy=[0,1.75], 
             ha='center', va='center', fontsize=8)

plt.annotate(r'$dq = \sigma\,dS$',xy = [0.5,3], ha='center',va='center',fontsize=8)
plt.annotate(r'$\displaystyle q =\int_S \sigma\,dS$',xy = [0.5,2.5], ha='center',va='center',fontsize=8)

plt.axis(False)
plt.xlim(None,3.5)
plt.tight_layout()
# plt.grid()
# plt.xticks(np.arange(0,3,0.5))
# plt.yticks(np.arange(0,3,0.5))
plt.savefig(r"..\images\surfacecharge.pdf")

# == volume charge
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create figure
fig = plt.figure(figsize=(2, 2), dpi=300)
ax = fig.add_subplot(111, projection='3d')

# ============================================
# BEAN SHAPE
# ============================================
u = np.linspace(0, 2 * np.pi, 50)
v = np.linspace(0, np.pi, 50)
U, V = np.meshgrid(u, v)

R = 1
r = R * (1 + 0.3 * np.cos(U))

X = r * np.sin(V) * np.cos(U)
Y = r * np.sin(V) * np.sin(U) * 0.7
Z = r * np.cos(V) * 0.6

# Bean surface (transparent)
surf_face = ax.plot_surface(X, Y, Z, 
                            color='black',
                            alpha=0.05,
                            edgecolor='none',
                            rstride=1,
                            cstride=1)

# Bean wireframe
ax.plot_wireframe(X, Y, Z, 
                  rstride=3,
                  cstride=3,
                  color='k',
                  linewidth=0.3,
                  alpha=0.7)

# ============================================
# CUBE (side length s, centered at origin)
# ============================================
s = 0.15  # Side length
half = s / 2

# 8 vertices
vertices = np.array([
    [-half, -half, -half],
    [ half, -half, -half],
    [ half,  half, -half],
    [-half,  half, -half],
    [-half, -half,  half],
    [ half, -half,  half],
    [ half,  half,  half],
    [-half,  half,  half]
])

# 6 faces
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[4], vertices[5], vertices[6], vertices[7]],
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[2], vertices[3], vertices[7], vertices[6]],
    [vertices[0], vertices[3], vertices[7], vertices[4]],
    [vertices[1], vertices[2], vertices[6], vertices[5]]
]

# Cube with transparent faces and edges
cube = Poly3DCollection(faces, 
                        facecolors='black',
                        alpha=0,
                        edgecolors='k',
                        linewidths=0.5)

ax.add_collection3d(cube)

# ============================================
# STYLING
# ============================================
ax.set_box_aspect([1, 1, 1])
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.axis('off')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])


P = np.array([0,0.9,0.8])
ax.text(P[0] + 0.1,P[1],P[2],r"$P$", fontsize = 8, color='k')
ax.scatter(P[0],P[1],P[2],color='k',s=3)
# 3D arrow from origin to P
ax.quiver(0, 0, 0,           # Start point (x, y, z)
          0.95*P[0], 0.95*P[1], 0.95*P[2],  # Direction vector (dx, dy, dz)
          color='k', 
          linewidth=0.8,
          arrow_length_ratio=0.1)  # Controls arrow head size
ax.text(P[0]*0.75 + 0.1,P[1]*0.75,P[2]*0.75,r"$\mathbf{r}_{qP}$", fontsize = 8, color='k')
ax.text(0.2,0,0,r"$dV$", fontsize = 8, color='k')
ax.text(0.5,0,-0.5,r"$V$", fontsize = 8, color='k')

ax.text(0.5,0,0,r"$+$", fontsize = 8, color='k')
ax.text(-0.5,0,0,r"$+$", fontsize = 8, color='k')
ax.text(0,0.5,0,r"$+$", fontsize = 8, color='k')
ax.text(0,-0.5,0,r"$+$", fontsize = 8, color='k')
ax.text(0,0,0.5,r"$+$", fontsize = 8, color='k')
ax.text(0,0,-0.5,r"$+$", fontsize = 8, color='k')

ax.text(-1,-1,-0.75,r"$dq = \rho\,dV$", fontsize = 8, color = 'k')
ax.text(-1,-1,-1.25,r"$\displaystyle q = \int_V \rho\,dV$", fontsize = 8, color = 'k')

plt.tight_layout()
plt.savefig(r"..\images\volumecharge.pdf")
