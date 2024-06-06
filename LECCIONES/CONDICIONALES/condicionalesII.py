
salario_presidente = int(input("indica el salario del presidente: "))
print("El salario del presidente es: "+ str(salario_presidente))

salario_director = int(input("Indica el salario del director: "))
print("El salario del directores: " + str(salario_director))

salario_jefeArea = int(input("Indica el salario del jefe de area: "))
print("El salario del directores: " + str(salario_jefeArea))

salario_admin = int(input("Indica el salario del Administrativo: "))
print("El salario del directores: " + str(salario_admin))



if salario_admin < salario_jefeArea < salario_director < salario_presidente:
    print("Es correcto")
    
else:
    print("No es correcto")
    
    