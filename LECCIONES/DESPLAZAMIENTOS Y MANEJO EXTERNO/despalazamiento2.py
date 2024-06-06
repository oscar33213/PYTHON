from io import open

# Abrir el archivo en modo lectura
archivo_texto = open("archivo.txt", "r+") #indicamos que es de lectura y escritura
#MODIFICACION DE UNA LINEA DE TEXTO
lista_texto= archivo_texto.readlines();

lista_texto[1] = "Esta linea a sido incluida desde fuera \n"

archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close