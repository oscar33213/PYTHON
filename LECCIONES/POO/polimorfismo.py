#POLIMORFISMO

class Coche():
    def desplazamiento(self):
        print("Me desplazo usando 4 ruedas")
    
    
    
    
class Moto():
    def desplazamiento(self):
        print("Me desplazo usando 2 ruedas")
        


class Camion():
    
    def desplazamiento(self):
        print("Me desplazo usando 6 ruedas")
        

#CONSTRUCCION DE POLIMORFIMSO
#CREAMOS UN METODO AL CUAL LE PASAREMOS UN IBJETO COMO ATRIBUTO
def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()
    
    

miVehiculo = Camion()
desplazamiento_vehiculo(miVehiculo)

#CONSEGUIMOS QUE EL OBJETO VEHICULO SE TRANSOFRME EN UN OBJETO DE TIPO CAMIÓN

#EJEMPLO: def desplazamiento_vehiculo(vehiculo): => def desplazamiento_vehiculo(camion):

miVehiculo2 = Coche()
desplazamiento_vehiculo(miVehiculo2)