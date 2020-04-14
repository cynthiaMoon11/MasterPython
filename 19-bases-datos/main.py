import mysql.connector

#conexion

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

#como saber si hay conexon

#print(database)

cursor=database.cursor(buffered=True) #para poder hacer varias consultas a la base de datos

cursor.execute("CREATE DATABASE IF NOT EXISTS Master_python")
cursor.execute("SHOW databases")

for bd in cursor:
    print(bd)

#crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS  vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
    
)
""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

"""
cursor.execute("INSERT INTO vehiculos VALUES(null,'Opel','Astra',18000)")


"""

"""
coches=[
    ('Seat','Ibiza',5000),
    ('Renault','Clio',15000),
    ('Citroen','Saxo',2000),
    ('Mercedes','Clase C',35000)
]

cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
database.commit()
"""
#sacer la info de la bbdd

cursor.execute("SELECT * FROM vehiculos WHERE precio <=5000 and marca='Seat'")
result=cursor.fetchall()

print("--Coches en la tabla----")
for dato in result:
    print(dato[1],dato[3])


cursor.execute("SELECT * FROM vehiculos")
coche1=cursor.fetchone() #devuelve el primer dato en la tabla

print(coche1)

#borrar datos

cursor.execute("DELETE FROM vehiculos WHERE marca='Mercedes'")
database.commit()

print(cursor.rowcount, "borrados")

#actualizar columnas

cursor.execute("UPDATE vehiculos SET modelo='León' WHERE marca='Seat'")
database.commit()

print(cursor.rowcount, "actualizados")