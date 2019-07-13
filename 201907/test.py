import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_points(num):
    '''
    更新数据点
    '''
    point_ani.set_data(x[num], y[num])
    return point_ani,

fig = plt.figure(tight_layout=True)
plt.plot(x, y)
point_ani, = plt.plot(x[0], y[0], "ro")

ani = animation.FuncAnimation(fig, update_points, np.arange(0, x.__len__()), interval=0.01, blit=True)
plt.show()
