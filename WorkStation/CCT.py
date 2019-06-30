import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

miu0 = 4 * np.pi / 10 ** 7


def deltaB(p0, p1, I, p):
    """
    计算点 p0 到点 p1 电流为 I 的直导线在 p 点产生的磁场。
    使用 毕奥-萨伐尔定律
    :param p0: 直导线起点 np.array() 量
    :param p1: 直导线终点 np.array() 量
    :param I: 电流，从 p0 流向 p1 float 量
    :param p: 需要计算磁场的点 np.array() 量
    :return: p 点的磁场 np.array() 量
    """
    p01 = p1 - p0
    r = p - p0
    rr = np.linalg.norm(r)

    # 计算速度有点慢啊
    return (10.0 ** -7) * I * (np.cross(p01, r)) / (rr ** 3)


class Solenoid:
    """
    螺线管
    """

    def __init__(self, r, w, n, I, stepTheta):
        """
        直螺线管建模
        :param r: 半径
        :param w: 相邻导线的距离 (轴向)
        :param n: 总匝数 n
        :param I: 电流
        :param stepTheta: θ步长，影响磁场计算精度
        """
        self.r = r
        self.w = w
        self.I = I
        self.n = n
        self.stepTheta = stepTheta

    def point(self, theta):
        """
        计算θ位置对应的点坐标
        注意坐标为笛卡尔直角坐标系。
        螺线管轴向为 z 轴，从z=0开始正向生长。
        θ=0 时，x=-r y=0 ，朝向 z 轴正方向，随 θ 增大，线圈顺时针转动
        具体可以参考文档AGCCT
        :param theta: 唯一的一个自变量θ
        :return: θ位置对应的点坐标
        """
        rr = np.array([-self.r * np.cos(theta), self.r * np.sin(theta), 0.0])
        zz = np.array([0.0, 0.0, self.w / (2 * np.pi) * theta])
        return rr + zz

    def magnet(self, p):
        """
        计算 p 点磁场
        :param p: np.array() 量
        :return: p 点磁场 np.array() 量
        """
        B = np.array([0, 0, 0])
        end = self.n * 2.0 * np.pi - self.stepTheta
        num = int(end / self.stepTheta)
        for th in np.linspace(0, end, num):
            p0 = self.point(th)
            p1 = self.point(th + self.stepTheta)
            B = B + deltaB(p0, p1, self.I, p)

        return B

    def plot(self):
        end = self.n * 2.0 * np.pi
        num = int(end / self.stepTheta)
        x = [0] * num
        y = [0] * num
        z = [0] * num
        i = 0
        for th in np.linspace(0, end, num):
            p0 = self.point(th)
            x[i] = p0[0]
            y[i] = p0[1]
            z[i] = p0[2]
            i = i + 1

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.plot(x, y, z)
        plt.show()

    @classmethod
    def demoInstance(cls):
        """
        :return: 一个demo
        """
        r = 0.1
        w = 0.01
        n = 400
        I = 1.0
        step = np.pi / 180.0
        print("线圈半径{}m，匝间距{}m，匝数{}，电流{}A，计算步长{}弧度".format(r, w, n, I, step))
        print("对应的无限长螺线管的理论磁场Bz = {: e}".format(-(10.0 ** -7) * 100 * 4 * np.pi))
        return Solenoid(r, w, n, I, step)


# 以下为测试代码
s = Solenoid.demoInstance()
print(s.magnet(np.array([0, 0, 2.0])))

# 2019年6月30日 螺线管测试通过
# 6.283185307179586e-06
# print((10.0 ** -7) * 5 * 4 * np.pi)
# s = Solenoid(0.1, 0.2, 1.0, np.pi / 180.0)
# s.plot()
# for i in np.linspace(0, 10, 10):
#     print(str(i) + '  ' + str(s.magnet(np.array([0, 0, i]))))
# 0.0  [ 6.52933420e-07  3.97898928e-07 -3.14588441e-06]
# 1.1111111111111112  [-2.74703870e-07 -7.54690884e-07 -6.27040826e-06]
# 2.2222222222222223  [ 5.13287917e-07  6.05768731e-07 -6.27987534e-06]
# 3.3333333333333335  [-6.90245782e-07 -3.96479840e-07 -6.28163762e-06]
# 4.444444444444445  [ 7.83901503e-07  1.35129261e-07 -6.28225465e-06]
# 5.555555555555555  [-7.83024300e-07  1.40316485e-07 -6.28253991e-06]
# 6.666666666666667  [ 6.87694670e-07 -4.00209889e-07 -6.28269444e-06]
# 7.777777777777779  [-5.09423426e-07  6.10885408e-07 -6.28278718e-06]
# 8.88888888888889  [ 2.69705439e-07 -7.48578545e-07 -6.28284692e-06]
# 10.0  [ 2.54119994e-09  7.95438886e-07 -6.28288741e-06]
