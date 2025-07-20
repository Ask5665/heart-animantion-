import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x = np.linspace(-np.sqrt(3), np.sqrt(3), 1000)
sqrt_term = np.sqrt(3 - x**2)
base_y = np.abs(x)**(2/3)


y_max = np.max(base_y + 0.9 * sqrt_term)
y_min = np.min(base_y - 0.9 * sqrt_term)

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)


ax.set_xlim(-np.sqrt(3), np.sqrt(3))
ax.set_ylim(y_min, y_max)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])
ax.grid(False)


def init():
    line.set_data([], [])
    return line,


def update(frame):
    k = frame * 0.5
    color = plt.cm.plasma((np.sin(k * 0.1) + 1) / 2)  
    y = base_y + 0.9 * np.sin(k * x) * sqrt_term
    line.set_data(x, y)
    line.set_color(color)
    return line,


ani = FuncAnimation(fig, update, frames=np.arange(0, 400), init_func=init,
                    interval=40, blit=True)

ani.save('heart.gif', writer='pillow', fps=25)

plt.show()
