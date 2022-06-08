PRIMEIRO_NUMERO = int(input('Insira o primeiro número que deve ser inteiro: '))
SEGUNDO_NUMERO = int(input('Insira o segundo número que deve ser inteiro: '))
TERCEIRO_NUMERO = float(
    input('Insira o terceiro número que deve ser real número: '))


print('**********')
print('*REPOSTAS*')
print('**********\n')

print('*****************************************************************')
PRIMEIRA_RESPOSTA = print('* O produto do primeiro número:',
                          (PRIMEIRO_NUMERO * 2), 'com metade do segundo: ', (SEGUNDO_NUMERO / 2), ' *')
print('*****************************************************************\n\n')


print('*****************************************************')
SEGUNDA_RESPOSTA = print('* Soma do triplo do primeiro com o terceiro: ', ((
    PRIMEIRO_NUMERO * 3) + TERCEIRO_NUMERO), ' *')
print('*****************************************************\n')


TERCEIRA_RESPOSTA = print(
    'Terceiro número elevado ao cubo: ', (TERCEIRO_NUMERO ** 3))
