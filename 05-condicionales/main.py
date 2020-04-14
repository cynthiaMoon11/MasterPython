#Condicional es una estructura de control
# Condicional IF
# Operadores de comparación
"""
==
!=
<
>
<=
>=
operadores lógicos
and Y
or   o
!   diferente
not No
"""
#Ejemplo 1
print("/*///// Ejemplo 1 ///***///")

color = "verde"
#color = input ("adivina cual es mi color favorito")
if color =="rojo":
    print("El color correcto, es rojo")
else:
    print("El color es incorrecto")

#Ejemplo 2
print("\n/*///// Ejemplo 2 ///***///")
year = 2020
#year = int( input("En que año estamos: "))
if year >=2021:
       print("Estamos de 2021 en adelante")
else:
   print ("Es un año anterior a 2021")

#Ejemplo 3
print("\n/*///// Ejemplo 3 ///***///")

nombre ="Cynthia Escobar"
ciudad = "Bilbo"
edad= 55 
continente ="Europa"
mayoria_edad = 18

if edad >= mayoria_edad:
     print(f"{nombre} es mayor de edad")

     if continente !="Europa":
         print(f"{nombre}, no es europeo")
     else:
        print(f"{nombre} es europeo, vive en {ciudad}") 
else:
    print(f"{nombre} no es mayor de edad")

    #Ejemplo 4
print("\n/*///// Ejemplo 4 ///***///")

dia = 1
#dia =int(input("Introduce el número de la semana: "))
if dia ==1:
    print("El día es Lunes")
elif dia==2:
    print("El día es Martes")
elif dia==3:
    print("El día es Miércoles")
elif dia==4:
    print("El día es Jueves")
elif dia==5:
    print("El día es Viernes")
else:
    print("Es fin de semana")
 
    #Ejemplo 5
print("\n/*///// Ejemplo 5 ///***///")

edad_min= 18
edad_max=65
edad_real=17

#edad_real=int(input("Cual es tu edad?"))
if edad_real >=edad_min and edad_real<=edad_max:
    print("Está en edad de trabajar")
else:
    print("no está en edad de trabajar")

     #Ejemplo 6
print("\n/*///// Ejemplo 6 ///***///")
pais="Alemania"

if pais=="Colombia" or pais=="España" or pais=="Mexico":
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} no es un pais de habla hispana:")


 #Ejemplo 7
print("\n/*///// Ejemplo 7 ///***///")
pais="España"

if not(pais=="Colombia" or pais=="España" or pais=="Mexico"):
    print(f"{pais} No es un pais de habla hispana")
else:
    print(f"{pais} Si es un pais de habla hispana:")

    #Ejemplo 8
print("\n/*///// Ejemplo 8 ///***///")
pais="Colombia"

if pais!="Colombia" and pais!="España" and pais!="Mexico":
    print(f"{pais} No es un pais de habla hispana")
else:
    print(f"{pais} Si es un pais de habla hispana:")

