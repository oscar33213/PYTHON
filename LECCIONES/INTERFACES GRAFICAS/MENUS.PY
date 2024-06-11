from tkinter import *
from tkinter import messagebox #LIBRERIA DE LAS VENTANAS EMERGENTES
from tkinter import filedialog

root = Tk()
#VENTANAS EMERGENTES

#FUNCION QUE CREA LAS VENTANAS EMERGENTES

def InfoAdd():
    messagebox.showinfo("Acerca de", "Oscar Hidalgo Llopez")
root.title("Menus")

def infoLicencia():
    messagebox.showwarning("Licencia", "Producto bajo licencia pirata")

def funSalir():
    valor = messagebox.askquestion("Salir" ,"¿Nos dejas? :(")
    
    if valor == "yes":
      valor1 =  messagebox.askokcancel("Salir", "¿Seguro?")
    
    if valor1 == True:
            root.destroy()
    

def cerrarDoc ():
    valor3 = messagebox.askretrycancel("Algo salio mal!", "Un elemento impide que el documento se cierre")
    
    if valor3 == True:
        valor3 = messagebox.askretrycancel("Algo salio mal!", "Un elemento impide que el documento se cierre")
    else:
        root.destroy()
    
#BUSCAR FICHEROS
def abreFichero():
    fichero = filedialog.askopenfilename(title="Guardar como", initialdir="F:", filetypes=(("Ficheros de Python", "*py"),("Ficheros de texto", "*txt"), ("Todos los ficheros", "*.*"))) #INDICAMOS ELTIPO DE FICHEROS QUE QUIERES QUE ABRA
    
    print(fichero)        


        

#GUARDAMOS EN UNA VARIABLE LA CLASE MENU Y LE INDICAMOS DONDE VA A ESTAR
barraMenu = Menu(root)
#CONFIGURAMOS EL MENÚ
root.config(menu = barraMenu, width=300, height=300)
#INDICAMOS EL NUMERO DE PESTAÑAS DEL MENÚ

archivoMenu = Menu(barraMenu, tearoff=0) #ELIMINAMOS LA BARRA DE ARRIBA
#AGREGAR SUBMENUS
archivoMenu.add_command(label="Nuevo Archivo")
archivoMenu.add_command(label="Nueva Carpeta")
#AGREGAMSO SEPARADOR
archivoMenu.add_separator()
archivoMenu.add_command(label="Guardar")
archivoMenu.add_command(label="Guardar Como", command=abreFichero)
archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar", command=cerrarDoc)
archivoMenu.add_command(label="Salir", command=funSalir)
#-------------------------------
edicionMenu = Menu(barraMenu, tearoff=0)
edicionMenu.add_command(label="Rehacer")
edicionMenu.add_command(label="Deshacer")
edicionMenu.add_separator()
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Pegar")
edicionMenu.add_separator()
edicionMenu.add_command(label="Buscar")
edicionMenu.add_command(label="Reemplazar")
edicionMenu.add_command(label="Buscar en Archivos")
edicionMenu.add_command(label="Reemplazar en Archivo")
#------------------------------
herramientaMenu = Menu(barraMenu)

#-----------------------------------
ayudaMenu = Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia", command=infoLicencia)
ayudaMenu.add_command(label="Acerca de", command=InfoAdd) #INDICAMOS QUE BOTON LE LLAMARA
#-----------------------------------
#CREAMOS LA ETIQUETA DE LOS ELEMENTOS
barraMenu.add_cascade(label="Archivo", menu=archivoMenu)
barraMenu.add_cascade(label="Edición", menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas", menu=herramientaMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)






root.mainloop()