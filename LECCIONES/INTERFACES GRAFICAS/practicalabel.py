from tkinter import *

root = Tk()
root.title("PRACTICAS LABEL")
miFrame = Frame(root, width="500", height="400")

miFrame.pack()

miImagen = PhotoImage(file="tkinter1.png")



#miLabel = Label(miFrame, text="Hola Mundo", fg="grey", font=("Comic Sans MS", 20))

Label(miFrame, image=miImagen).place(x=100, y=200) #DE ESTA MANERA EL LABEL RESPETA EL TAMAÑO ORIGINAL, SE LE DEBERAN INDICAR COORDENADAS



root.mainloop()

