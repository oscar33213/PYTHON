
#FUNCION MAP

#APLICA UNA FUNCION A CADA ELEMENTO DE LA LISTA ITERABLE


class Empleado :
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        
    def __str__(self) -> str:
        return "{} que trabaja como {} y tiene un salario de {} €".format(self.nombre, self.cargo, self.salario)
    
    
    
listaEmple = [
    Empleado ("Juan", "Chofer", 1600),
    Empleado ("Pedro", "Jefe de Sección", 2500),
    Empleado ("Marta", "Auxiliar Administrativo", 800),
    Empleado ("Andrea", "Tecnico IT", 1800),
    
]

def calculoComision (empleado):
    
    if empleado.salario < 1500:
        empleado.salario = empleado.salario * 1.03
    
    return empleado


listaEmple = map(calculoComision, listaEmple) #listaIterada = map (funcion, listaIterada)


for empleado in listaEmple :
    print(empleado)

