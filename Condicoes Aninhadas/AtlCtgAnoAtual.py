import datetime
ano = int(input('Digite o ano do seu nascimento: '))
idade = datetime.date.today().year - ano
if ano <= datetime.date.today().year:
    if idade <= 9:
        print('Categoria Mirim!')
    elif idade > 9 and idade <= 14:
        print('Categoria Infantil!')
    elif idade > 14 and idade <= 19:
        print('Categoria Junior!')
    elif idade == 20:
        print('Categoria Sênior!')
    else:
        print('Categoria Master!')
else:
    print('Data de nascimento inválida!')
