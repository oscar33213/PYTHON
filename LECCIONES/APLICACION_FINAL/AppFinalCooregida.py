from tkinter import *
from tkinter import messagebox
import sqlite3
import os

#--------------------------FUNCIONES--------------------------------

#CREAR BBDD
def ConectionBD():
    miBase = sqlite3.connect("Usuarios")
    miCursor = miBase.cursor()
    try:
        miCursor.execute('''
            CREATE TABLE IF NOT EXISTS DATOSUSUARIOS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                NOMBRE_USUARIO VARCHAR(100),
                APELLIDO_USUARIO VARCHAR(100),
                PASSWORD VARCHAR(50),
                DIRECCION VARCHAR(100),
                COMENTARIO VARCHAR(200)
            )
        ''')
        messagebox.showinfo("BBDD", "Base de Datos creada con exito")
    except Exception as e:
        messagebox.showwarning("ERROR", f"Error creando la Base de Datos: {e}")

#SALIR APP
def SalirApp():
    valor = messagebox.askquestion("Salir", "¿Deseas salir?")
    if valor == "yes":
        root.destroy()

#CREAR REGISTRO
def CrearRegistro():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    try:
        miCursor.execute(
            "INSERT INTO DATOSUSUARIOS (ID, NOMBRE_USUARIO, APELLIDO_USUARIO, PASSWORD, DIRECCION, COMENTARIO) VALUES (NULL, ?, ?, ?, ?, ?)",
            (cuadroNombre.get(), cuadroApellido.get(), cuadroPass.get(), cuadroDireccion.get(), textoComentario.get("1.0", "end-1c"))
        )
        miConexion.commit()
        messagebox.showinfo("BBDD", "Registro añadido correctamente")
    except Exception as e:
        miConexion.rollback()
        messagebox.showerror("BBDD", f"Error al añadir registro: {e}")
    finally:
        miConexion.close()

#LIMPIAR CAMPOS
def LimpiarCampos():
    miId.set("")
    Nombre.set("")
    Apellido.set("")
    Passw.set("")
    Adrees.set("")
    textoComentario.delete(1.0, END)

#LEER REGISTROS
def leerRegistros():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT * FROM DATOSUSUARIOS WHERE ID = ?", (miId.get(),))
    elUsuario = miCursor.fetchall()
    for usuario in elUsuario:
        miId.set(usuario[0])
        Nombre.set(usuario[1])
        Apellido.set(usuario[2])
        Passw.set(usuario[3])
        Adrees.set(usuario[4])
        textoComentario.insert(1.0, usuario[5]) # Corregido para insertar el comentario en el campo correcto
    miConexion.commit()
    miConexion.close()

#ACTUALIZAR REGISTRO
def actualizarRegistro():
    miConexion = sqlite3.connect("Usuarios")
    miCursor = miConexion.cursor()
    miCursor.execute("UPDATE DATOSUSUARIOS SET NOMBRE_USUARIO = '" + Nombre.get() + 
                     "', APELLIDO_USUARIO = '" + Apellido.get() + 
                     "', PASSWORD = '" + Passw.get() + 
                     "', DIRECCION = '" + Adrees.get() + 
                     "', COMENTARIO = '" + textoComentario.get(1.0, "end-1c") + 
                     "' WHERE ID = " + miId.get())
    messagebox.showinfo("Actualizado", "Registro actualizado con exito")
    miConexion.commit()
    miConexion.close() # Asegurarse de cerrar la conexión
    

def EliminarRegistro():
    eliminar = messagebox.askyesno("Eliminar Registro", "¿Desea eliminar el registro?")
    
    if eliminar:
        miConexion = sqlite3.connect("Usuarios")
        miCursor = miConexion.cursor()
        try:
            miCursor.execute("DELETE FROM DATOSUSUARIOS WHERE ID = ?", (miId.get(),))
            miConexion.commit()
            messagebox.showinfo("Eliminar registro", "El registro ha sido eliminado correctamente")
        except Exception as e:
            miConexion.rollback()
            messagebox.showerror("Error", f"No se pudo eliminar el registro: {e}")
        finally:
            miConexion.close()
    else:
        messagebox.showinfo("Operación Cancelada", "No se ha eliminado el registro.")


#ELIMINAR BBDD
def BorrarBDD():
    eliminar = messagebox.askyesno("Eliminar Base de Datos", "¿Desea eliminar la Base de Datos?")
    if eliminar:
        try:
            os.remove("Usuarios")
            messagebox.showinfo("Base de Datos Eliminada", "La base de datos ha sido eliminada exitosamente.")
        except FileNotFoundError:
            messagebox.showerror("Error", "La base de datos no existe.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar la base de datos: {e}")
    else:
        messagebox.showinfo("Operación Cancelada", "No se ha eliminado la base de datos.")

root = Tk()
root.title("Aplicación")
#-----------------------CREACION DE MENUS-----------------------------
barraMenu = Menu(root)
root.config(menu=barraMenu, width=300, height=300)

BBDDMenu = Menu(barraMenu, tearoff=0)
BBDDMenu.add_command(label="Conectar", command=ConectionBD)
BBDDMenu.add_command(label="Salir", command=SalirApp)

Deletemenu = Menu(barraMenu, tearoff=0)
Deletemenu.add_command(label="Borrar Campos", command=LimpiarCampos)

CRUDMenu = Menu(barraMenu, tearoff=0)
CRUDMenu.add_command(label="Crear Registro", command=CrearRegistro)
CRUDMenu.add_command(label="Leer Registro", command=leerRegistros) # Añadir la función de lectura
CRUDMenu.add_command(label="Actualizar Registro", command=actualizarRegistro)
CRUDMenu.add_command(label="Borrar Registro", command=EliminarRegistro)

HelpMenu = Menu(barraMenu, tearoff=0)
HelpMenu.add_command(label="Acerca de:")

barraMenu.add_cascade(label="Base De Datos", menu=BBDDMenu)
barraMenu.add_cascade(label="Borrar", menu=Deletemenu)
barraMenu.add_cascade(label="CRUD", menu=CRUDMenu)
barraMenu.add_cascade(label="Ayuda", menu=HelpMenu)

#---------------------FORMULARIO-------------------------
miFrame = Frame(root)
miFrame.pack()

miId = StringVar()
Nombre = StringVar()
Apellido = StringVar() # Corregir paréntesis
Passw = StringVar()
Adrees = StringVar()

cuadroID = Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre = Entry(miFrame, textvariable=Nombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

cuadroApellido = Entry(miFrame, textvariable=Apellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroPass = Entry(miFrame, textvariable=Passw)
cuadroPass.grid(row=3, column=1, padx=10, pady=10)
cuadroPass.config(show="*")

cuadroDireccion = Entry(miFrame, textvariable=Adrees)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

textoComentario = Text(miFrame, width=16, height=5)
textoComentario.grid(row=5, column=1, padx=10, pady=10)

#-----------------------BARRA DESPLAZAMIENTO-----------------
scrollVert = Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)

#------------------- AGREGAMOS LABEL-------------------
ID = Label(miFrame, text="ID")
ID.grid(row=0, column=0, sticky="e", padx=10, pady=10)

Name = Label(miFrame, text="Nombre")
Name.grid(row=1, column=0, sticky="e", padx=10, pady=10)

Surname = Label(miFrame, text="Apellido")
Surname.grid(row=2, column=0, sticky="e", padx=10, pady=10)

Pass = Label(miFrame, text="Contraseña")
Pass.grid(row=3, column=0, sticky="e", padx=10, pady=10)

Adress = Label(miFrame, text="Dirección")
Adress.grid(row=4, column=0, sticky="e", padx=10, pady=10)

Comments = Label(miFrame, text="Comentario")
Comments.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#-------------------BOTONES----------------------
miFrame2 = Frame(root)
miFrame2.pack()
BotonCrear = Button(miFrame2, text="Crear", width=10, command=CrearRegistro)
BotonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)
BotonRead = Button(miFrame2, text="Leer", width=10, command=leerRegistros)
BotonRead.grid(row=1, column=1, sticky="e", padx=10, pady=10)
BotonUpdate = Button(miFrame2, text="Actualizar", width=10, command=actualizarRegistro)
BotonUpdate.grid(row=1, column=2, sticky="e", padx=10, pady=10)
BotonDelete = Button(miFrame2, text="Borrar BBDD", width=10, command=BorrarBDD)
BotonDelete.grid(row=1, column=3, sticky="e", padx=10, pady=10)

root.mainloop()
