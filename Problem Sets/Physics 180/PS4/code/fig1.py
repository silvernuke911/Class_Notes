import numpy as np
import matplotlib.pyplot as plt
import os
plt.rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'

fsize = 10
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

fig = r'..\images\fig1.pdf'


# Initial conditions and decay constants
N0 = 1
lambda1 = 0.5
lambda2 = 0.3

# Time
t = np.linspace(0, 30, 1000)

# Populations
N1 = N0 * np.exp(-lambda1 * t)

N2 = (
    lambda1 * N0 / (lambda2 - lambda1)
    * (np.exp(-lambda1 * t) - np.exp(-lambda2 * t))
)

N3 = N0 * (
    1
    - (lambda2 * np.exp(-lambda1 * t)
       - lambda1 * np.exp(-lambda2 * t))
      / (lambda2 - lambda1)
)

# Plot
plt.figure(figsize=(6, 3), dpi=300)

plt.plot(
    t, N1,
    'r-', lw=1,
    label=r'$N_1(t)$'
)

plt.plot(
    t, N2,
    'b-', lw=1,
    label=r'$N_2(t)$'
)

plt.plot(
    t, N3,
    'g-', lw=1,
    label=r'$N_3(t)$'
)

plt.xlabel(r'$t$')
plt.ylabel(r'$N_i/N_0$')
plt.xlim(t.min(), t.max())
plt.ylim(0, 1)
plt.legend(frameon=False)
plt.tight_layout()
plt.savefig(fig, bbox_inches='tight')
os.startfile(fig)

filename = r'..\images\fig1a.pdf'

fig, ax = plt.subplots(
    3, 1,
    figsize=(3, 4),
    dpi=300,
    sharex=True
)

fig.subplots_adjust(hspace=0)

ax[0].plot(t, N1, 'r-', lw=1)
ax[1].plot(t, N2, 'b-', lw=1)
ax[2].plot(t, N3, 'g-', lw=1)


# Common limits
dx = 5
dy = 0.2
for i, a in enumerate(ax):
    a.set_xlim(t.min(), t.max())
    a.set_ylim(0, 1)

    if i == 0:
        a.set_yticks(np.arange(0, N0 + dy, dy))
    else:
        a.set_yticks(np.arange(0, N0, dy))

    a.set_xticks(np.arange(t.min(), t.max(), dx))
    a.grid(True)

# Y-axis labels
ax[0].set_ylabel(r'$N_1/N_0$')
ax[1].set_ylabel(r'$N_2/N_0$')
ax[2].set_ylabel(r'$N_3/N_0$')

# Common x-axis
ax[2].set_xlabel(r'$t$')


# Remove x-axis ticks/labels from upper panels
ax[0].tick_params(axis='x', which='both', bottom=False, labelbottom=False)
ax[1].tick_params(axis='x', which='both', bottom=False, labelbottom=False)

plt.savefig(filename, bbox_inches='tight')
plt.close()

os.startfile(filename)
