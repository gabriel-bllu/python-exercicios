valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Informe seu salário: R$'))
anos = int(input(f'Em quantos anos deseja pagar a casa? '))

prestacao_mensal = valor_casa / (anos * 12)

if round(prestacao_mensal) > (salario * 30) / 100:
    print()
    print('Emprestimo negado.')
    print(f'A prestação mensal é R${prestacao_mensal:.2f} e excede o limite de 30% do seu salário, que seria R${(salario * 30) / 100:.2f} de um total de R${salario:.2f}')
else:
    print('Você está apto para comprar esta casa. Parabéns!')
    print(f'A prestação mensal é de R${prestacao_mensal:.2f}, e está dentro da margem dos 30% do seu salário!')
