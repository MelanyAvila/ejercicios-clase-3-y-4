# 4 - Realizar un programa en donde se puedan utilizar los prototipos de la función Restar en
# sus 4 combinaciones.
# A- restar1(int, int)->int:
def restar_1(numero_1: int, numero_2: int) -> int:
    return numero_1 - numero_2

print(restar_1(10, 5))

# B- restar2()->int:
def restar_2() -> int:
    return 20 - 5

print(restar_2())

# C- restar3(int, int):
def restar_3(numero_1: int, numero_2: int):
    print(numero_1 - numero_2)

restar_3(9, 3)

# D- restar4():
def restar_4():
    print(22 - 2)

restar_4()
