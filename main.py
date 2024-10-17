import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

# Количество частиц
num_particles = 20

# Начальные координаты (все частицы начинаются в центре)
positions = np.zeros((num_particles, 2))

# Генерируем случайные направления (углы) и скорости
angles = np.random.uniform(0, 2 * np.pi, num_particles)  # Углы в радианах
speeds = np.random.uniform(0.01, 0.05, num_particles)  # Скорости

# Создаем фигуру для анимации
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')
scat = ax.scatter(positions[:, 0], positions[:, 1])


def update(frame):
    global positions
    # Обновляем позиции частиц
    for i in range(num_particles):
        positions[i, 0] += speeds[i] * np.cos(angles[i])  # Обновляем x
        positions[i, 1] += speeds[i] * np.sin(angles[i])  # Обновляем y
    scat.set_offsets(positions)  # Обновляем положение частиц
    return scat,


def reset(event):
    global positions, angles, speeds
    positions = np.zeros((num_particles, 2))
    angles = np.random.uniform(0, 2 * np.pi, num_particles)
    speeds = np.random.uniform(0.01, 0.05, num_particles)
    scat.set_offsets(positions)


reset_ax = plt.axes([0.8, 0.01, 0.1, 0.05])
reset_button = Button(reset_ax, 'Reset')
reset_button.on_clicked(reset)


ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)


plt.show()
