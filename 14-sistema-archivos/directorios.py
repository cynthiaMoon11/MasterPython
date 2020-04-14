import os
import shutil

#crear carpeta

if not os.path.isdir("./14-sistema-archivos/mi_carpeta"):
    os.mkdir("./14-sistema-archivos/mi_carpeta")
else:
    print("Ya existe el directorio")

#Eliminar

#os.rmdir("./14-sistema-archivos/mi_carpeta")
"""
rutaOriginal="./14-sistema-archivos/mi_carpeta"
rutaNueva="./14-sistema-archivos/mi_carpeta_copia"

shutil.copytree(rutaOriginal, rutaNueva )
"""
#os.rmdir("./14-sistema-archivos/mi_carpeta_copia")


# para ver el contenido de una carpeta
contenido=os.listdir("./14-sistema-archivos/mi_carpeta")
print("El contenido de esta carpeta es: ", contenido)

for fichero in contenido:
    print("fichero: ", fichero)

