import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
import os

plt.rcParams.update({
        'text.usetex':True,
        'font.family': 'serif',
        'font.size': 6
    })

x = np.linspace(-4,4,300)
y = np.linspace(-4,4,300)
xv, yv = np.meshgrid(x,y)

q = 1
a = 2
p = q * a 

e0 = 1
k = 1/(4*np.pi*e0)

r = np.sqrt(xv**2 + yv**2)
theta = np.atan2(xv,-yv)
r_plus  = np.sqrt(r**2 + a**2 / 4 - a * r * np.cos(theta))
r_minus = np.sqrt(r**2 + a**2 / 4 + a * r * np.cos(theta))
cmap_color = 'hot'

V = k * q * (1/r_plus - 1/r_minus)
plt.figure(figsize=(2,2),dpi=300)
plt.imshow(
    V,
    cmap=cmap_color,
    vmax = 1,
    vmin = -1,
    extent=[x.min(),x.max(),y.min(),y.max()]
)
ticks = np.arange(-2*a, 3*a, a)
tick_labels = []
for t in ticks:
    if t == 0:
        tick_labels.append('$0$')
    elif t == a:
        tick_labels.append('$a$')
    elif t == -a:
        tick_labels.append('$-a$')
    else:
        tick_labels.append(f'${int(t/a)}a$')
plt.xlim(x.min(),x.max())
plt.ylim(y.min(),y.max())
plt.xticks(ticks, tick_labels)
plt.yticks(ticks, tick_labels)

plot_1 = r"..\images\dipole_normal_V.pdf"
plt.tight_layout()
plt.savefig(plot_1)
os.startfile(plot_1) 


plt.figure(figsize=(2,2),dpi=300)
plt.gca().set_aspect('equal')
yhat = np.array([0, 1])[:, None, None]  # Shape: (2, 1, 1)
rvec = np.array([xv, yv])
rvec_plus = rvec + (a/2) * yhat
rvec_minus = rvec - (a/2) * yhat

r_plus = np.sqrt(rvec_plus[0]**2 + rvec_plus[1]**2)
r_minus = np.sqrt(rvec_minus[0]**2 + rvec_minus[1]**2)
rhat_plus  = rvec_plus / r_plus
rhat_minus = rvec_minus / r_minus

E_plus  =  k * q * (rhat_plus / r_plus**2) 
E_minus = -k * q * (rhat_minus / r_minus**2) 
E = -(E_plus + E_minus)

plt.streamplot(
    xv, yv, 
    E[0], E[1],
    density=1,
    color=np.log(np.sqrt(E[0]**2 + E[1]**2)+1),
    cmap=cmap_color,   
    linewidth=1,
    arrowsize=0.5
)

plt.xlim(x.min(),x.max())
plt.ylim(y.min(),y.max())
plt.xticks(ticks, tick_labels)
plt.yticks(ticks, tick_labels)

plot_2 = r"..\images\dipole_normal_E.pdf"
plt.tight_layout()
plt.savefig(plot_2)
os.startfile(plot_2) 

plt.figure(figsize=(2,2),dpi=300)
V = k * p * np.cos(theta) / r**2 
plt.imshow(
    V,
    cmap=cmap_color,
    vmax = 1,
    vmin = -1,
    extent=[x.min(),x.max(),y.min(),y.max()]
)
plt.xlim(x.min(),x.max())
plt.ylim(y.min(),y.max())
plt.xticks(ticks, tick_labels)
plt.yticks(ticks, tick_labels)
plot_3 = r"..\images\dipole_limit_V.pdf"
plt.tight_layout()
plt.savefig(plot_3)
os.startfile(plot_3) 

plt.figure(figsize=(2,2),dpi=300)
plt.gca().set_aspect('equal')
dx = x[1]-x[0]
dy = y[1]-y[0]
E_y, E_x = np.gradient(V, dx, dy)  
E = np.array([E_x, E_y])  

plt.streamplot(
    xv, yv, 
    E[0], E[1],  
    density=1,
    color=np.log(np.sqrt(E[0]**2 + E[1]**2)+1),
    cmap=cmap_color,   
    linewidth=1,
    arrowsize=0.5
)

plt.xlim(x.min(),x.max())
plt.ylim(y.min(),y.max())
plt.xticks(ticks, tick_labels)
plt.yticks(ticks, tick_labels)
plot_4 = r"..\images\dipole_limit_E.pdf"
plt.tight_layout()
plt.savefig(plot_4)
os.startfile(plot_4) 
