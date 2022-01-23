import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery-nogrid')

# make data
X, Y = np.meshgrid(np.linspace(-10, 10, 264), np.linspace(-10, 10, 300))
Z = (1 - 5 * X + Y ** 10 + X**6 + 40 * np.cos(X ** 8)) * np.exp(-X**2 - Y**2)

# plot
fig, ax = plt.subplots()

ax.contour(X, Y, Z, levels=15)

plt.show()