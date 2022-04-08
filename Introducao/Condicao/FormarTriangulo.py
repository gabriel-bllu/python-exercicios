r1 = int(input('Informe o comprimento da primeira reta: '))
r2 = int(input('Informe o comprimento da segunda reta: '))
r3 = int(input('Informe o comprimento da terceira reta: '))
if r1 > r2 - r3 and r1 < r2 + r3:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')
