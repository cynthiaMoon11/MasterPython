"""
tenemos que usar el paquete open dentro de io
"""
from io import open
import pathlib
import shutil #para copiar, renombrar, elimmiar, etc archivos

#abrir archivo
#archivo = open("./14-sistema-archivos/fichero_texto.txt","a+") 
#archivo = open("fichero_texto.txt","a+")

#poner la ruta absoluta
ruta=str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
print(ruta)
archivo =open(ruta, "a+")

#archivo.write("******Soy Cynthia*****\n")

#cerrar archivo

archivo.close()

#abrir archivo con permiso de lectura

ruta=ruta=str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
archivoLectura =open(ruta, "r")

#leer contenido
#contenido =archivoLectura.read()

#print(contenido)

#leer contenido por lineas y guardar en una lista

lista=archivoLectura.readlines()
archivoLectura.close()
print(type(lista))

for elemento in lista:
    #listaElemento=elemento.split()  mete cada elemento en una lista
    #print(listaElemento)
    print(elemento.upper())

"""
rutaOriginal=str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
rutaNueva=str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copia.txt"
rutaAlternativa="./07-ejercicios/fichero_copiado77.txt"
shutil.copyfile(rutaOriginal,rutaAlternativa)
"""
#mover un archivo
"""
rutaOriginal=str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copia.txt"
rutaNueva=str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto_copia_Nuevo.txt"

shutil.move(rutaOriginal, rutaNueva )
"""
#eliminar archivos

import os
"""
rutaNueva=str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto_copia_Nuevo.txt"

os.remove(rutaNueva)
#comprobar si un archivo existe
"""
import os.path

print(os.path.abspath("./"))


rutaComprobar="./fichero_texto.txt"

print(rutaComprobar)

if os.path.isfile(rutaComprobar):
    print("El archivo exite")

else:
    print("el archivo no exite")

"""
if os.path.isfile(os.path.abspath("./14-sistema-archivos")+"/fichero_texto.txt"):
    print("El archivo exite")

else:
    print("el archivo no exite")
"""

