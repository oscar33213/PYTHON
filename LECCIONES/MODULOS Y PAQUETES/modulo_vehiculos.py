class Vehiculos:
    
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.enmarcha = False
        self.acelerar = False
        self.frenar = False
        
    def arrancar(self):
        self.enmarcha = True
        
    def acelerar(self):
        self.acelerar = True
    
    def frenar(self):
        self.frenar = True
    
    def estadoVehiculo(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo}\nColor: {self.color} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelerar} \nFrenado: {self.frenar}")

# HERENCIA

class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito = "Haciendo caballito"
        #SOBREESCRITURA DE METODOS:
        #AÑADIR UN METODO CON EL MISMO NOMBRE Y AGREGAR
    def estadoVehiculo(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo}\nColor: {self.color} \nEn Marcha: {self.enmarcha} \nAcelerando: {self.acelerar} \nFrenado: {self.frenar} \n{self.hcaballito}")
        

# Llamada al método estadoVehiculo

print("-----------------------------------")
class Furgoneta(Vehiculos):
    def cargaFurgoneta (self, carga):
        self.cargado = carga
        if(self.cargado):
            return "Esta caragada"
        else:
            return "Esta vacia"
        
        


class VElectricos (Vehiculos):
    
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo, color)
        self.autonomia = 100
    def cargaEnergia(self):
        self.cargando = True
        
        
#MULTIHERENCIA O HERENCIA MULTIPLE
#EN CASO DE HERENCIA MULTIPLE SE DA PRIORIDAD A LA PRIMERA CLASE DE LA QUE HEREDA, EN ESTE CASO ESTA RECOGIENDO LOS CONSTRUCTORES DE VELECTRICO
class BiciElectrica(VElectricos, Vehiculos):
    pass




