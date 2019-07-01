import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


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

    # 计算速度有点慢啊 可以优化
    return (10.0 ** -7) * I * (np.cross(p01, r)) / (rr ** 3)


def plot(cctList, box=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]):
    """
    画图，想画几个cct就画几个
    :param cctList: 一个[] 里面装了cct类的实例
    :param box: 设定范围[xmin,xmax,ymin,ymax,zmin,zmax]
        当cct超出所设定范围时，无效
        需要吐槽，matplotlib三维画图似乎无法设定坐标轴范围!
    :return:
    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    for cct in cctList:
        stepTheta = np.pi / 360.0  # 步长固定为1°画个图而已
        end = cct.getN() * 2.0 * np.pi
        num = int(end / stepTheta)
        x = [0] * num
        y = [0] * num
        z = [0] * num
        i = 0
        for th in np.linspace(0, end, num):
            p0 = cct.point(th)
            x[i] = p0[0]
            y[i] = p0[1]
            z[i] = p0[2]
            i = i + 1

        ax.plot(x, y, z, zdir='x')

    if True:  # 便于折叠
        xmin = box[0]
        xmax = box[1]
        ymin = box[2]
        ymax = box[3]
        zmin = box[4]
        zmax = box[5]
        ax.plot([xmin], [ymin], [zmin], 'w')
        ax.plot([xmax], [ymax], [zmax], 'w')

    plt.show()


class Solenoid:
    """
    螺线管建模
    没有实际用处，只是作为代码正确性验证手段
    本来想先写个抽象类的..
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

        self.p = np.array([0.0, 0.0, 0.0])  # 位置
        self.azim = 0.0  # 方位角，这里固定以 y 为旋转轴，azim=0 表示z轴正方向，azim>0 表示往x轴的正向旋转
        self.azimR = np.array([
            [np.cos(self.azim), 0.0, np.sin(self.azim)],
            [0.0, 1.0, 0.0],
            [-np.sin(self.azim), 0.0, np.cos(self.azim)]
        ])  # 旋转矩阵

    def setPosition(self, p):
        """
        设置元件的位置
        所谓元件的位置，即线圈绕制时，导线初始点所对应的圆柱横截圆面的圆心
        具体可见文档
        默认值 np.array([0.0, 0.0, 0.0])
        :param p: 新原点 np.array() 数据
        """
        self.p = p

    def setAzimuth(self, azim):
        """
        设置元件的方位，注意元件只能在 xz 轴上旋转（这仅仅是为了编程方便而已
        所谓元件的方位，就是线圈的轴向方向，正方向为绕制时线圈增长方法
        默认值为 0.0 即z轴正向
        azim>0 时，向x轴正方向旋转，即从y轴正向往下看，元件做逆时针旋转。例如 azim =pi/2时，方向即为x正方向
        :param azim: 方位角 弧度制 float 数据
        """
        self.azim = azim
        self.azimR = np.array([
            [np.cos(self.azim), 0.0, np.sin(self.azim)],
            [0.0, 1.0, 0.0],
            [-np.sin(self.azim), 0.0, np.cos(self.azim)]
        ])

    def point(self, theta):
        """
        计算θ位置对应的点坐标
        注意坐标为笛卡尔直角坐标系
        当元件位置处于坐标轴原点且方位角为0时：
        螺线管轴向为 z 轴，从z=0开始正向生长
        θ=0 时，x=-r y=0 ，朝向 z 轴正方向，随 θ 增大，线圈顺时针转动
        具体可以参考文档AGCCT
        :param theta: 唯一的一个自变量θ
        :return: θ位置对应的点坐标
        """
        rr = np.array([-self.r * np.cos(theta), self.r * np.sin(theta), 0.0])
        zz = np.array([0.0, 0.0, self.w / (2 * np.pi) * theta])
        p = np.matmul(self.azimR, (rr + zz).T).T + self.p
        return p

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


class CCT:
    def __init__(self, r, w, n, I, tiltAngle, nth, stepTheta):
        """
        CCT 建模
        :param r: 半径
        :param w: 相邻导线的距离 (轴向)
        :param n: 总匝数 n
        :param I: 电流
        :param stepTheta: θ步长，影响磁场计算精度
        :param tiltAngle: 倾斜角，见文档
        :param nth: 绕线方式 n=1 二极场 / n=2 四机场
        """
        self.r = r
        self.w = w
        self.I = I
        self.n = n
        self.stepTheta = stepTheta
        self.tA = tiltAngle
        self.nth = nth

        self.p = np.array([0.0, 0.0, 0.0])  # 位置
        self.azim = 0.0  # 方位角，这里固定以 y 为旋转轴，azim=0 表示z轴正方向，azim>0 表示往x轴的正向旋转
        self.azimR = np.array([
            [np.cos(self.azim), 0.0, np.sin(self.azim)],
            [0.0, 1.0, 0.0],
            [-np.sin(self.azim), 0.0, np.cos(self.azim)]
        ])  # 旋转矩阵

    def setPosition(self, p):
        """
        设置元件的位置
        所谓元件的位置，即线圈绕制时，导线初始点所对应的圆柱横截圆面的圆心
        具体可见文档
        默认值 np.array([0.0, 0.0, 0.0])
        :param p: 新原点 np.array() 数据
        """
        self.p = p

    def setAzimuth(self, azim):
        """
        设置元件的方位，注意元件只能在 xz 轴上旋转（这仅仅是为了编程方便而已
        所谓元件的方位，就是线圈的轴向方向，正方向为绕制时线圈增长方法
        默认值为 0.0 即z轴正向
        azim>0 时，向x轴正方向旋转，即从y轴正向往下看，元件做逆时针旋转。例如 azim =pi/2时，方向即为x正方向
        :param azim: 方位角 弧度制 float 数据
        """
        self.azim = azim
        self.azimR = np.array([
            [np.cos(self.azim), 0.0, np.sin(self.azim)],
            [0.0, 1.0, 0.0],
            [-np.sin(self.azim), 0.0, np.cos(self.azim)]
        ])

    def getN(self):
        return self.n

    def point(self, theta):
        """
        计算θ位置对应的点坐标
        注意坐标为笛卡尔直角坐标系
        当元件位置处于坐标轴原点且方位角为0时：
        螺线管轴向为 z 轴，从z=0开始正向生长
        θ=0 时，x=-r y=0 ，朝向 z 轴正方向，随 θ 增大，线圈顺时针转动
        具体可以参考文档AGCCT
        :param theta: 唯一的一个自变量θ
        :return: θ位置对应的点坐标
        """
        p0 = np.array([-self.r * np.cos(theta), self.r * np.sin(theta),
                       (self.r / np.tan(self.tA) / self.nth * np.sin(self.nth * theta)) + (
                               self.w / (2 * np.pi) * theta)])
        p = np.matmul(self.azimR, p0.T).T + self.p
        return p

    def magnet(self, p):
        """
        计算 p 点磁场
        :param p: np.array() 量
        :return: p 点磁场 np.array() 量
        """
        B = np.array([0, 0, 0])
        end = self.n * 2.0 * np.pi - self.stepTheta
        num = int(end / self.stepTheta)
        # 这里的for循环 要想办法矩阵化
        for th in np.linspace(0, end, num):
            p0 = self.point(th)
            p1 = self.point(th + self.stepTheta)
            B = B + deltaB(p0, p1, self.I, p)

        return B

    @DeprecationWarning
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
        # ax.plot([1], [1], [0])

        plt.show()

    def printTheoreticalValues(self):
        """
        打印一些理论值
        """
        miu0 = 4 * np.pi / 10 ** 7

        if np.abs(self.nth - 1.0) < 1e-7:
            print("这应该也许是个二极场CCT吧")
            print("理论By = " + str(-miu0 * self.I / 2.0 / self.w / np.tan(self.tA)))
        elif np.abs(self.nth - 2.0) < 1e-7:
            print("这应该也许是个四极场CCT吧")
            print("理论梯度G = " + str(-miu0 * self.I / 2.0 / self.w / np.tan(self.tA) / self.r))

        print("理论Bz = " + str(miu0 * self.I / self.w))


# 以下为测试代码

cct = CCT(25e-3, 6.96e-3, 75, 1.0, np.pi / 9.0, 1, np.pi / 180.0)
cct1 = CCT(25e-3, 6.96e-3, 75, 1.0, -np.pi / 9.0, 1, np.pi / 180.0)
cct1.setPosition(np.array([0.2, 0.0, 0.0]))
axis = 0.5
plot([cct1, cct], [-axis, axis, -axis, axis, -axis, axis])

# 2019年7月1日 四极场CCT测试通过了!!
# for i in np.linspace(-1, 3, 10):
#     print(str(cct.magnet(np.array([0, 0, i]))))
# print('----------------')
# for i in np.linspace(-1, 3, 10):
#     print(str(cct.magnet(np.array([0, -0.01, i]))))
# print('----------------')
# for i in np.linspace(-1, 3, 10):
#     print(str(cct.magnet(np.array([0, 0.01, i]))))
# 理论值 0.00108827961T
# [ 5.25934039e-10  8.78163175e-09 -2.80243593e-07]
# [ 2.91803370e-09  2.97525526e-08 -9.79559438e-07]
# [-1.45258216e-07  1.78035519e-07 -2.14051134e-05]
# [ 9.89045718e-09 -8.53657421e-08 -1.22655503e-04]
# [ 8.07490337e-10 -2.29472113e-08 -1.24922845e-04]
# [-8.39503918e-10 -2.28989234e-08 -1.24922818e-04]
# [-1.06164604e-08 -8.44756452e-08 -1.22655092e-04]
# [ 1.57464426e-07  1.87707027e-07 -2.13998905e-05]
# [-2.81521872e-09  2.99329656e-08 -9.79463454e-07]
# [-5.15923350e-10  8.81056315e-09 -2.80227045e-07]
# ----------------
# [ 8.22926338e-10  5.74257152e-09 -2.80290435e-07]
# [ 2.71893985e-09  1.13553131e-08 -9.79579257e-07]
# [-7.47469640e-09 -1.06813142e-06 -2.12844808e-05]
# [ 1.09005854e-05  1.70760328e-08 -1.22661397e-04]
# [ 1.08807958e-05  1.61937466e-07 -1.24923148e-04]
# [ 1.08789874e-05  1.72016979e-07 -1.24922820e-04]
# [ 1.08779917e-05  1.91803814e-07 -1.22657160e-04]
# [ 3.12565592e-07  1.50520703e-06 -2.13746346e-05]
# [-3.57847552e-09  4.84569934e-08 -9.78425880e-07]
# [-3.20869371e-10  1.18609057e-08 -2.80085859e-07]
# ----------------
# [ 2.28786573e-10  1.18178305e-08 -2.80102763e-07]
# [ 3.11489283e-09  4.81221350e-08 -9.78526128e-07]
# [-2.84817524e-07  1.43475242e-06 -2.13817922e-05]
# [-1.08808029e-05 -1.87658588e-07 -1.22657565e-04]
# [-1.08791813e-05 -2.07822794e-07 -1.24922846e-04]
# [-1.08806659e-05 -2.17805777e-07 -1.24923120e-04]
# [-1.08992190e-05 -3.60609017e-07 -1.22660948e-04]
# [ 4.12821280e-09 -1.11872670e-06 -2.12782715e-05]
# [-2.05012691e-09  1.13810086e-08 -9.79484980e-07]
# [-7.10834539e-10  5.75734443e-09 -2.80274108e-07]


# 2019年7月1日 二极场CCT测试通过了!!
# -1.0  [-6.10587573e-09 -2.32563670e-07 -2.90535117e-07]
# -0.5555555555555556  [-2.15574311e-08 -7.99342223e-07 -1.09315935e-06]
# -0.11111111111111116  [-5.82756805e-07  1.19649541e-05 -3.44793116e-05]
# 0.33333333333333326  [-8.61961431e-07  1.11064906e-04 -1.21714844e-04]
# 0.7777777777777777  [-9.31963089e-07  1.09427987e-04 -1.24889384e-04]
# 1.2222222222222223  [-9.33212986e-07  1.09427976e-04 -1.24889357e-04]
# 1.6666666666666665  [-8.77627630e-07  1.11064822e-04 -1.21714434e-04]
# 2.1111111111111107  [-2.56436432e-07  1.19592190e-05 -3.44740888e-05]
# 2.5555555555555554  [-2.59520152e-08 -7.99377941e-07 -1.09306337e-06]
# 3.0  [-6.88869388e-09 -2.32571053e-07 -2.90518568e-07]
# 理论值 By = 1.08828e-4  Bz = 1.2566e4


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
