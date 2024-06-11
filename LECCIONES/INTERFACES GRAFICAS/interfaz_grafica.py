from tkinter import *

# Crear la ventana principal
raiz = Tk()

# Configurar la ventana principal
raiz.title("Ventana de Pruebas")
raiz.resizable(1, 1)  # (HEIGHT, WIDTH) 1 = Sí, 0 = No
raiz.iconbitmap("bobomb.ico")

#raiz.geometry("650x350") #TAMAÑO VENTANA

raiz.config(bg="red")
raiz.config(relief="raised")
raiz.config(bd=30)

#CREAMOS EL FRAME
miFrame = Frame()
#EMPAQUETAMOS EL FRAME A LA RAIZ
miFrame.pack(side="right", anchor="n") #INDICAMOS DONDE SE ANCLARA EL FRAME

#miFrame.pack(fill="both", expand="true")

miFrame.config(bg="blue")

miFrame.config(width="650", height="350")
miFrame.config(bd=40)
miFrame.config(relief="sunken")

miFrame.config(cursor="pirate") #CAMBIAR EL CURSOR



# Iniciar el bucle principal de la ventana
raiz.mainloop()  # <= Siempre al final



