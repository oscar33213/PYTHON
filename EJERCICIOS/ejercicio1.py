


#EJERCICIO 01

num1 = (int(input("Indica primer numero ")))
num2 = (int(input("Indica segundo numero ")))



def numMax(n1, n2):
	if n1 < n2:
		print(n2)
	elif n1 > n2:
		print(n1)
	else:
		print("Son iguales")



print("El numero mas alto es: ")
numMax(num1, num2)




#EJERCCIO 2

nombre = input("Indica tu nombre: ")
direccion = input("Indica tu direccion: ")
numero = input("Indica tu numero de telefono: ")


listaDatos = [nombre, direccion, numero]

print("Los datos personales son: " + listaDatos[0] + " " + listaDatos[1] + " " + listaDatos[2])


#EJERCICIO 3

numero1 = (int(input("Indica primer numero: ")))
numero2 = (int(input("Indica segundo numero: ")))
numero3 = (int(input("Indica tercer numero: ")))


def mediaAr(n1, n2, n3):

	media = (n1 + n2 + n3)/3

	return media 


print(mediaAr(numero1, numero2, numero3))




#EJERCICIO 04

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