class Empleado :
    def __init__(self, nombre, cargo, salario):
        self.nombreTrabajador = nombre
        self.cargoTrabajador = cargo
        self.salarioTrabajador = salario
        
    def __str__(self) -> str:
        return "{} que trabaja como {} y tiene un salario de {} €".format(self.nombreTrabajador, self.cargoTrabajador, self.salarioTrabajador)
    
    
    
listaEmpleados = [
    Empleado ("Juan", "Chofer", 24000),
    Empleado ("Pedro", "Jefe de Sección", 35000),
    Empleado ("Marta", "Auxiliar Administrativo", 18000),
    Empleado ("Andrea", "Tecnico IT", 21000),
    
]


salariosAltos = filter(lambda empleado : empleado.salarioTrabajador > 30000, listaEmpleados)

for empleadoSalario in listaEmpleados :
    print(empleadoSalario)