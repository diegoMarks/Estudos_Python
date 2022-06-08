PESO_DE_PEIXE = float(input('Peso dos peixes: '))

if PESO_DE_PEIXE > 50:
    PESO_EXCESSO = PESO_DE_PEIXE - 50
    MULTA = PESO_EXCESSO * 4
    print(
        'Você está com {:3.2f} KG acima do limite permitido, terá de pagar uma multa de R$ {:3.2f}'.format(PESO_EXCESSO, MULTA))
else:
    print('Peso correto, não precisa pagar multa')
