

# DEFINICION DE CLASE

class Coche:
    #CREAMOS UN METODO CONSTRUCTOR PARA INDICAR EL ESTADO INCIAL DE LOS OBJETOS
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #ENCAPSULACION DE PROPIEDAD (VARIABLE)
        self.__enmarcha = False

    # METODOS
    def arrancarCoche(self, arrancamos):
        self.__enmarcha = arrancamos
        if(self.__enmarcha):
            chequeo = self.__Checkeo()
            
        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo == False):
            return "Chequeo no completado"
        else:
            return "El coche esta parado"
        
        

    def estadoVehiculo(self):
        print(f"El coche tiene {self.__ruedas} ruedas. Un ancho de {self.__anchoChasis} metros. Y un largo de: {self.__largoChasis} metros")
        
    
    #ENCAPSULACION DE METODOS (COLOCAMOS __ DELANTE DEL NOMBRE DEL METODO)
    def __Checkeo(self):
        print("Realizando checkeo")
        self.gasolina = "OK"
        self.aceite = "OK"
        self.puertas = "Cerradas"
        if(self.gasolina == "OK" and self.aceite == "OK" and self.puertas == "Cerradas"):
            return True
        else:
            return False



# INSTANCIA DE CLASE

miCoche = Coche()
#ACCESO A SUS PROPIEDADES Y METODOS
print(miCoche.arrancarCoche(True))
miCoche.estadoVehiculo()


print("-------------------------")


miCoche2 = Coche()
print(miCoche2.arrancarCoche(False))
miCoche2.estadoVehiculo()


