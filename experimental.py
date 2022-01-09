import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2 * np.pi)
phi = np.linspace(10, -10)
x = np.cos(4 * theta) * np.cos(theta)
y = np.cos(4 * theta) * np.sin(theta)
z = theta

fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
ax.stem(x, y, z)

ax.set(xlabel='x', ylabel='y', zlabel='z')

plt.show()