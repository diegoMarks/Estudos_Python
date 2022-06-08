NUM_1 = int(input('Número 1: '))
NUM_2 = int(input('Número 2: '))
NUM_3 = int(input('Número 3: '))

MAIOR = NUM_1

if (NUM_2 > NUM_1) and (NUM_2 > NUM_3):
    MAIOR = NUM_2
elif (NUM_3 > NUM_1) and (NUM_3 > NUM_2):
    MAIOR = NUM_3

MENOR = NUM_1
if NUM_2 < NUM_1 and NUM_2 < NUM_3:
    MENOR = NUM_2
elif(NUM_3 < NUM_1) and (NUM_3 < NUM_2):
    MENOR = NUM_3

MEDIO = NUM_1
if NUM_2 < NUM_1 and NUM_2 > NUM_3:
    MENOR = NUM_2
elif(NUM_3 < NUM_1) and (NUM_3 > NUM_2):
    MENOR = NUM_3

print('Ordem decrescente: ', MAIOR, MEDIO, MENOR)
