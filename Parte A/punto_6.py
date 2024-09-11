# 6 - Realizar un programa que: asigne a las variables numero1 y numero2 los valores
# solicitados al usuario, valide los mismos entre 10 y 100, asigne a la variable operacion el
# valor solicitado al usuario: 's'-sumar, 'r'-restar (validar),realice la operación de dichos valores
# a través de una función. Mostrar el resultado por pantalla.

def ingresar_numero() -> float:
    numero = float(input('ingrese un numero entre 10 y 100: '))

    while numero < 10 or numero > 100:
        numero = float(input('error, ingrese un numero entre 10 y 100:  : '))
    return numero

def calcular_suma_o_resta(calcular_num1: float, calcular_num2, signo: str) -> float:
    if signo == 's':
        return calcular_num1 + calcular_num2
    elif signo == 'r':
        return calcular_num1 - calcular_num2
    
numero_1 = ingresar_numero()
numero_2 = ingresar_numero()
operador = input('ingrese un operador (r o s): ')

print(calcular_suma_o_resta(numero_1, numero_2, operador))
    