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


class GUI:
    def __init__(self):
        self.envelope = None
        self.root = tk.Tk()  # 创建主窗体
        self.root.protocol("WM_DELETE_WINDOW", lambda: exit(0))

        self.f = plt.figure(num=2, figsize=(16, 12), dpi=60, facecolor="white", edgecolor='green',
                            frameon=True)  # 创建绘图对象f
        self.canvas = FigureCanvasTkAgg(self.f, self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.X, side=tk.BOTTOM)

        self.stepVar = tk.Variable()
        self.stepVar.set(str(0.01))
        self.stepLabel = tk.Label(self.frame, text='step')
        self.stepLabel.grid(row=0, column=0)
        self.stepEntries = tk.Entry(self.frame, textvariable=self.stepVar)
        self.stepEntries.grid(row=1, column=0, rowspan=2)

        self.QG0 = -4.37
        self.QG1 = 5.39
        self.CD1ang = 15.0
        self.CD1n = 5.9
        self.CD2n = -22.9
        self.gap = 0.3

        self.QG0var = tk.Variable()
        self.QG1var = tk.Variable()
        self.CD1angvar = tk.Variable()
        self.CD1nvar = tk.Variable()
        self.CD2nvar = tk.Variable()
        self.gapvar = tk.Variable()

        self.QG0var.set(str(self.QG0))
        self.QG1var.set(str(self.QG1))
        self.CD1angvar.set(str(self.CD1ang))
        self.CD1nvar.set(str(self.CD1n))
        self.CD2nvar.set(str(self.CD2n))
        self.gapvar.set(str(self.gap))

        tk.Label(self.frame, text='QG0').grid(row=0, column=1)
        tk.Label(self.frame, text='QG1').grid(row=0, column=3)
        tk.Label(self.frame, text='CD1ang').grid(row=0, column=5)
        tk.Label(self.frame, text='CD1n').grid(row=0, column=7)
        tk.Label(self.frame, text='CD2n').grid(row=0, column=9)
        tk.Label(self.frame, text='gap').grid(row=0, column=11)

        tk.Entry(self.frame, textvariable=self.QG0var).grid(row=1, column=1, rowspan=2)
        tk.Entry(self.frame, textvariable=self.QG1var).grid(row=1, column=3, rowspan=2)
        tk.Entry(self.frame, textvariable=self.CD1angvar).grid(row=1, column=5, rowspan=2)
        tk.Entry(self.frame, textvariable=self.CD1nvar).grid(row=1, column=7, rowspan=2)
        tk.Entry(self.frame, textvariable=self.CD2nvar).grid(row=1, column=9, rowspan=2)
        tk.Entry(self.frame, textvariable=self.gapvar).grid(row=1, column=11, rowspan=2)

        QG0add = lambda: self.QG0var.set(
            str(round(float(self.QG0var.get()) + float(self.stepVar.get()), 5))) == None and self.updateDate() == None
        QG1add = lambda: self.QG1var.set(
            str(round(float(self.QG1var.get()) + float(self.stepVar.get()), 5))) == None and self.updateDate() == None
        CD1angadd = lambda: self.CD1angvar.set(
            str(round(float(self.CD1angvar.get()) + float(self.stepVar.get()),
                      5))) == None and self.updateDate() == None
        CD1nadd = lambda: self.CD1nvar.set(
            str(round(float(self.CD1nvar.get()) + float(self.stepVar.get()), 5))) == None and self.updateDate() == None
        CD2nadd = lambda: self.CD2nvar.set(
            str(round(float(self.CD2nvar.get()) + float(self.stepVar.get()), 5))) == None and self.updateDate() == None
        gapadd = lambda: self.gapvar.set(
            str(round(float(self.gapvar.get()) + float(self.stepVar.get()), 5))) == None and self.updateDate() == None

        QG0sub = lambda: self.QG0var.set(
            str(round(float(self.QG0var.get()) - float(self.stepVar.get()), 5))) == None and self.updateDate() == None
        QG1sub = lambda: self.QG1var.set(
            str(round(float(self.QG1var.get()) - float(self.stepVar.get()), 5))) == None and self.updateDate() == None
        CD1angsub = lambda: self.CD1angvar.set(
            str(round(float(self.CD1angvar.get()) - float(self.stepVar.get()),
                      5))) == None and self.updateDate() == None
        CD1nsub = lambda: self.CD1nvar.set(
            str(round(float(self.CD1nvar.get()) - float(self.stepVar.get()), 5))) == None and self.updateDate() == None
        CD2nsub = lambda: self.CD2nvar.set(
            str(round(float(self.CD2nvar.get()) - float(self.stepVar.get()), 5))) == None and self.updateDate() == None
        gapsub = lambda: self.gapvar.set(
            str(round(float(self.gapvar.get()) - float(self.stepVar.get()), 5))) == None and self.updateDate() == None

        tk.Button(self.frame, text='+', command=QG0add).grid(row=1, column=2)
        tk.Button(self.frame, text='+', command=QG1add).grid(row=1, column=4)
        tk.Button(self.frame, text='+', command=CD1angadd).grid(row=1, column=6)
        tk.Button(self.frame, text='+', command=CD1nadd).grid(row=1, column=8)
        tk.Button(self.frame, text='+', command=CD2nadd).grid(row=1, column=10)
        tk.Button(self.frame, text='+', command=gapadd).grid(row=1, column=12)

        tk.Button(self.frame, text='-', command=QG0sub).grid(row=2, column=2)
        tk.Button(self.frame, text='-', command=QG1sub).grid(row=2, column=4)
        tk.Button(self.frame, text='-', command=CD1angsub).grid(row=2, column=6)
        tk.Button(self.frame, text='-', command=CD1nsub).grid(row=2, column=8)
        tk.Button(self.frame, text='-', command=CD2nsub).grid(row=2, column=10)
        tk.Button(self.frame, text='-', command=gapsub).grid(row=2, column=12)

        self.root.mainloop()

    def updateDate(self):
        self.envelope = transport.trans(QGO=float(self.QG0var.get()), QG1=float(self.QG1var.get()),
                                        CD1ang=float(self.CD1angvar.get()),
                                        CD1n=float(self.CD1nvar.get()), CD2n=float(self.CD2nvar.get()),
                                        gap=float(self.gapvar.get()))
        self.prepare()
        self.canvas.draw()  # 以前的版本使用show()方法，matplotlib 2.2之后不再推荐show（）用draw代替，但是用show不会报错，会显示警告
        self.root.update()

    def prepare(self):
        x = np.array(self.envelope[0])
        y1 = np.array(self.envelope[1])
        y2 = np.array(self.envelope[2])
        y3 = np.array(self.envelope[3])

        self.f.clf()
        fig1 = plt.subplot(1, 1, 1)  # 创建一副子图

        fig1.plot(x, y1, color='black', linewidth=2, linestyle='-')
        fig1.plot(x, y2, color='black', linewidth=2, linestyle='-')
        fig1.plot(x, y3, color='red', linewidth=2, linestyle='--')

        # fig1.set_title("这是第一幅图", loc='center', pad=20, fontsize='xx-large', color='red')  # 设置标题
        # line1.set_label("正弦曲线")  # 确定图例
        # fig1.legend(['正弦', '余弦'], loc='upper left', facecolor='green', frameon=True, shadow=True, framealpha=0.5,
        #             fontsize='xx-large')

        fig1.set_xlabel('xy/mm')  # 确定坐标轴标题
        fig1.set_ylabel('s/m')
        # fig1.set_yticks([-1, -1 / 2, 0, 1 / 2, 1])  # 设置坐标轴刻度
        # fig1.grid(which='major', axis='x', color='r', linestyle='-', linewidth=2)  # 设置网格


gui = GUI()
