#For
"""
for variable in el elemento_iterable (lista, rango, etc)
   BLOQUE DE INSTRUCCIONES

"""

contador = 0
resultado=0
for contador in range (0,5):
     print("voy por el " + str(contador))
     resultado+=contador

print(f"El resultado es: {resultado}")

#Ejemplo tablas de multiplicar
print("\n*************ejemplo*************")

numero=int(input("¿de que número quiere la tabla?: "))

if numero<1:
    numero=1

print(f"\n*****Tabla de multi del {numero}******")

for numTabla in range(1,11):

    if numero==45:
        print("No se pueden mostrar números prohibidos")
        break
    print(f"{numero} x {numTabla} = {numero*numTabla}")
else:
    print("Tabla finaliza.")



