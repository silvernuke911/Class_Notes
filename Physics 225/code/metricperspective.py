import matplotlib.pyplot as plt 
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.size": 8
})

plt.figure(figsize=(4,2),dpi=300)
plt.gca().set_aspect('equal')

metric_pos = np.array([0,2.5])
plt.annotate(
    r"\textbf{Metric}",
    xy=metric_pos,
    ha="center",
    va="center",
    bbox=dict(
        boxstyle="square,pad=0.3",
        facecolor="white",
        edgecolor="black",
        linewidth=0.5
    )
)
plt.annotate(
    r"$\mathbf{Relativist\ perspective}$" + "\n\n" +
    "Spacetime structure is variant\n" +
    r"$\downarrow$" + "\n" +
    "Gravity is the manifestation\n" +
    "of Riemannian spacetime\n" +
    "curvature and it governs\n" +
    "particle motion",
    xy=[-4, -1.5],
    ha="center",
    va="center",
    multialignment="center",
    bbox=dict(
        boxstyle="square,pad=0.3",
        facecolor="white",
        edgecolor="black",
        linewidth=0.5
    )
)
plt.annotate(
    r"$\mathbf{Particle\ physicist\ perspective}$" + "\n\n" +
    "Fixed spacetime,\n" +
    "fields live on top of it" + "\n" +
    r"$\downarrow$" + "\n" +
    "Gravity is a special\n" +
    r"gauge field in $SO(3,1)$" + "\n" +
    "which couples to\n" +
    "everything universally",
    xy=[4, -1.5],
    ha="center",
    va="center",
    multialignment="center",
    bbox=dict(
        boxstyle="square,pad=0.3",
        facecolor="white",
        edgecolor="black",
        linewidth=0.5
    )
)
boxpos = np.array([2,0.8]) - metric_pos
plt.arrow(
    metric_pos[0], metric_pos[1],       # start
    boxpos[0], boxpos[1],       # dx, dy
    width=0.005,
    head_width=0.1,
    head_length=0.15,
    length_includes_head=True
)
plt.arrow(
    metric_pos[0], metric_pos[1],       # start
    -boxpos[0], boxpos[1],       # dx, dy
    width=0.005,
    head_width=0.1,
    head_length=0.15,
    length_includes_head=True
)
plt.axis(False)
plt.xlim(-5,5)
plt.ylim(-3,3)
plt.tight_layout()
plt.savefig(r"..\images\metricperspective.pdf")
