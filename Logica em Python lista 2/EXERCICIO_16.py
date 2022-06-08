import math


A = float(input('Insira o valor de A: '))
if A == 0:
    print('A = 0, finalizando o programa..')
    exit()
B = float(input('Insira o valor de B: '))
C = float(input('Insira o valor de C: '))

DELTA = (B ** 2) - 4 * A * C
X_POSITIVO = - B + math.sqrt(DELTA) / (2 * A)
X_NEGATIVO = - B - math.sqrt(DELTA) / (2 * A)

if DELTA < 0:
    print('Delta negativo, não possuí raizes reais, finalizando programa..')
    exit()
elif DELTA > 0:
    print('Delta positivo, equação possuí duas raízes reais!')
    print('Delta: {:3.2f} '.format(DELTA))
    print('X Positivo: {:3.2f}'.format(X_POSITIVO))
    print('X Negativo: {:3.2f}'.format(X_NEGATIVO))
