r1 = float(input('Informe o comprimento da primeira reta: '))
r2 = float(input('Informe o comprimento da segunda reta: '))
r3 = float(input('Informe o comprimento da terceira reta: '))
if r1 > r2 - r3 and r1 < r2 + r3 or r2 > r1 - r3 and r2 < r1 + r3:
    print('É possível formar um triângulo.')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('É um triângulo equilátero.')
    elif r1 == r2 and r1 != r3 or r2 == r3 and r2 != r1 or r3 == r1 and r3 != r2:
        print('É um triângulo isósceles.')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('É um triângulo escaleno.')
else:
    print('Não é possível formar um triângulo.')
