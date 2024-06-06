
#GENERADORES: 

# EXTRAEN VALORES DE UNA FUNCION Y SE ALMACENAN EN OBJETOS QUE SE PUEDEN RECORRER

#SE ALMACENAN DE UNO EN UNO

#CADA VEZ QUE UN GENERADOR ALMACENA UN VALOR ESTE PERMANECE EN ESTADO PAUSADO HASTA QUE SE SOLICITA EL SIGUIENTE



#SINTAXIS CON FUNCION

def generarNumPares(limite):
    
    numero = 1
    
    lista = []
    
    while numero < limite:
        lista.append(numero*2)
        numero = numero + 1
        
        
    return lista




print(generarNumPares(10))






def generarNumPares(limite):
    
    numero = 1
    
    
    while numero < limite:
        yield numero * 2
        numero = numero + 1
        
        
    


devuelvePares = generarNumPares(10)



print(next(devuelvePares)) 
#DEVUELVE EL PRIMER VALOR ALMACENADO

print("HOPLA")

print(next(devuelvePares)) 


print("HOPLA")

print(next(devuelvePares)) 


print("HOPLA")

print(next(devuelvePares)) 


print("HOPLA")

print(next(devuelvePares)) 


print("HOPLA")



