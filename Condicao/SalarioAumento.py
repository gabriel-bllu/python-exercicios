sal = float(input('Informe o valor do seu salário: R$'))
if sal > 1250:
    print(f'Salário com aumento de 10%: R${sal + ((sal * 10) / 100)}')
else:
    print(f'Seu salário com aumento de 15%: R${sal + ((sal * 15) / 100)}')
