#capturar excepciones y manejar errores en código
#susceptible a errores

"""
try:
    nombre=input("Cual es tu nombre")
    if len(nombre)>1:
        nombre_usuario="El nombre es " + nombre
    print(nombre_usuario)

except:
    print("has introducido un valo no válido")
else:
    print("nombre introducido correctamente")
finally:
    print("fin del programa")

# ejercicio 1 de ejercicios carpeta 11

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
"""
#Multiples excepciones
""""
try:
    num=int(input("Introduce un numero para elevarlo al cuadrado"))
    print("el cuadrado es: "+str(num*num))
except TypeError:
    print("Tipo de dato no válido")
except ValueError:
    print("Valor inválido")
except Exception as e:
    print(type(e))
    print("Ha ocurrido un error", type(e).__name__)
"""
#excepciones personalizadas (Lanzar excepciones)

nombre=input("introduce nombre: ")
edad=int(input("Digita tu edad: "))

try:

    if edad <5 or edad > 110:
        raise ValueError ("La edad introducida no es real")
    elif len(nombre)<=1:
        raise ValueError("el nombre no está completo")
    else:
        print(f"Bienvenido {nombre}, tienes {edad}")
except Exception as e:
    print("Existe un error:", e)





