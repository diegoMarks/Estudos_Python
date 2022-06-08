QT_HORA = int(input('Insira a quantidade de horas: '))
VALOR_HORA = float(input('Insira o valor da hora: '))

SALARIO_BRUTO = QT_HORA * VALOR_HORA
FGTS = (SALARIO_BRUTO * 11) / 100
INSS = (SALARIO_BRUTO * 10) / 100
VALOR_IR = 1


if SALARIO_BRUTO <= 900:
    VALOR_IR = 0
    IR = 0
elif SALARIO_BRUTO <= 1500:
    VALOR_IR = (SALARIO_BRUTO * 5) / 100
    IR = 5
elif SALARIO_BRUTO <= 2500:
    VALOR_IR = (SALARIO_BRUTO * 10) / 100
    IR = 10
elif SALARIO_BRUTO > 2500:
    VALOR_IR = (SALARIO_BRUTO * 20) / 100
    IR = 20


print(
    f'Salário bruto {QT_HORA} * {VALOR_HORA}                               : R$ {SALARIO_BRUTO}')
print(
    f'(-) IR ({IR}%)                                           : R$', VALOR_IR)
print('(-) INSS (10%)                                        : R$', INSS)
print('FGTS (11%)                                            : R$', FGTS)
print('Total de descontos                                    : R$',
      VALOR_IR + INSS)
print('Salário Liquido                                       : R$',
      SALARIO_BRUTO - (VALOR_IR + INSS))
