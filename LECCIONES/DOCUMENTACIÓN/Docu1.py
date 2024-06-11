class Areas:
    
    """esta clase calcula diferentes areas"""

    def area_cuadrado(lado): 
        
        """CALCULA EL AREA DE UN CUADRADO"""
        
        return "El area del cuadrado es:" + str(lado*lado)


    def area_triangulo(base, altura): 
        
        """CALCULA EL AREA DE UN TRIANGULO QUE RECIBE DOS PARAMETROS"""
        
        return "El area del triangulo es:" + str(base * altura)/2

#print(area_cuadrado(23))
#print(area_cuadrado.__doc__) #IMPRIME LA DOCUMENTACION ASOCIADA A LA FUNCION



help(Areas.area_triangulo) #IMPRIME LA DOCUMENTACION ASOCIADA A LA FUNCION SIN LA NECESIDAD DE PRINT
help(Areas) #IMPRIME LAS AYUUDAS DE TODA LA CLASE




