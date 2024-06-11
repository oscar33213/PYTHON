import re

nombre1 = "Oscar Hidalgo"

nombre2 = "Marcos Hidalgo"

nombre3 = "Jose Diaz"

nombre4 = "Luis Perez"

nombre5 ="Jara Lopez"

nombre6 ="Cara Lopez"

nombre7 ="Hola a todos, mi nombre es Pepe y tengo 28 años, me gustan las amapolas, mi madreme dijo que soy bueno"




#Match BUSCA AL PRINCIPIO DE LA CADENA EL PATRON DE BUSQUEDA
if re.match("Sandra", nombre2):
    print("Si")
else:
    print("No")
    


if re.match("Oscar", nombre1, re.IGNORECASE): #IGNORA LAS AMYUSCULAS
    print("Si")
else:
    print("No")
    

if re.match(".ara", nombre5, re.IGNORECASE): #BUSCA LOS NOMBRES SEGUIDOS DE ara
    print("Si")
else:
    print("No")
    

if re.match("\d", nombre2): #BUSCA LOS NOMBRES SEGUIDOS DE ara
    print("Si")
else:
    print("No")


#SEARCH

if re.search("Pepe", nombre7):
    
        print("Si")
else:
    print("No")
