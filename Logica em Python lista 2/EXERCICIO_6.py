from re import X


NUM_1 = int(input('Número 1: '))
NUM_2 = int(input('Número 2: '))
NUM_3 = int(input('Número 3: '))


if (NUM_1 > NUM_2) and (NUM_1 > NUM_3):
    print('Primeiro número é o maior')
elif (NUM_2 > NUM_1) and (NUM_2 > NUM_3):
    print('Segundo número é o maior')
else:
    print('Terceiro número é o maior')
