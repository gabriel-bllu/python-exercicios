maça_peso = float(input('Quantidade de maçãs (em kg): '))
morango_peso = float(input('Quantidade de morango (em kg): '))
kg_total = maça_peso + morango_peso

if morango_peso <= 5 and maça_peso <= 5:
    preço_morango = morango_peso * 2.5
    preço_maça = maça_peso * 1.8
    valor_total = preço_maça + preço_morango
    if kg_total > 8 or valor_total > 25:
        print(f'Valor total com 10% de desconto: R${valor_total - ((valor_total * 10) / 100):.2f}')
    else:
        print(f'Valor total sem desconto: R${valor_total:.2f}')

elif morango_peso <= 5 and maça_peso > 5:
    preço_morango = morango_peso * 2.5
    preço_maça = maça_peso * 1.5
    valor_total = preço_maça + preço_morango
    if kg_total > 8 or valor_total > 25:
        print(f'Valor total com 10% de desconto: R${valor_total - ((valor_total * 10) / 100):.2f}')
    else:
        print(f'Valor total sem desconto: R${valor_total:.2f}')

elif morango_peso > 5 and maça_peso <= 5:
    preço_morango = morango_peso * 2.2
    preço_maça = maça_peso * 1.8
    valor_total = preço_maça + preço_morango
    if kg_total > 8 or valor_total > 25:
        print(f'Valor total com 10% de desconto: R${valor_total - ((valor_total * 10) / 100):.2f}')
    else:
        print(f'Valor total sem desconto: R${valor_total:.2f}')

else:
    preço_morango = morango_peso * 2.2
    preço_maça = maça_peso * 1.5
    valor_total = preço_maça + preço_morango
    if kg_total > 8 or valor_total > 25:
        print(f'Valor total com 10% de desconto: R${valor_total - ((valor_total * 10) / 100):.2f}')
    else:
        print(f'Valor total sem desconto: R${valor_total:.2f}')
