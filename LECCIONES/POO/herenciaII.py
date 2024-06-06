#FUNCION SUPER
#FUNCION QUE DONDE SE COLOQUE LLAMARA A LOS METODOS DE LA CLASE PADRE

class Persona:
    def __init__(self, nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia_persona = residencia

    def descripcion(self):
        print(f"Nombre: {self.nombre} \nEdad: {self.edad} \nLugar de residencia: {self.residencia_persona}.")
        
        
class Empleado (Persona):
    
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        #FUNCION SUPER()
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)
        self.salario = salario
        self.antiguedad = antiguedad
        
    def descripcion(self):
        super().descripcion()
        print(f"Salario: {self.salario} € \nAntigüedad: {self.antiguedad} años")
        
        
Antonio = Persona("Antonio", 55, "Cadiz")
Empleado1 = Empleado(21200, 5, "José", 23, "Jaen")

Empleado1.descripcion()


#ISINSTANCE

print(isinstance(Antonio, Empleado))
