"""
Ejercicio 1
Lista con 8 números enteros
recorrerla lista y mostrarla
hacer una función que devuelta una lista de número y devuelva un string
ordenarla y mostrarla
mostrar su longitud
buscar un elemento pedido por teclado
"""
#Crear la lista

numeros=[13, 64, 52 , 73, 21, 7, 91, 63]

#recorrer con función (creo la función)

def mostrarLista(lista):
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: "+ str(elemento)
        resultado += "\n"
    return resultado    


#recorrer y mostrar
"""
print("Recorrer y mostrar")
for numero in numeros:
    print(numero)

"""
#llamamos a la funcion
print(mostrarLista(numeros))

#Ordenar y mostrar
print("***Ordenar y mostrar***")

numeros.sort()
print(mostrarLista(numeros))

#mostrar longitud
print("***longitud***")

print(len(numeros))

#buscar en la lista
try:
    print("***buscar en la lista***")


    num2=int(input("digita un número: "))

    comprobar =isinstance(num2, int)

    while not comprobar or num2 <=0:
        num2 = int(input("Introduce el número: "))
    else:
        print(f"Has introducido el {num2}")
   
        busqueda=numeros.index(num2)
        print(f"El numero buscado existe y está en la posición {busqueda}")
except:
    print("El número no está en la lista")






