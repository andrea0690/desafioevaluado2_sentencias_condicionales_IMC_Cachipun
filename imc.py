#  Ejercicio 1. IMC

weight = float(input('Ingrese el valor de su peso en kilogramos: '))
height = float(input('Ingrese su estatura en centimetros: '))
height = height/100

imc = (weight)/(height*height)

if imc < 18.5:
    print(f'Su IMC es igual a: {imc:.2f} \n La clasificación OMS es Bajo peso')
elif imc <= 25:
    print(f'Su IMC es igual a: {imc:.2f} \n La clasificación OMS es Adecuado')
elif imc <= 30:
    print(f'Su IMC es igual a: {imc:.2f} \n La clasificación OMS es Sobrepeso')
elif imc <= 35:
    print(f'Su IMC es igual a: {imc:.2f} \n La clasificación OMS es Obesidad Grado I')
elif imc <= 40:
    print(f'Su IMC es igual a: {imc:.2f} \n La clasificación OMS es Obesidad Grado II')
else:
    print(f'Su IMC es igual a: {imc:.2f} \n La clasificación OMS es Obesidad Grado III')
    
    
    
    