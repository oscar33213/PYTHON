

# EJERCICIO 1

# Crea un programa que pida números infinitamente. Los números introducidos deben
# ser cada vez mayores. El programa finalizará cuando se introduzca un número menor que
# el anterior.

numero_anterior = int(input("Indica un número: "))

while True:
    numero_nuevo = int(input("Indica un número, este tiene que ser mayor al anterior: "))
    if numero_nuevo <= numero_anterior:
        print("El número introducido es menor o igual que el anterior. Programa terminado.")
        break
    numero_anterior = numero_nuevo


# EJERCICIO 2

#Crea un programa que pida números positivos indefinidamente. El programa termina
#cuando se introduce un número negativo. Finalmente el programa muestras la suma de
#todos los números introducidos

numeros = (int(input("INDICA EL NUMERO, ESTE TIENE QUE SER POSITIVO: ")))
suma = 0
while numeros >= 0:
    suma = suma + numeros
    numeros = (int(input("INDICA EL NUMERO, ESTE TIENE QUE SER POSITIVO: ")))

print("La suma de los nuemros es: ", str(suma) )



