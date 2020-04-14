nada= None #no tiene nada
cadena= "Hola soy Cynthia "
entero=99
flotante =4.2
booleano=True
lista=[10, 20, 30, 100, 200]
listaString=[44, "treinta",30,"cuarenta"]
tuplaNoCambia=("master", "en", "python")
diccionario={
    "nombre":"Víctor",
    "apellido":"Robles",
    "curso":"Master en Python"

}
rango=range(9)
dato_byte=b"Probando"
#imprimir variable
print("nada")
print(entero)
print(flotante)
print(booleano)
print(lista)
print(diccionario)
print(rango)
print(dato_byte)
#mostrar tipo de dato
print(type(nada))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))

#conversiones

texto="Hola soy un texto"
numero= str(776) #convierte de int a string
print(texto + " " + numero)

numero2=int(numero) #convierte a int
print(type(numero2))

numero3=float(numero2) #convierte en float
print(numero3)
print(type(numero3))



