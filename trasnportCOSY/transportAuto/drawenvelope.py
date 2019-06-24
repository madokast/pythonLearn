import transport
import matplotlib.pyplot as plt
import numpy as np

print(transport.trans(QGO=-4.3737, QG1=5.398396, CD1ang=15.0, CD1n=5.9, CD2n=-22.9, gap=0.3))

x = np.linspace(-2, 6, 50)
y1 = x + 3  # 曲线 y1
y2 = 3 - x  # 曲线 y2
plt.figure()  # 定义一个图像窗口
plt.plot(x, y1)  # 绘制曲线 y1
plt.plot(x, y2)  # 绘制曲线 y2
plt.show()
