import math

#FUNCION LAMBDA:
areaTriangulo = lambda base,altura : (base * altura)/2


al_cubo = lambda numero : numero ** 3


Area_Circulo = lambda radio: math.pi * (math.pow(radio, 2))


valor1 = float(input("Indica el primer valor: "))
valor2 = float(input("Indica el segundo valor: "))

Area_Rectangulo = lambda valor1, valor2: valor1 * valor2

# Calcula el área del rectángulo
area = Area_Rectangulo(valor1, valor2)

# Imprime el mensaje con el área calculada
print(f"El área del rectángulo de {2 * valor1 + 2 * valor2} es: {area}")



destacar_valor = lambda comision : "¡{}! €".format(comision)


comision_Ana = 1000

print(destacar_valor(comision_Ana))