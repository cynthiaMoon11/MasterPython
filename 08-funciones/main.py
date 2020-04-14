"""
Función: es un conjunto de instrucciones agrupadas bajo un nombre concreto que 
puede llamarce tantas veces sea necesario.

def nombreDeLaFuncion(parametros):
    bloque de código/ conjunto de instrucciones

nombreDelaFuncion(parametro)
"""

#Ejemplo 1

print("***Ejemplo 1***")

#deficion función
def muestraNombres():
     print("Victor")
     print("cynthia")
     print("Rafael\n")

#llamada a la función
muestraNombres()
"""
#Ejemplo 2
#Parámetros
print("***Ejemplo 2***")


def mostrarTuNombre(nombre , edad):
    print(f"{nombre}")
    if edad>=18:
        print("y eres mayor de edad")

nombre=input("Introduce tu nombre: ")
edad=int(input("Introduce tu edad: "))
mostrarTuNombre(nombre,edad)
"""

#Ejemplo 3
print("***Ejemplo 3***")

def tabla(numero):
    print(f"Tabla del {numero}")

    for cont in range(11):
        opera=numero*cont
        print(f"{numero} x {cont} = {opera}")
    print("\n")


tabla(3)

for numeroTabla in range(1,11):
    tabla(numeroTabla)

#Ejemplo 4
print("***Ejemplo 4***")

#Parámetros opcionales

def getEmpleado(nombre, dni = False):
    print("Empleado")
    print(f"Nombre: {nombre}")
    print(f"DNI: {dni}")

nombre="Cynthia"
getEmpleado(nombre, "1234567r")

#Ejemplo 5  devolver datos return
print("***Ejemplo 5***")

def saludame(nombre):
    saludo = f"Hola, saludos {nombre}"

    return saludo

print(saludame("Cynthia"))    

#Ejemplo 6  
print("***Ejemplo 6***")

def calculadora(num1, num2, basicas=True):
    suma=num1+num2
    resta=num1-num2
    multi=num1*num2
    div=num1/num2
    cadena = " "
    if basicas!=True:        
        cadena += "suma: " + str(suma)
        cadena +="\n"
        cadena += "resta: " + str(resta)
        cadena +="\n"
    else:
        cadena += "multiplicacion: " + str(multi)
        cadena +="\n"
        cadena += "division: " + str(div)

    
    return cadena

print(calculadora(55,55, True))
    
#Ejemplo 7 
print("***Ejemplo 7***")

def getNombre(nombre):
    texto=f"El nombre es: {nombre}"
    return texto

def getApellido(apellidos):
    texto=f"Los apellidos son: {apellidos}"
    return texto

def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellido(apellidos)
    return texto

print(devuelveTodo("Cynthia" , "Escobar"))

#Ejemplo 8 o funciones lambda funciones anonimmas
print("***Ejemplo 8 ***")

dimeElYear= lambda year: f"El año es {year}"

print(dimeElYear(2033))

        