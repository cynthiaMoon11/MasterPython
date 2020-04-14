"""
Hallar el porcentaje x de un número introducido
"""
num =int(input("Introduce el valor al que le quieres aplicar el porcentaje: "))
por=int(input("introduce el porcentaje que quieres aplicar a la cifra: "))

resultado=num*por/100

print(f"El {por} por ciento de {num} es {resultado}")