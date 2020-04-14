"""
cuadrados de los 60 números primeros
con while y for
"""

contador=0
while contador <=60:  

        cuadrado=contador*contador
        print(f"el cuadrado de {contador} es {cuadrado}") 

        contador+=1


for cont in range (0,61):
    print(f"el cuadrado de {cont} es {cont*cont}") 
