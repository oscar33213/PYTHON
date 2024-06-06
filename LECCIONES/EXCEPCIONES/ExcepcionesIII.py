import math

def evaluaEdad(edad):
    
    if edad < 0:
        raise TypeError("No se permites edad negativas")
    if edad < 20:
        return "Eres joven"
    elif edad < 40:
        return "Eres Joven"
    elif edad < 65:
        return "Te conservas bien"
    elif edad < 100:
        return "Cuidate"
    
    
print(evaluaEdad(-25))



def calcRaiz(numero):
    if numero < 0:
        raise ValueError("El numero tiene que ser positivo")
    else: 
        return math.sqrt(numero)
    



op1 =(int(input("Introduce numero: ")))
try:
    print(calcRaiz(op1))
except ValueError as ErrorNegativo: #SE LE DA UN NOMBRE PERSONALIZADO AL ERROR
    print(ErrorNegativo)

print("Calculo finalizado")

