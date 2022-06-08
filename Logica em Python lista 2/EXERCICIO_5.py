

NOTA_1 = int(input('Primeira nota: '))
NOTA_2 = int(input('Segunda nota: '))

MEDIA = (NOTA_1 + NOTA_2) / 2

if MEDIA > 7 and MEDIA < 10:
    print('APROVADO')
elif MEDIA == 10:
    print('APROVADO COM DISTINÇÃO')
else:
    print('REPROVADO ')
