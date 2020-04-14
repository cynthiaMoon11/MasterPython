"""
colecciones de datos bajo un solo nombre
para acceder a ellas necesitamos indices númericos
"""
pelicula="Batman"
#definir una lista
peliculas=["Barman", "Spiderman", "El señor de los anillos"]
#define con una tupla
cantantes =list(("2pac" , "Drake" , "Shakira"))
years = list(range(2020, 2050))
variada = ["Victor",20, 1.4, "texto"]
"""
print(peliculas)
print(cantantes)
print(years)
print(variada)
"""
#indices
peliculas[1]="Gran Torino" #modifico el elemento 1 del array
print(peliculas[2])
print(peliculas[-2]) #cuenta de atras para delante  empieza en -1
print(cantantes[1:3]) # un rango en la lista 
print(cantantes[1:]) #imprime del uno en adelante hsata el final
print(peliculas)

#añadir elementos de la lista
cantantes.append("kase O")
print(cantantes)

#recorrer lista

"""
nuevaPeli=" "
while nuevaPeli != "parar":
    nuevaPeli=input("introduce una nueva pelicula: ")
    if nuevaPeli!="parar":
        peliculas.append(nuevaPeli)

print("\n****listado peliculas****")
for pelicula in peliculas:
    print (f"{peliculas.index(pelicula)+1}.{pelicula}")
"""
#Lista multidimensionales
print("\n****Lista de contactos****")

contactos = [
    [
        "Antonio",
        "antonio@a.com"
    ],
    [
        "Antonia",
        "anto@a.com"
    ],
    [
        "Cynthia",
        "cynt@a.com"
    ]
]
"""
print(contactos)
print(contactos[2][0])
"""

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) ==0:
            print("Nombre:" + elemento)
        else:
            print("Correo: " + elemento)
        
    print("\n")