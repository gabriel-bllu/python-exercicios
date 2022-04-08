import datetime
ano = int(input('Informe o ano que você nasceu: '))
idade = datetime.date.today().year - ano
if ano <= datetime.date.today().year:
    if idade < 18:
        print(f'Ainda falta {18 - idade} ano(s) para você se alistar.')
    elif idade > 18:
        print(f'Você deveria ter feito o alistamento a {idade - 18} ano(s) atrás.')
    else:
        print('A hora de se alistar é agora!')
else:
    print('Ano de nascimento inválido.')
