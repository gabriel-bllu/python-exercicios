from math import hypot
cato = float(input('Insira a altura do triângulo retângulo: '))
cata = float(input('Insira a largura do triângulo retângulo: '))
h = hypot(cato, cata)
print('O valor do comprimento da hipotenusa é {:.2f}'.format(h))
