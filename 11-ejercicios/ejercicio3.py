"""
comprobar una si una variable está vacía y si lo está que 
la rellene con una cadena en minuscula
mostrarla en Mayucula
"""

texto= " "

if len(texto.strip()) <=0:
    texto = "texto en minúsculas"
    print (texto.upper())

else:
    print(f"La variable tiene contenido {texto}")