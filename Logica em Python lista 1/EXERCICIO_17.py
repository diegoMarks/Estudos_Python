from math import ceil
print('')
AREA_PINTADA = float(input('Área a ser pintada: '))

LATA_G = ceil((AREA_PINTADA / (18 * 6)))
LATA_P = ceil(AREA_PINTADA / (3.6 * 6))
TINTA_MISTA = ceil(((LATA_G + LATA_P) / 0.10) + LATA_G + LATA_P)
TOTAL_DE_LITROS = 108 + 21.6
QT_GALOES_MISTURADOS = 0

if TOTAL_DE_LITROS < AREA_PINTADA:
    while TOTAL_DE_LITROS < AREA_PINTADA:
        QT_GALOES_MISTURADOS = QT_GALOES_MISTURADOS + 1
        TOTAL_DE_LITROS = TOTAL_DE_LITROS + TOTAL_DE_LITROS
else:
    QT_GALOES_MISTURADOS = QT_GALOES_MISTURADOS + 1

print('')
print(f'Quantidade de latas de 18 litros: {LATA_G}')
print('Preço a pagar: ', LATA_G * 80.00)
print('')
print(f'Quantidade de latas de 3.6 litros: {LATA_P}')
print('Preço a pagar: ', LATA_P * 25.00)
print('')
print(f'Quantidade de latas misturadas necessárias: {QT_GALOES_MISTURADOS}')
print('Preço a pagar: ', (QT_GALOES_MISTURADOS * 80.00) +
      (QT_GALOES_MISTURADOS * 25.00))
print('')
