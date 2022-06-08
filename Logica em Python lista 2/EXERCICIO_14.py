from asyncio.windows_events import NULL
from tkinter import E


NOTA = float(input('Insira a nota: '))

CONCEITO = NULL
RESULTADO = NULL

if NOTA <= 4.0:
    CONCEITO = E
    RESULTADO = 'REPROVADO!'
elif NOTA <= 6.0:
    CONCEITO = 'D'
    RESULTADO = 'REPROVADO!'
elif NOTA <= 7.5:
    CONCEITO = 'C'
    RESULTADO = 'APROVADO!'
elif NOTA <= 9.0:
    CONCEITO = 'B'
    RESULTADO = 'APROVADO!'
elif NOTA == 10.0:
    CONCEITO = 'A'
    RESULTADO = 'APROVADO!'


print('Média de aproveitamento: ',NOTA)
print('Conceito: ',CONCEITO)
print('Resultado: ',RESULTADO)
