PRODUTO_1 = float(input('Valor produto 1: '))
PRODUTO_2 = float(input('Valor produto 2: '))
PRODUTO_3 = float(input('Valor produto 3: '))

MAIS_BARATO = 'Produto 1'

if PRODUTO_2 < PRODUTO_1 and PRODUTO_2 < PRODUTO_3:
    MAIS_BARATO = 'Produto 2'
elif PRODUTO_3 < PRODUTO_1 and PRODUTO_3 < PRODUTO_2:
    MAIS_BARATO = 'Produto 3'


print('Você deve comprar o', MAIS_BARATO)
