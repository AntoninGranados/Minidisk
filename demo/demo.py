import sys
sys.path.append('.')
sys.path.append('..')

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle as PltCircle, Ellipse as PltEllipse

from minidisk import Circle, minidisk
from miniellipse import miniellipse

points = np.random.random((20, 2)) * 2 - 1

circle = minidisk(list(points))
ellipse = miniellipse(list(points))

plt_circle = PltCircle(
    circle.center, circle.radius,
    facecolor="none", edgecolor="k"
)

eigenvalues, eigenvectors = np.linalg.eig(ellipse)
axis_size = 2 / np.sqrt(eigenvalues)
angle = np.rad2deg(np.atan2(eigenvectors[1,0], eigenvectors[0,0]))
plt_ellipse = PltEllipse(
    (0,0), axis_size[0], axis_size[1], angle=angle,
    facecolor="none", edgecolor="k"
)

fig, axs = plt.subplots(1, 2)

axs[0].scatter(points[:,0], points[:,1])
axs[0].add_patch(plt_circle)
axs[0].set_xlim(-2, 2)
axs[0].set_ylim(-2, 2)
axs[0].set_aspect("equal")
axs[0].set_title("Smallest Enclosing Disk")

axs[1].scatter(points[:,0], points[:,1])
axs[1].add_patch(plt_ellipse)
axs[1].set_xlim(-2, 2)
axs[1].set_ylim(-2, 2)
axs[1].set_aspect("equal")
axs[1].set_title("Smallest Enclosing Ellipse\n(centered at 0)")

fig.tight_layout()
plt.show()
