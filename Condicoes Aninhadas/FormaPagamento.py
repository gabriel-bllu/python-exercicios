valor_produto = float(input('Informe o valor de um produto: R$'))
print('Digite 1 para pagamento à vista com dinheiro ou cheque. (10% de desconto)')
print('Digite 2 para pagamento à vista no cartão. (5% de desconto)')
print('Digite 3 para parcelar em até 2x no cartão.')
print('Digite 4 para parcelar em 3x ou mais no cartão. (20% de juros)')
forma_pagamento = int(input('Como você gostaria de pagar o produto? '))

if forma_pagamento == 1:
    print(f'O preço do produto à vista em dinheiro ou cheque é R${valor_produto - ((valor_produto * 10) / 100):.2f}')
elif forma_pagamento == 2:
    print(f'O preço do produto à vista no cartão é R${valor_produto - ((valor_produto * 5) / 100):.2f}')
elif forma_pagamento == 3:
    print(f'O preço do produto é em até 2x no cartão é R${valor_produto:.2f}')
elif forma_pagamento == 4:
    print(f'O preço do produto em 3x ou mais no cartão é R${valor_produto + ((valor_produto * 20) / 100):.2f}')
else:
    print('Forma de pagamento inválida.')
