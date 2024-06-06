
print("Programa becas 2024")
distancia_escuela = int(input("Indica tu distancia en KM: "))
numero_hermanos = int(input("Indica el numero de hermanos cursando en el centro: "))
salario_padre = int(input("Indica el salario (año) del padre; "))
salario_madre = int(input("indica el salario (año) de la madre: "))
salario_familia = int(input("Si lo hubiese, indica salario (año) de otro familiar que conviva en su domicilio (SI NO, MARQUE CON 0): "))

salario = salario_padre + salario_madre + salario_familia
print(salario)

if distancia_escuela > 40 and numero_hermanos >= 2 or salario <= 20000:
    print("Opta a beca")

else: 
    print("No opta a beca")
    
    