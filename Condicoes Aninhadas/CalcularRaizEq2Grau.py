from math import sqrt
print('Dada a equação ax² + bx + c:')
a = float(input('Informe o valor de (a): '))
b = float(input('Informe o valor de (b): '))
c = float(input('Informe o valor de (c): '))
delta = (b**2) - 4 * a * c
if a != 0:
    if delta < 0:
        print(f'Valor de Δ: {delta}\nA equação não tem raízes.')
    elif delta == 0:
        x = (-b) / (2*a)
        print(f'Valor de Δ: {delta}\nA equação tem apenas uma raíz: {x}')
    else:
        x1 = ((-b) + sqrt(delta)) / 2*a
        x2 = ((-b) - sqrt(delta)) / 2*a
        print(f'Valor de Δ: {delta}\nA equação tem duas raízes: {x1} e {x2}')
else:
    print('A equação não é do segundo grau, pois o valor de (a) é igual a zero.')
