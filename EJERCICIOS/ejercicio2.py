

#EJERCICIO 1:

#Crea un programa que muestre los números impares del 1 al 100. Los números deberán
#aparecer una al lado del otro sin salto de línea


for i in range (1, 101, 2):
    print(i, end=" ")
    


# EJERCICIO 2:

#Crea un programa que pida por teclado introducir una contraseña. La contraseña no
#podrá tener menos de 8 caracteres ni espacios en blanco. Si la contraseña es correcta,
#el programa imprime “Contraseña OK”. En caso contrario imprime “Contraseña
#errónea”


contador = 0


intrPass = (input("Indica la contraseña: (RECUERDA MAXIMO 8 CARACTERES, SIN ESPACIOS)"))


for i in range(len(intrPass)):
    if intrPass[i] == " ":
        contador = 1
        
if len(intrPass)< 8 or contador > 0:
    print("Contraseña erronea")
else:
    print("Contraseña correcta")
    
    
    

#EJERCICIO 3

#Crea un programa que evalúe si una dirección de correo electrónico es válida o no en
#función de si tiene “@” o “.” Hay que tener en cuenta que la dirección se considera
#correcta si solo tiene una “@” y si tiene uno o más “.”


arroba = 0
punto = 0
mail = False

indicaMail = input("Introduce tu email: ")

for i in indicaMail:
    if i == '@':
        arroba += 1
    elif i == '.':
        punto += 1

if arroba == 1 and punto >= 1:
    mail = True

if mail:
    print("Acceso permitido")
else:
    print("ERROR!")