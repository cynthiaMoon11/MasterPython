"""
imprimir los números dentro del rango que hace el usuario
"""
num1=int(input("introduce un num1:"))
num2=int(input("introduce un num2:"))
if num1<num2:
        
        for contador in range (num1,(num2+1)):    
                print(contador)  
else:
        print("El número 1 debe ser mayor al numero 2")


if num1<num2:
        
       while num1 <=num2:
        print(num1) 
        num1+=1
else:
        print("El número 1 debe ser mayor al numero 2")


        
