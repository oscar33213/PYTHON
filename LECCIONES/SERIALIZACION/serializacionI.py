import pickle
#CREAMOS LA LISTA
lista_nombres = ["Pedro", "Jose", "Andrea"]
#CREAMOS EL ARCHIVO DONDE INTRODUCIERMOS LA LISTA
fichero_binario = open("lista_nombres", "wb")
#VOLCAMOS LA LISTA AL FICHERO
pickle.dump(lista_nombres, fichero_binario)
#CERRAMOS EL FICHERO
fichero_binario.close()

del (fichero_binario)



