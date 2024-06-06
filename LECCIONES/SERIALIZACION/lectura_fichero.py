import pickle
#CREAMOS UN NUEVO FICHERO EN MEMORIA YU LO ABRIMOS, INDICAMOS EL NOMBRE DEL ARCHIVO(ESTE DEBE SER EL BINARIO) Y rb (read binary)
fichero = open("lista_nombres", "rb")
#CARGAMOS LA LISTA => nombrevariableLista = pickle.load(variable donde se va a descargar)
lista =pickle.load(fichero)

print(lista)