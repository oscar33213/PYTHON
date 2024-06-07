from tkinter import *

root = Tk()

varOp = IntVar()

def imprimir():
    if varOp.get() == 1:
        etiqueta.config(text="Si")
    else:
        etiqueta.config(text="No")
        
Label(root, text="Eres tonto?").pack()

root.title("RADIO BUTTONS")

Radiobutton(root, text="Si", variable=varOp, value=1, command=imprimir).pack()
Radiobutton(root, text="No", variable=varOp, value=2, command=imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()

root.mainloop()
