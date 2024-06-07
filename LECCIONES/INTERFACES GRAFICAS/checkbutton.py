from tkinter import *

root = Tk()
root.title("CheckButton")

playa = IntVar()
montanya = IntVar()
ciudad = IntVar()

def opcionesVia():
    opcionEscogida = ""
    
    if playa.get() == 1:
        opcionEscogida += "Playa "
    if montanya.get() == 1:
        opcionEscogida += "Montaña "
    if ciudad.get() == 1:
        opcionEscogida += "Ciudad "
    
    textoFinal.config(text=opcionEscogida)
    
    
try:
    foto = PhotoImage(file="tkinter1.png")
    Label(root, image=foto).pack()
except:
    print("Error: No se pudo cargar la imagen.")
    
frame = Frame(root)
frame.pack()

Label(frame, text="Elige destino", width=50).pack()
Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesVia).pack()
Checkbutton(frame, text="Montaña", variable=montanya, onvalue=1, offvalue=0, command=opcionesVia).pack()
Checkbutton(frame, text="Ciudad", variable=ciudad, onvalue=1, offvalue=0, command=opcionesVia).pack()


textoFinal = Label(frame)
textoFinal.pack()
root.mainloop()
