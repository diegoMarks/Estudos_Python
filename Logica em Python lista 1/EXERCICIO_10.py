

CONTINUAR = 'S'

while CONTINUAR == 'S':
    CELSIUS = float(input('Insira a temperatura em Celsius: '))
    FARENHEIT = ((CELSIUS * 1.8) + 32)
    print('Temperatura em Farenheit: {:3.2f} Cº Farenheit'.format(FARENHEIT))
    CONTINUAR = input('Deseja efetuar o programa novamente? [S] [N]: ')
    if CONTINUAR == 'S' or 's':
        continue
print('Encerrando programa')
