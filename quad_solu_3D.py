import matplotlib.pyplot as plt
import numpy as np

def quadratic(a, b, c):
    square = (b ** 2) - (4 * a * c)
    root = (square ** 0.5) / (2 * a)
    answer = (-b) / (2 * a)
    return [np.round(answer + root, 3), np.round(answer - root, 3)]

ax = plt.axes(projection='3d')

def f(x, y):
    return quadratic(x, 0, y) # change variable locations to change what x and y graph

x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)

Z = f(X, Y)[0]
ax.plot_surface(X, Y, Z, rstride=10, cstride=10, cmap='viridis', edgecolor='none') # change these lines to change how the graph looks
Z = f(X, Y)[1]
ax.plot_surface(X, Y, Z, rstride=10, cstride=10, cmap='viridis', edgecolor='none')

# ax.contour3D(X, Y, Z, 100)
# ax.plot_wireframe(X, Y, Z, rstride=1, cstride=1, color='k')
# ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='binary', edgecolor='none')

plt.show()
