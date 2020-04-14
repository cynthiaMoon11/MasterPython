"""
Como conectarnos a la base de datos:
1. importar el módulo

"""

import sqlite3

#conexion

conexion=sqlite3.connect('pruebas.db')
#crear cursor
cursor=conexion.cursor()
#crear tabla
cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY  KEY AUTOINCREMENT,
    titulo varchar(255),
    descripcion text,
    precio int(255)
    );
    """)

conexion.commit()
"""
#insertar datos
cursor.execute("INSERT INTO productos VALUES (null, 'Primer producto', 'Descripción', 550)")
conexion.commit()
"""
#borrar registros
cursor.execute("DELETE FROM productos")

#insertar
productos=[
    ("ordenador", "buen pc", 700),
    ("movil", "buen celuco", 140),
    ("placa base", "buena placa", 80),
    ("tablet 15", "buena tablet", 300),
]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)",productos)
conexion.commit()

#update
cursor.execute("UPDATE productos SET precio=678 WHERE precio=80")


#leer datos listandolos
cursor.execute("SELECT * FROM productos WHERE precio >=300;")
productos =cursor.fetchall()

#print(productos)
for producto in productos:
    print("id:", producto[0])
    print("Titulo:", producto[1])
    print("precio",producto[3])

cursor.execute("SELECT titulo FROM productos;")
producto=cursor.fetchone()
print(producto)

#cerrar conexion
conexion.close()


