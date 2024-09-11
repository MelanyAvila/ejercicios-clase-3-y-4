# Ejercicio 7:
# Supongamos que le solicito a chatgpt una función para calcular valores de ventas de
# productos con impuestos para una determinada empresa:
# La respuesta de chatgpt es:
# def calculo_impuestos(valor_exportaciones, valor_ventas_nacionales, iva = 21, retenciones = 15):
#     resultado_nacional = valor_ventas_nacionales* (1 / (1 + (iva / 100)))
#     resultado_exportaciones = valor_exportaciones* (1 - (retenciones / 100))
#     resultado_final = resultado_nacional + resultado_exportaciones
#     return resultado_final
# ¿Considera que cumple con los objetivos de una función?
# Corrija la función dentro de un módulo, divida en distintas funciones de ser necesario,
# documente y denomine correctamente.

def calcular_ventas_exportaciones(valor_exportaciones: float, retenciones: float = 15) -> float:
    # calcula las ventas por exportaciones con las retenciones
    resultado_exportaciones = valor_exportaciones * (1 - (retenciones / 100))
    return resultado_exportaciones

def calcular_ventas_nacionales(valor_nacionales: float, iva: int = 21) -> float:
    # calcula ventas nacionales con iva aplicado
    resultado_nacionales = valor_nacionales * (1 / (1 + (iva / 100)))
    return resultado_nacionales

def calcular_impuestos(resultado_nacionales: float, resultado_exportaciones: float) -> float:
    # suma los resultados de calcular_ventas_exportaciones y calcular_ventas_nacionales 
    resultado_final = resultado_exportaciones + resultado_nacionales
    return resultado_final

'''
Separe la funcion en dos e hice una tercera para sumar los resultados.
Las funciones sirven para descomponer una tarea especifica, las tareas no eran independientes y
esto tambien lleva a que no se puedan reutilizar.
'''