
import math
print("Programa de calculo de raiz cuadrada: ")


numero = int(input("Introduzca un numero positivo: "))

vidas = 5

while  numero < 0:
    print("No existe la raiz de un numero negativo")
    
    
    if vidas < 0:
        print(f"Te quedan {vidas} vidas. HAS PERDIDO")
        break
    numero = int(input("Introduzca un numero positivo: "))
    if numero<0:
        vidas = vidas - 1
        
    



if vidas >= 0:
    solucion = math.sqrt(numero)   
    print(f"La raiz cuadrada de {numero} es: {solucion}")



        