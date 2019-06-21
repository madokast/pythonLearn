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
        self.root = tk.Tk()  # 创建主窗体
        # self.canvas = tk.Canvas()  # 创建一块显示图形的画布
        # self.figure = self.create_matplotlib()  # 返回matplotlib所画图形的figure对象
        # self.create_form(self.figure)  # 将figure显示在tkinter窗体上面

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

        QG0add = lambda: self.QG0var.set(str(round(float(self.QG0var.get()) + float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None
        QG1add = lambda: self.QG1var.set(str(round(float(self.QG1var.get()) + float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None
        CD1angadd = lambda: self.CD1angvar.set(str(round(float(self.CD1angvar.get()) + float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None
        CD1nadd = lambda: self.CD1nvar.set(str(round(float(self.CD1nvar.get()) + float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None
        CD2nadd = lambda: self.CD2nvar.set(str(round(float(self.CD2nvar.get()) + float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None
        gapadd = lambda: self.gapvar.set(str(round(float(self.gapvar.get()) + float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None

        QG0sub = lambda: self.QG0var.set(str(round(float(self.QG0var.get()) - float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None
        QG1sub = lambda: self.QG1var.set(str(round(float(self.QG1var.get()) - float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None
        CD1angsub = lambda: self.CD1angvar.set(str(round(float(self.CD1angvar.get()) - float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None
        CD1nsub = lambda: self.CD1nvar.set(str(round(float(self.CD1nvar.get()) - float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None
        CD2nsub = lambda: self.CD2nvar.set(str(round(float(self.CD2nvar.get()) - float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None
        gapsub = lambda: self.gapvar.set(str(round(float(self.gapvar.get()) - float(self.stepVar.get()),5))) == None and transport.trans(QGO=float(self.QG0var.get()),QG1=float(self.QG1var.get()),CD1ang=float(self.CD1angvar.get()),CD1n=float(self.CD1nvar.get()),CD2n=float(self.CD2nvar.get()),gap=float(self.gapvar.get())) == None

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


gui = GUI()
