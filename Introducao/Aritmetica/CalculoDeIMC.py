peso = float(input('Informe seu peso em kilogramas: '))
alt = float(input('Informe sua altura em metros: '))
imc = peso / (alt**2)
print('Seu IMC tem como resultado: {:.2f}.'.format(imc))
