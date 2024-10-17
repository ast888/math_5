import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Определяем функцию f(x, y)
def f(x, y):
    return np.sin(x) * np.cos(y)

# Создаем сетку значений x и y
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)  # от -2π до 2π
y = np.linspace(-2 * np.pi, 2 * np.pi, 100)  # от -2π до 2π
x, y = np.meshgrid(x, y)  # создаем сетку

# Вычисляем значения z
z = f(x, y)

# Создаем 3D график
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Ось Z')
ax.set_title('3D график поверхности z = sin(x) * cos(y)')

plt.show()
