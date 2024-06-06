print("Asignaturas Optativas 2024")

print("inforamtica grafica - Pruebas de SW - Usabilidad y Accesibilidad")

opcion = input("Escribe la asignatura escogida: ")

#TRANFORMA EL STRING A MINUSCULA

asignatura = opcion.lower()

if asignatura in ("informatica grafica", "pruebas de SW", "usabilidad y accesibilidad"):
    print("Asignatura elegida: " + asignatura)
else:
    print("No se ha encontrado la asignatura")
    
    
    
    

