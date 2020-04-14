"""
pedir 15 notas e imprimir ls aprobados y los suspendidos

"""

cont=1
apro=0
sus=0

numAlum=int(input("cuantos notas vas a ingresar?  "))

while cont < numAlum:
    nota=int(input(f"ingresa una nota al alumno {cont} "))

    if nota>=5:
        apro+=1
    else:
        sus+=1

    cont+=1

print(f"alumnos aprobados {apro}")
print(f"Alumnos suspendidos {sus}")