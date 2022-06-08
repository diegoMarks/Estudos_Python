RESPOSTA = 'S'

while RESPOSTA == 'S' or 's':
    FARENHEITH = float(input('Insira o valor da temperatura em Fareinheit: '))
    CELSIUS = 5*((FARENHEITH - 32) / 9)
    print('Temperatura em Celsius: {:3.2f}'.format(CELSIUS))
    RESPOSTA = input('Deseja continuar? [S] ou [N]: ')
    if RESPOSTA == 'N' or 'n':
        break
    elif RESPOSTA == 'S' or 's':
        continue
