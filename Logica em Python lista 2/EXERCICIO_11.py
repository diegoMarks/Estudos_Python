SALARIO = float(input('Insira o valor do salário: '))

if SALARIO <= 280.00:
    REAJUSTE = (SALARIO * 20) / 100
    PERCENTUAL = '20%'
elif SALARIO <= 700.00:
    REAJUSTE = (SALARIO * 15) / 100
    PERCENTUAL = '15%'
elif SALARIO <= 1500.00:
    REAJUSTE = (SALARIO * 10) / 100
    PERCENTUAL = '10%'
elif SALARIO > 1500.00:
    REAJUSTE = (SALARIO * 5) / 100
    PERCENTUAL = '5%'

print('Salário antes do reajuste: ', SALARIO)
print('Percentual de aumento aplicado: ', PERCENTUAL)
print('Valor do aumento: ', REAJUSTE)
print('Novo salário após aumento: ', REAJUSTE + SALARIO)
