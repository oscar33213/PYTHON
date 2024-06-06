#LISTAS O ARRAYS

#PYTHON PERMITE GUARDAR VARIOS TIPOS DE VALORES EN UNA MISMA LISTA

#SE PUEDEN EXPANDIR DINAMICAMENTE

Coches = ["Volvo", "Audi", "Toyota", "Renault", "Ferrari", "Lamborghini", "Opel", "Subaru", "Lexus", "Citroen", "Masseratti"]


print(Coches[:])

print(Coches[3])


#PORCION DE LISTA
#ACCEDE A LA LISTA ENTRE EL NUMERO INICIAL Y EL NUMERO FINAL -1

print(Coches[3:8])


print(Coches[5:]) #INDICAMOS QUE EMPIECE A CONTAR DESDE LA POSICIÓN NUMERO 5 HASTA EL FINAL

#AGREGAR ELEMENTOS

Coches.append("MINI")

print(Coches[:])


#AGREGAR ELEMENTOS EN LA POSICION INDICADA

Coches.insert(8, "Honda")
print(Coches[:])


#AGREGAR VARIOS ELEMENTOS 

Coches.extend(["Alfa Romeo", "Alpine", "Aston Martin", "BMW"])
print(Coches[:])

#DEVOLVER LA POSICION DE UN ELEMENTO EN LA LISTA

print(Coches.index("MINI"))


Coches.append((5*4))

print(Coches[:])

Coches.append(5*5)

print(Coches[:])


#ELIMINACION DE ELEMENTOS

Coches.remove("BMW")

print(Coches[:])


#SUMAR LISTAS

Clientes = ["Juan", "Pedro", "Lucas", "Pepe"]

ListaClientesCoches = Clientes + Coches

print(ListaClientesCoches[:])


#MULTIPLICACION DE LISTAS

Materiales = ["Lapiz", "Goma", "Borrador"]* 4 #REPITE 4 VECES LA MISMA LISTA

print(Materiales[:])

