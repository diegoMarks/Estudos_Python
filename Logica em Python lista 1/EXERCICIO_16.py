AREA_PINTADA = float(input('Área a ser pintada em metros quadrados: '))

GALAO_TINTA = 0
QUANTIDADE_GALOES = 0
PRECO_GALAO = 0

while GALAO_TINTA < AREA_PINTADA:
    QUANTIDADE_GALOES = QUANTIDADE_GALOES + 1
    GALAO_TINTA = GALAO_TINTA + (18 * 3)
    PRECO_GALAO = PRECO_GALAO + 80.00

print(f'Quantidade de latas de tinta: {QUANTIDADE_GALOES}')
print(f'Preço: R$ {PRECO_GALAO}')
