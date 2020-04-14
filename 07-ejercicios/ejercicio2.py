"""
Ejercicio 2
-mostrar por pantalla todos los números pares del 1 al 120
"""
contador = 1


while contador <=120:
    if contador%2==0:
        print(f"es par {contador}")
    else:
        print(f"es impar{contador}")   
    contador+=1


for contador in range (1,121):
    if contador%2==0:
        print(contador)   
