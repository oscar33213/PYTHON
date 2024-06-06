#DICCIONARIOS

#ESTRUCTURA DE DATOS QUE NOS PERMITE ALMACENAR DIFERENTES VALORES, INCLUSO LISTAS Y DICCIONARIOS

#A LA HORA DE ALMAENARLO LOS HACE MEDIANTE UNA ASOCIACION TIPO CLAVE:VALOR

#EL ORDEN ES INDIFERENTE

#SINTAXIS:

miDiccionario ={"Alemania": "Berlin", "España":"Madrid", "Portugal": "Lisboa", "Andorra": "Andorra La Vella"}
#EL PRIMER ELEMENTO ES LA CLAVE Y EL SEGUNDO EL VALOR ASIGNADO A ESA CLAVE

#ACEDER A UN ELEMENTO

print(miDiccionario["Andorra"])

#ACCEDER A TODO EL DICCIONARIO

print(miDiccionario)

#AGREGAR ELEMENTOS

miDiccionario["Rusia"] = "Moscú"
print(miDiccionario)

#MODIFICAR UN VALOR

miDiccionario["Rusia"] = "Moscow"
print(miDiccionario)

#ELIMINAR ELEMENTOS

del miDiccionario["Rusia"]
print(miDiccionario)



#ASIGNAR CLAVES CON TUPLAS

miTupla =["Juan", "Pedro", "Lucas", "Jorge", "Andrea", "Ana"]
diccionarioAlumnos = {miTupla[0]: 23, miTupla[1]: 22, miTupla[2]:32, miTupla[3]: 20, miTupla[4]: 27, miTupla[5]: 19}
print(diccionarioAlumnos)


#DICCIONARIO ALMACENA A TUPLA

diccionario = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago Bulls", "Anillos":[1991,1992,1993,1996,1997,1998]}
print(diccionario)
#DICCIONARIO DENTRO DE OTRO DICCIONARIO
DiccionarioRM = {"Club":"Real Madrid", "Estadio":"Santiago Bernabeu", "Año": 1902, "UEFA CHAMPIONS LEAGUE": {"Palmares":[1955,1956,1957,1958,1959,1965,1997,1999,2002,2014,2016,2017,2018,2022]}}

print(DiccionarioRM)


#METODO KEYS, VALUE Y LEN

print(DiccionarioRM.keys())
print(DiccionarioRM.values())
print(len(DiccionarioRM))


