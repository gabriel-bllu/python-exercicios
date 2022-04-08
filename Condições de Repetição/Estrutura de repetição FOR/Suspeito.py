perg1 = input('Telefonou para a vítima? ').strip()
perg2 = input('Esteve no local do crime? ').strip()
perg3 = input('Mora perto da vitima? ').strip()
perg4 = input('Devia para a vítima? ').strip()
perg5 = input('Já trabalhou com a vítima? ').strip()
x = 0
veredito = [perg1, perg2, perg3, perg4, perg5]

for z in range(len(veredito)):
    if veredito[z].upper() == 'SIM':
        x += 1
if x == 2:
    print('Suspeito')
elif 3 <= x <= 4:
    print('Cúmplice')
elif x == 5:
    print('Assassino')
else:
    print('Inocente')
