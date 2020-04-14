"""
los numeros impares entre dos numeros que escriba el usuario
"""
num1=int(input("introduce número 1: "))
num2=int(input("introduce número 2: "))

if num1<num2:
    for cont in range(num1, (num2+1)):
        if cont%2!=0:
            print(f"es un numero impar {cont}")
        else:
            print(f"es un numero par {cont}")
else:
    print("El número 1 debe ser menor a el número 2")
