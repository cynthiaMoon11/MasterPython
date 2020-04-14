"""
crear un scrip 4 variables
lista
string
entero
booleano
Imprimir un mensaje segun el tipo. usar funciones
"""
def traducirTipo(tipo):
    resultado=None
    if tipo==list:
        resultado="Lista"
    elif tipo == str:
        resultado="Cadena"
    elif tipo == int:
        resultado="Entero"
    elif tipo == bool:
        resultado="Booleano"
    return resultado

def comprobarTipado (dato, tipo):
    test = isinstance(dato, tipo)
    result=""

    if test:
        result= f"Este dato es del tipo {traducirTipo(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    return result

miLista= ["hola mundo", 77]
titulo = "master python"
numero = 99
verdadero = False

print(comprobarTipado(titulo, str))
print(comprobarTipado(miLista, list))
print(comprobarTipado(numero, int))
print(comprobarTipado(verdadero, bool))

