# 5 - Realizar un programa que: asigne a la variable numero1 un valor solicitado al usuario,
# valide el mismo entre 10 y 100, realice un descuento del 5% a dicho valor a través de una
# función llamada realizarDescuento(). Mostrar el resultado por pantalla. Atención: pueden
# reutilizarse funciones ya creadas.

def hacer_descuento(numero: int) -> float:
    return numero - (numero * 5/100)

numero_1 = float(input('ingrese un numero entre 10 y 100: '))
if numero_1 < 100 or numero_1 > 10:
    print(f'su numero con descuento del 5% es: {hacer_descuento(numero_1)}')
else:
    print('no tiene ningun descuento')
