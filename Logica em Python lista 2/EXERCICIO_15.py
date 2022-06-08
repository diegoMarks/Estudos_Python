A = float(input('Insira o lado do triângulo A: '))
B = float(input('Insira o lado do triângulo B: '))
C = float(input('Insira o lado do triângulo C: '))

if ((A == B) and (A == C)) or ((B == C) and (B == A)) or ((C == A) and (C == B)):
    print('Triângulo Equilátero')
elif (A == B) or (A == C) or (B == C):
    print('Triângulo é Isósceles')
elif (A != B) and (A != C) and (B != C):
    print('Triângulo Escaleno')
