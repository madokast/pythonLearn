import tkinter as tk

window = tk.Tk()
frameDown = tk.Frame(window)
frameDown.pack(fill=tk.X, side=tk.BOTTOM)

entry = tk.Entry()

button = tk.Button(window,text='+')

tk.mainloop()
