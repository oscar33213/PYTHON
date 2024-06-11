


def funcion_decoradora(funcion_parametro):
    
    def funcion_interna(*args, **kwargs): 
        
        
        
        print("Vamos a realizar un calculo: ")
        
        funcion_parametro(*args, **kwargs)
        
        
        
        print("Fin del calculo")
        
    return funcion_interna
        
        

# args para indicar que la funcion va a recibir parametros
# kwargs VA A RECIBIR UN PARAMETRO CLAVE:VALOR



#DECORADORES CON PARAMETROS

@funcion_decoradora
def suma(num1, num2):
    print (num1 + num2)
    
@funcion_decoradora
def resta (num1, num2):
    
    print (num1 - num2)
    
@funcion_decoradora
def potencia(base, expo):
       
       print(pow(base, expo))
    
suma(7,5)
resta(20, 23)
potencia(base=20,expo=4)

