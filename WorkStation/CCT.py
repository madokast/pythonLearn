import numpy as np


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


# TODO 毕奥-萨伐尔定律


class Solenoid:
    def __init__(self, r, w, I, stepTheta):
        """
        直螺线管建模
        :param r: 半径
        :param w: 相邻导线的距离 (轴向)
        :param I: 电流
        :param stepTheta: θ步长，影响磁场计算精度
        """
        self.r = r
        self.w = w
        self.I = I
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


# 以下为测试代码
s = Solenoid(1, 1, 1)
print(s.point(0.0))
print(s.point(np.pi / 6))
print(s.point(np.pi / 3))
print(s.point(np.pi))
