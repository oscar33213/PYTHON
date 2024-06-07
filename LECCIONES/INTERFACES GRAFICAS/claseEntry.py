from tkinter import *

# Crear la ventana principal
root = Tk()
root.title("PRACTICA ENTRY")

# Crear una variable de tipo StringVar para almacenar el texto del campo de nombre
minombre = StringVar()

# Crear y configurar el frame
miFrame = Frame(root, width=1200, height=600)
miFrame.pack()

# Crear un campo de texto para el nombre, enlazado con la variable minombre
cuadroNombre = Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="center")  # Configurar el color del texto y la alineación

# Crear un campo de texto para la contraseña
cuadroPass = Entry(miFrame)
cuadroPass.grid(row=1, column=1, padx=10, pady=10)
cuadroPass.config(show="X")  # Configurar para que la contraseña se muestre como "X"

# Crear un campo de texto para el apellido
cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

# Crear un campo de texto para la dirección
cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

# Crear un área de texto para comentarios
cuadroTexto = Text(miFrame, width=16, height=5)
cuadroTexto.grid(row=4, column=1, padx=10, pady=10)

# Crear una barra de desplazamiento para el área de texto
barraLateral = Scrollbar(miFrame, command=cuadroTexto.yview)
barraLateral.grid(row=4, column=2, sticky="nsew")  # Ajustar la barra de desplazamiento con sticky

# Configurar el área de texto para usar la barra de desplazamiento
cuadroTexto.config(yscrollcommand=barraLateral.set)

# Crear etiquetas para cada campo de texto
nombreLabel = Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Password: ")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

ApeelidoLabel = Label(miFrame, text="Apellido: ")
ApeelidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

Direccion = Label(miFrame, text="Direccion: ")
Direccion.grid(row=3, column=0, sticky="e", padx=10, pady=10)

Comentarios = Label(miFrame, text="Comentarios")
Comentarios.grid(row=4, column=0, sticky="e", padx=10, pady=10)

# Definir una función que se ejecutará cuando se presione el botón
def codigoBoton():
    minombre.set("Oscar")  # Establecer el texto del campo de nombre a "Oscar"

# Crear un botón y enlazarlo con la función codigoBoton
BotonEnvio = Button(root, text="Enviar", command=codigoBoton)
BotonEnvio.pack()

# Ejecutar el bucle principal de la aplicación
root.mainloop()


