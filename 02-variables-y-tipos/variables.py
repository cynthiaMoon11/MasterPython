"""
una variable es un contenedor de información
dentro 
"""
texto="Máster en Python"
texto2 = "con Victor Robles"
num=45
decimal =6.7

#mostrar las variables
print(texto)
print(texto2)
print(num)
print(decimal)

print("__________________________________")
#reasignamos el valor de las variables
num=88
decimal =8.7
print(num)
print(decimal)

print("__________________________________")

#Concatenación
nombre="Cynthia"
apellidos="Escobar"
web="Cynthia.es"

print(nombre + " "+ apellidos + " mi web es " + web)
print (f"{nombre} {apellidos} mi web es {web}") 
print("Hola me llamo {} {} y mi web es: {}".format(nombre,apellidos,web))

print(nombre, apellidos, web)#similar a concatenar


