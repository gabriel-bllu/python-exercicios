from calendar import isleap
from datetime import date
ano = int(input('Qual ano deseja analisar? Coloque 0 para o ano atual: '))
if ano == 0:
    if isleap(date.today().year):
        print(f'O ano {date.today().year} é bissexto.')
    else:
        print(f'O ano {date.today().year} não é bissexto.')
else:
    if isleap(ano):
        print(f'O ano {ano} é bissexto.')
    else:
        print(f'O ano {ano} não é bissexto.')
