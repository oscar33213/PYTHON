#IMPORTAMOS LA LIBRERIA SQL
import sqlite3
#CREAMOS LA CONEXION
miConexion = sqlite3.connect("Primera Base")
#CREAMOS EL PUNTERO
miCursor = miConexion.cursor()
#CREAR TABLA
miCursor.execute("""
    CREATE TABLE IF NOT EXISTS PRODUCTOS (
        NOMBRE_ARTICULO VARCHAR(100),
        PRECIO_ARTICULO INTEGER,
        SECCION_ARTICULO VARCHAR(20)
    )
""")
#INSERTAR REGISTRO
#miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN', 15, 'DEPORTES')")
#INSERTAR VARIOS REGISTROS A LA VEZ
#variosProductos = [
#    
#   ("Camiseta", 10, "Deportes"),
#    ("Coche de Juguete", 14, "Jugetes"),
#    ("Pelota de Playa", 25, "Playa"),
#    ("Polo", 30, "Deportes")         
#]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)", variosProductos) #CADA INTERRPGANTE ES UN CAMPO
#VALIDAR EL REGISTRO

miCursor.execute("SELECT * FROM PRODUCTOS")
ListaProductos = miCursor.fetchall()
#print(ListaProductos)

for producto in ListaProductos:
    print(f"Nombre producto {producto[0]} \nSeccion {producto[2]}")
miConexion.commit()

miConexion.close()