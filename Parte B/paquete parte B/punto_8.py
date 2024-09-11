# Ejercicio 8:
# Genere un segundo módulo en el cual existan las funciones necesarias para la gestión del
# equipo de recursos humanos de la empresa.
# En el mismo debe existir una primera función que calcule el valor del salario de cada
# empleado. El valor del mismo es la cantidad de horas trabajadas multiplicadas por 10 y un
# incremento del 3% por cada año de antigüedad.
# También debe haber una segunda función que calcule la productividad del empleado. La
# misma se calcula como la cantidad de artefactos producidos, dividido por la cantidad de
# horas de trabajo.
# En tercer lugar debe haber una función que reporte toda la información del empleado
# incluyendo la calculada en las dos funciones anteriores, nombre y edad.

def calcular_salario(cantidad_horas_trabajadas: float, años_antiguedad: int) -> float:
    salario_total = cantidad_horas_trabajadas * 10 * (1 + años_antiguedad * 3/100)
    return salario_total

def calcular_productividad(cantidad_artefactos_produciodos: int, cantidad_horas_trabajadas: float) -> float:
    productividad_empleado = cantidad_artefactos_produciodos / cantidad_horas_trabajadas
    return productividad_empleado

def mostrar_datos(nombre: str, edad: int, salario_total: float, productividad_empleado: float):
    print(f'\nDATOS:')
    print(f'nombre: {nombre}')
    print(f'edad: {edad}')
    print(f'salario total: {salario_total}')
    print(f'productividad: {productividad_empleado}')

#prueba
nombre = input('ingrese su nombre: ')
edad = int(input('ingrese su edad: '))
cantidad_horas_trabajadas = float(input('ingrese la cantidad de horas trabajadas: '))
años_antiguedad = int(input('ingrese sus años de antigüedad: '))
cantidad_artefactos_producidos = int(input('ingrese la cantidad de artefactos producidos: '))

salario_total = calcular_salario(cantidad_horas_trabajadas, años_antiguedad)
productividad_empleado = calcular_productividad(cantidad_artefactos_producidos, cantidad_horas_trabajadas)

mostrar_datos(nombre, edad, salario_total, productividad_empleado)