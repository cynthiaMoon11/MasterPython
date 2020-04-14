"""
Modulos: son funcinalidades ya hechas para reutilizar.

podemos conseguir modulos que ya vienen en el lenguaje, modulos en internet
y tambien crear los propios .
"""
"""
import mimodulo
print(mimodulo.holaMundo("Cynthia"))
print(mimodulo.calculadora(3,5,True))
"""
"""
from mimodulo import holaMundo
print(holaMundo("Cynthia"))
"""

from mimodulo import * #Importa todo
print(holaMundo("Cynthia"))

import datetime

print(datetime.date.today())

fechaCompleta = datetime.datetime.now()

print(fechaCompleta.year)
print(fechaCompleta.month)
print(fechaCompleta.day)

fechaPersonalizada = fechaCompleta.strftime("%d/%m/%Y/%H,")
print(fechaPersonalizada)

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())

#MODULO MATEMÁTICAS

import math

print("Raiz cuadrada de 10: ", math.sqrt(10))

print(math.pi)

print("redondear", math.ceil(6.56845252))

#Modulo random

import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15,67))








