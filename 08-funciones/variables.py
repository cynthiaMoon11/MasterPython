"""
Variables locales y Variables globales
local: se define dentro de la función
global: se declaran fuera de las funciones 
y estan disponibles dentro y fuera de las funciones
"""
#Variable global
frase="Hola, soy Cynthia"

print(frase)

def holaMundo():
    frase = "hola mundo"
    print("Dentro de la función: ")
    print(frase)

    year=2021
    print(year)

    global website
    website= "cynthia.es"
    print("dentro",website)

holaMundo()

print("fuera", website)