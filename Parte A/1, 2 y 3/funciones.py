# 1- Crear una función que muestre por pantalla el número que recibe como parámetro
def mostrar_numero(numero: int) -> None:
    print(numero)

# 2- Crear una función que permita determinar si un número es par o no. La función retorna
# “True” en caso afirmativo y “False” en caso contrario. Probar en el programa principal
# realizando la invocación o llamada.
def definir_par(numero: int) -> bool:
    if numero % 2 == 0:
        return True
    else:
        return False
    
# 3- Especializar la función del punto 1 para que valide el número en un rango determinado
# pasado por parámetro “desde”-“hasta”.
def definir_numero_rango(numero: int, desde: int, hasta: int):
    if numero < desde or numero > hasta:
        print('el numero no esta dentro del rango')
    elif numero % 2 == 0:
        print(True)
    else:
        print(False)
        
