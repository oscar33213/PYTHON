#FUNCION DECORADORA

def funcion_decoradora(funcion_parametro):
    
    def funcion_interna():
        
        #ACCIONES ADICIONALES QUE DECORAN
        
        print("Vamos a realizar un calculo: ")
        
        funcion_parametro()
        
        #ACCIONES ADICIONALES
        
        print("Fin del calculo")
        
    return funcion_interna
        
        






#DECORAMOS LA FUNCIÓN
@funcion_decoradora
def suma():
    print (15 + 20)
    
@funcion_decoradora
def resta ():
    
    print (20 - 23)
    
    
    
suma()
resta()