"""
Bucle whie
estructura de control que itera una serie de instrucciones tantas veces
como sea necesario hara que deje de cumplirse la condición
"""

contador=1

while contador <=100:
    print(f"Estoy en el número {contador}")
    contador+=1
print("__________________________________________________")


contador=1
muestrame=str(0)

while contador <=100:
    muestrame=muestrame + ", " + str(contador)   
    contador+=1  

print(muestrame) 

#Ejem`plo
print ("Ejemplo con tabla de multiplicar")

num=int(input("¿de que número quiere la tabla: "))

if num<1:
    num=1

print(f"tabla del {num}")

contador = 1
while contador <=10:
    print(f"{num} x {contador} = {num*contador}")
    contador+=1
else:
    print("tabla terminada")


