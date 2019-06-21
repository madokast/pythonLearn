import tkinter as tk

step = 0.001
varNumber = 0
window = tk.Tk()
window.title("TRANSPORT")
frameDown = tk.Frame(window)
frameDown.pack(fill=tk.X, side=tk.BOTTOM)


def addVar(name, val):
    global step
    global varNumber
    global frameDown
    varNumber += 1
    var = tk.Variable()
    var.set(str(val))
    QG0Label = tk.Label(frameDown, text=name)
    QG0Label.grid(row=0, column=varNumber * 2 - 1)
    entryVar = tk.Entry(frameDown, textvariable=var)
    entryVar.grid(row=1, column=varNumber * 2 - 1, rowspan=2)

    varAdd = lambda: var.set('{: .5f}'.format(float(var.get()) + step))
    varSub = lambda: var.set('{: .5f}'.format(float(var.get()) - step))

    bottomVarAdd = tk.Button(frameDown, text="+", command=varAdd)
    bottomVarAdd.grid(row=1, column=varNumber * 2)
    bottomVarSub = tk.Button(frameDown, text="-", command=varSub)
    bottomVarSub.grid(row=2, column=varNumber * 2)

    return var

stepLen = addVar("")



window.mainloop()
