"""

"""

cantantes = ["Slayer", "Metallica", "Mon Laferte"]
numeros = [1, 2, 3, 4, 5, 8, 3]

#ordenar una lista

print(numeros)
numeros.sort()
print(numeros)

#agregar elementos

cantantes.append("Natalia")
cantantes.insert(1,"David Bisbal")
print(cantantes)

#eliminar elementos
cantantes.pop(1)
cantantes.remove("Metallica")

print(cantantes)

#dar la vuelta a una lista
print(numeros)
numeros.reverse()
print(numeros)

#buscar elemento en una lista
print("Mon Laferte" in cantantes)

#contar elementos
print(len(cantantes))

#cuantas veces aparce un elemento en la lista

print(numeros.count(8))
numeros.append(8)

print(numeros.count(8))

#buscar indices donde aparece
print(cantantes.index("Mon Laferte"))

#Unir listas

cantantes.extend(numeros)
print(cantantes)
