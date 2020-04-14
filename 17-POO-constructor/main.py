#tengo que importar el archivo (módulo)
from coche import Coche

carro=Coche("rojo", "Renauld" ,"Clio", 150, 200, 4)
carro2=Coche("verde", "Seat" ,"Panda", 240, 200, 4)
carro3=Coche("azul", "Citroen" ,"Xara", 100, 180, 2)
carro4=Coche("rojo", "Mercedes" ,"Clase a", 350, 400, 2)

print(carro.getModelo())

print(carro.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())

#detectar tipado

if type(carro3) == Coche:
    print("Si es un obj de tipo coche")

else:
    print("No es un obj de tipo coche")

#Visibilidad 
print(carro.soyPublico)
print(carro.getPrivado())






