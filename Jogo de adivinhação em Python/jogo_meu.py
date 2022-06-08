import forca
import Adivinhacao


def escolhe_jogo():

    print('******************************************')
    print('**********Escolha o seu jogo**************')
    print('******************************************')

    print('(1) Forca (2) Adivinhacao (0) Sair')

    jogo = int(input('Qual jogo?'))

    while jogo != 0:
        if jogo == 1:
            print('Jogando forca')
            forca.jogar()
        elif jogo == 2:
            print('Jogando Adivinhacao')
            Adivinhacao.jogar()


print('Encerrando..')


if __name__ == '__main__':
    escolhe_jogo()
