import re

cadena = "Hola a todos, mi nombre es Pepe y tengo 28 años, me gustan las amapolas, mi madreme dijo que soy bueno"

# Pedir al usuario que introduzca la palabra a buscar
textBuscar = input("Indica la palabra a buscar: ")

# Buscar el texto en la cadena
textoEncontrado = re.search(textBuscar, cadena)

# Verificar si el texto fue encontrado
if textoEncontrado:
    print(textoEncontrado.start())  # Imprime el número del carácter donde empieza el texto encontrado
else:
    print("No se ha encontrado el texto")
    
    

print(len(re.findall(textBuscar, cadena)))












    
