import pickle


class Vehiculos():
    
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
        
        
        

coche1 = Vehiculos("Renault", "Megane", "Rojo")
coche2 = Vehiculos("Seat", "Altea", "Verde")
coche3 = Vehiculos("Opel", "Zafira", "Negro")


coches = [coche1, coche2, coche3]

fichero = open("fichero_vehiculos", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

ficheroApertura = open("fichero_vehiculos", "rb")

misCoches = pickle.load(ficheroApertura)

ficheroApertura.close()

for c in misCoches:
    print(c.estadoVehiculo())
    