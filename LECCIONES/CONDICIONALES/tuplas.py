#TUPLAS

#LAS TUPLAS NO PERMITEN SU EDICION, SON INMUTABLES
										
#PERMITEN EXTRAER PORCIONES, PERO ESTAS LO HACEN DE MANERA DE UNA NUEVA TUPLA

#PERMITEN FORMAYEAR STRINGS

#SINTAXIS DE TUPLA

ListaTupla = ("Juan", "Pedro", "Pepe", "Jorge")

#ACCEDER A UN ELEMENTO EN CONCRETO

print(ListaTupla[2])

#DE TUPLA A LISTA <>

MiLista = list(ListaTupla) #ALMACENAMOS EN FORMA DE LISTA LA TUPLA

print(MiLista)

#DE LIST A TUPLA

miArray = [1, 5,12, 21]

MiTupla = tuple(miArray)

print(MiTupla)


#LOCALIZAR UN ELEMENTO EN UNA TUPLA

print("Pepe" in ListaTupla)

#METODO COUNT
#INDICAMOS QUE NOS IMPRIMA LA CANTIDAD DE REPETICIONES DE UN ELEMENTO
print(ListaTupla.count("Juan"))

#LEN, MIDE LA LONGITUD DE UNA TUPLA

print(len(ListaTupla))


#TUPLA UNITARIA

TuplaUnitaria = ("Marcos",)

print(len(TuplaUnitaria))

#DESEMPAQUETADO DE TUPLA
TuplaFecha = ("Oscar", 03, 03, 1997)
#ASIGNAMOS CADA VALOR EN LA VARIABLE SIGUIENDO EL MISMO ORDEN
nombre, dia, mes, anyo = TuplaFecha


print(nombre)