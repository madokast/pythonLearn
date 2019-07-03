import matplotlib.pyplot as plt
import numpy as np

'''
    双极坐标系
    文档中有详细介绍
'''

a = 1  # foci 焦点 (0,a) (0,-a)

# ksi 0-2pi 构成过一个焦点的圆，关于x轴对称，圆心在轴上，也就是说上下各一个
# |eta| 的值越小，圆半径越大。 eta 不能为0
# eta 为正时 圆整体位于x轴之上 。 复数时，位于x轴之下
# 圆方程 x^2 + ( x - a cot(ksi))^2 = a^2/sin^2(ksi)
ksi = np.linspace(0, 2 * np.pi, 100)
for eta in np.linspace(-5, 5, 11):
    if np.abs(eta) < 10e-7: continue
    x = a * np.sin(ksi) / (np.cosh(eta) - np.cos(ksi))
    y = a * np.sinh(eta) / (np.cosh(eta) - np.cos(ksi))
    plt.plot(y, x)


# eta 0-2pi 构成圆心在x轴上的圆 . 圆经过两个焦点
# ksi 不能为0

eta = np.linspace(np.pi, 1 * np.pi+10, 100)
for ksi in [1,2]:
    if np.abs(ksi) < 10e-7: continue
    x = a * np.sin(ksi) / (np.cosh(eta) - np.cos(ksi))
    y = a * np.sinh(eta) / (np.cosh(eta) - np.cos(ksi))
    plt.plot(y, x)
    # plt.plot(-y, x)

plt.axis('equal')
plt.show()
