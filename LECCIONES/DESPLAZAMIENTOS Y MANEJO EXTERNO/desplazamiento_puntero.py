from io import open

# Abrir el archivo en modo lectura
archivo_texto = open("archivo.txt", "r")

# Leer el contenido del archivo
lineas_texto = archivo_texto.read()

# Cerrar el archivo
archivo_texto.close()

# Imprimir el contenido del archivo
print(lineas_texto)

# Reabrir el archivo para mover el puntero y leer desde una posición específica
archivo_texto = open("archivo.txt", "r")

# Mover el puntero a la posición 21
archivo_texto.seek(len(archivo_texto.read())/2)

# Leer el contenido del archivo desde la posición indicada
lineas_texto = archivo_texto.read(24)

# Cerrar el archivo
archivo_texto.close()

# Imprimir el contenido del archivo desde la posición 21
print(lineas_texto)


