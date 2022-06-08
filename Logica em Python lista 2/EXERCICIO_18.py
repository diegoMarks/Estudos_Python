from time import strptime
from tomlkit import datetime


DATA = input('Insira uma data no formato dd/mm/aaaa: ')

try:
    strptime(DATA, '%d/%m/%Y')
    print('Data válida')
except ValueError:
    print('Data inválida.')
