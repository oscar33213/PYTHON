#YIELD FROM


#SIMPLIFICA EL CODIGO DEL GENERADOR EN CASO DE BUCLES ANIDADOS


def Ciudades(*ciudades): #EL ASTERISCO INDICA QUE VA A RECIBIR UN NUMERO INDETERMINADO DE ELEMENTOS EN UNA LISTA
    for elemento in ciudades:
        yield from elemento
        #EN ESTE CASO DEVOLVERIA SOLO LOS 3 PRIMEROS SUBELEMENTOS




ciudades_devueltas = Ciudades("Madrid", "Murcia", "Vitoria", "Alava")


print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))

