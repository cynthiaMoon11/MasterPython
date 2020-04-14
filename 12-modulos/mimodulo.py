def holaMundo (nombre):
    return f"Hola, {nombre}"


def calculadora(num1, num2, basicas=True):
    suma=num1+num2
    resta=num1-num2
    multi=num1*num2
    div=num1/num2
    cadena = " "
    if basicas!=True:        
        cadena += "suma: " + str(suma)
        cadena +="\n"
        cadena += "resta: " + str(resta)
        cadena +="\n"
    else:
        cadena += "multiplicacion: " + str(multi)
        cadena +="\n"
        cadena += "division: " + str(div)

    
    return cadena

