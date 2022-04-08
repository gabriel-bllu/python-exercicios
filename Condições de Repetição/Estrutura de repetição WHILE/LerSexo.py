sexo = input('Informe seu sexo [M/F]: ').upper()
while sexo != 'F' and sexo != 'M':
    print()
    print('Sexó inválido')
    sexo = input('Informe seu sexo [M/F]: ').upper()
if sexo == 'F':
    print('Sexo Feminino.')
elif sexo == 'M':
    print('Sexo Masculino.')
