nombre="Cynthia Escoba"

#funciones generales
print(nombre)
print(type(nombre))

#Detectar el tipado
comprobar=isinstance(nombre, str)
if comprobar:
    print("es un string")
else:
    print("no es una cadena")

if not isinstance(nombre, float):
    print("La variable no es un flotante")

#Limpiar espacios
frase= "       espacios     "
print(frase)
print(frase.strip())

#Eliminar variables
"""
year==2021
print(year)
del year
"""
#comprobar variables vacías

texto= " ff "

if len(texto) <= 0:
    print("la variable está vacía")
else:
    print(F"la cadena tiene {len(texto)}")

#Encontrar caracteres

frase="la vida es bella"

print(frase.find("vida"))

#Reemplazar palabras en un string

nuevaFrase = frase.replace("vida", "moto")

print (nuevaFrase)

#Mayusculas y Minusculas

print(nombre)
print(nombre.lower())
print(nombre.upper())
