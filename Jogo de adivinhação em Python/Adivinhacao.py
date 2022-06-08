import random



def jogar():

    print('*********************************')

    print('Bem vindo ao jogo de Adivinhação!')
    print('*********************************')

    NUMERO_SECRETO = random.randrange(1, 100)
    TOTAL_DE_TENTATIVAS = random.randrange(2, 5)
    TOTAL_PONTOS = 1000

    print('Qual nível de dificuldade?')
    print('(1) Fácil (2) Médio (3) Díficil')

    NIVEL = int(input('Defina o nível: '))

    if NIVEL == 1:
        TOTAL_DE_TENTATIVAS = 20
    elif NIVEL == 2:
        TOTAL_DE_TENTATIVAS = 10
    else:
        TOTAL_DE_TENTATIVAS = 5

    for RODADA in range(1, TOTAL_DE_TENTATIVAS + 1):
        print(f'Tentativa {RODADA} de {TOTAL_DE_TENTATIVAS}')
        print(f'n = {NUMERO_SECRETO}')
        STR_CHUTE = input('Digite um número entre 1 e 100: ')
        print('Você digitou ', STR_CHUTE)
        CHUTE = int(STR_CHUTE)

        if CHUTE < 1 or CHUTE > 100:
            print('Você deve digitar um número entre 1 e 100!')
            continue

        ACERTOU = NUMERO_SECRETO == CHUTE
        MAIOR = CHUTE > NUMERO_SECRETO
        MENOR = CHUTE < NUMERO_SECRETO

        if ACERTOU:
            print(f'Você acertou e  fez {TOTAL_PONTOS}')
            break
        if MAIOR:
            print('Você errou! O seu chute foi maior do que o número secreto.')
        elif MENOR:
            print('Você errou! O seu chute foi menor que o número secreto.')
            PONTOS_PERDIDOS = int(abs(NUMERO_SECRETO - CHUTE))
            TOTAL_PONTOS = TOTAL_PONTOS - PONTOS_PERDIDOS

    print('Fim de jogo')

if __name__ == '__main__':  
    jogar()
