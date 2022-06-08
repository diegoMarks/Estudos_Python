from statistics import mean


N1 = float(input('Insira a primeira nota do aluno: '))
N2 = float(input('Insira a segunda nota do aluno: '))
N3 = float(input('Insira a terceira nota do aluno: '))

N4 = [N1, N2, N3]
MEDIA = mean(N4)
MEDIA_F = round(MEDIA, 1)

if MEDIA_F < 7:
    print('Reprovado!')
    print('Média do aluno: ', MEDIA_F)
elif MEDIA_F < 10:
    print('Aprovado!')
    print('Média do aluno: ', MEDIA_F)
elif MEDIA_F == 10:
    print('Aprovado com distinção!')
    print('Média do aluno: ', MEDIA_F)
