"""
mostrar las tablas de multiplicar de los números del 1 al 10
mostrando el título de la tabla.
"""

for cont in range (1,11) :
   print(f"tabla del {cont}")
   num=1
   while num <=10:
        print(f"{num} x {cont} = {num*cont}")
        num+=1
        print("\n")

for cabecera in range (1, 11):
    print(f"###########################")
    print(f"#######*Tabla del {cabecera}*#######")
    print(f"###########################")
    for numero in range (1, 11):
        print(f"{numero} X {cabecera} = {numero*cabecera} ")
    print("\n") 