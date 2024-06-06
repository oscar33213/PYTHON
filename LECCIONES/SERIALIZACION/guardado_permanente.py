import pickle

class Persona:
    def __init__(self, nombre, genero, edad):
        self.nombrePersona = nombre
        self.generoPersona = genero
        self.edadPersona = edad
        print(f"Se ha creado una persona nueva llamada {self.nombrePersona}")

    def __str__(self):
        return "{} {} {}".format(self.nombrePersona, self.generoPersona, self.edadPersona)

class ListPersonas:
    def __init__(self):
        self.personas = []
        try:
            with open("fichero_personas", "rb") as listaDePersonas:
                self.personas = pickle.load(listaDePersonas)
                print("Completada la carga, se han cargado {} personas".format(len(self.personas)))
        except (FileNotFoundError, EOFError):
            print("El fichero está vacío o no existe")
            
    def agregarPersona(self, p):
        self.personas.append(p)
        self.guardarPersonasFichero()

    def mostrarPersonas(self):
        for p in self.personas:
            print(p)
            
    def guardarPersonasFichero(self):
        with open("fichero_personas", "wb") as listaDePersonas:
            pickle.dump(self.personas, listaDePersonas)
        
    def mostrarInfFichero(self):
        print("La información del fichero es: ")
        for p in self.personas:
            print(p)

# Crear una instancia de ListPersonas y agregar personas
miLista = ListPersonas()
p = Persona("Oscar", "Masculino", 27)
miLista.agregarPersona(p)
p = Persona("Ana", "Femenino", 17)
miLista.agregarPersona(p)
p = Persona("Kylian", "Masculino", 37)
miLista.agregarPersona(p)

# Mostrar la información del fichero
miLista.mostrarInfFichero()




