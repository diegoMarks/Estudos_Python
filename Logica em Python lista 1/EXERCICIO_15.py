GANHO_HORA = float(input('Quanto você ganha por hora: '))
TRABALHO_HORA = float(input('Quantas horas você trabalha por mês: '))
SALARIO_BRUTO = GANHO_HORA * TRABALHO_HORA
print('+ Salário bruto : R$', SALARIO_BRUTO)
print('- IR (11%) : R$', (SALARIO_BRUTO * 11)/100)
print('- INSS (8%) : R$', (SALARIO_BRUTO * 8)/100)
print('- Sindicato (5%) : R$', (SALARIO_BRUTO * 5)/100)
print('= Salário Liquido : R$', SALARIO_BRUTO - (((SALARIO_BRUTO*(11+8+5))/100)))
