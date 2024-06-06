#IMPORTAMOS EL PAQUETE io
from io import open
#CREAMO EL ARCHIVO EXTERNO (nombre_documento = open("nombredelarchivo.extension", "w (escritura)"))
archivo_texto = open("archivo.txt", "w")

#AÑADIMOS TEXTO AL ARCHIVO
frase ="Hola a todos \nMe llamo Óscar"
#AÑADIMOS EL TEXTO AL ARCHIVO
archivo_texto.write(frase)
#CERRAMOS EL ARCHIVO
archivo_texto.close()