import math
import numpy as np
# -------------------------------------------------------------------------------------------
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk  # NavigationToolbar2TkAgg
# ------------------------------------------------------------------------------------------
import tkinter as tk
# ------------------------------------------------------------------------------------------
import transport

mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
mpl.rcParams['axes.unicode_minus'] = False  # 负号显示


class From:
    def __init__(self):
        self.root = tk.Tk()  # 创建主窗体
        # self.canvas = []  # 创建一块显示图形的画布.  谁写的？ 垃圾代码！
        # self.figure = self.create_matplotlib()  # 返回matplotlib所画图形的figure对象
        self.create_form(self.create_matplotlib(), self.root)  # 将figure显示在tkinter窗体上面
        self.envalope = transport.trans(QGO=-4.3737, QG1=5.398396, CD1ang=15.0, CD1n=5.9, CD2n=-22.9, gap=0.3)

        self.buttom = tk.Button(self.root, text='ok', command= self.create_matplotlib()==None)
        self.buttom.pack(fill=tk.X, side=tk.BOTTOM)

        self.root.mainloop()

    def create_matplotlib(self):
        # 创建绘图对象f
        f = plt.figure(num=2, figsize=(16, 12), dpi=60, facecolor="white", edgecolor='green', frameon=True)
        # 创建一副子图
        fig1 = plt.subplot(1, 1, 1)

        envalope = transport.trans(QGO=-4.3737, QG1=5.398396, CD1ang=15.0, CD1n=5.9, CD2n=-22.9, gap=0.3)
        x = np.array(envalope[0])
        y1 = np.array(envalope[1])
        y2 = np.array(envalope[2])
        y3 = np.array(envalope[3])

        line1, = fig1.plot(x, y1, color='red', linewidth=3, linestyle='--')  # 画第一条线
        line2, = fig1.plot(x, y2, color='black', linewidth=3, linestyle='-', alpha=0.3)
        line3, = fig1.plot(x, y3, color='black', linewidth=3, linestyle='-', alpha=0.3)
        # plt.setp(line2, color='black', linewidth=3, linestyle='-', alpha=0.3)  # 华第二条线
        # plt.setp(line3, color='blue', linewidth=3, linestyle='-', alpha=0.3)  # 华第3条线

        # fig1.set_title("这是第一幅图", loc='center', pad=20, fontsize='xx-large', color='red')  # 设置标题
        # line1.set_label("正弦曲线")  # 确定图例
        # fig1.legend(['正弦', '余弦'], loc='upper left', facecolor='green', frameon=True, shadow=True, framealpha=0.5,
        #             fontsize='xx-large')

        fig1.set_xlabel('横坐标')  # 确定坐标轴标题
        fig1.set_ylabel("纵坐标")
        # fig1.set_yticks([-1, -1 / 2, 0, 1 / 2, 1])  # 设置坐标轴刻度
        # fig1.grid(which='major', axis='x', color='r', linestyle='-', linewidth=2)  # 设置网格

        return f

    @classmethod
    def create_form(cls, figure, root):
        # 把绘制的图形显示到tkinter窗口上
        canvas = FigureCanvasTkAgg(figure, root)
        canvas.draw()  # 以前的版本使用show()方法，matplotlib 2.2之后不再推荐show（）用draw代替，但是用show不会报错，会显示警告
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)


if __name__ == "__main__":
    form = From()
