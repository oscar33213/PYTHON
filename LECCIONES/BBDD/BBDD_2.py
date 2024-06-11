import sqlite3

# Conectar a la base de datos (o crearla si no existe)
conexion = sqlite3.connect('TIENDA')  # Especifica la extensión del archivo

# Crear un cursor
miCursor = conexion.cursor()



# Crear la tabla PRODUCTOS
miCursor.execute("""
    CREATE TABLE IF NOT EXISTS PRODUCTOS (
        CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
        NOMBRE_ARTICULO VARCHAR(100),
        PRECIO_ARTICULO INTEGER,
        SECCION_ARTICULO VARCHAR(20)
    )
""")

# Crear la tabla PERSONAL con la estructura correcta
miCursor.execute("""
    CREATE TABLE IF NOT EXISTS PERSONAL (
        ID_TRABAJADOR INTEGER PRIMARY KEY AUTOINCREMENT,
        NOMBRE_TRABAJADOR VARCHAR(100),
        APELLIDO1_TRABAJADOR VARCHAR(100),
        APELLIDO2_TRABAJADOR VARCHAR(100)
    )
""")


#CRUD

miCursor.execute("SELECT * FROM PERSONAL WHERE APELLIDO1_TRABAJADOR = 'Ruiz'")



personal = miCursor.fetchall()


# miCursor.execute("UPDATE PERSONAL SET NOMBRE_TRABAJADOR = 'ANDRES' WHERE NOMBRE_TRABAJADOR = 'Juan'")

miCursor.execute("DELETE FROM PRODUCTOS WHERE CODIGO_ARTICULO = 'AR05'")

print(personal)
# Guardar los cambios y cerrar la conexión
conexion.commit()
conexion.close()
