import tkinter as tk

window = tk.Tk()
window.title("TRANSPORT")
window.geometry('800x600')
QG0 = tk.Variable()
QG0.set("-5.46165")
entry = tk.Entry(window, textvariable=QG0)
entry.pack()

QGOget = lambda: QG0.set('{: .5f}'.format(float(QG0.get())+0.001))
bottom = tk.Button(window,text="+",command=QGOget)
bottom.pack()

print(QG0.get())

window.mainloop()
