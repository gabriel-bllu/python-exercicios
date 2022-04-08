peso = float(input('Informe seu peso (em Kg): '))
altura = float(input('Digite sua altura (em M): '))
imc = peso / (altura**2)
print(f'O resultado do seu IMC deu {imc:.2f}kg/m2')
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você se encontra na categoria "Sobrepeso".')
elif imc >= 30 and imc < 40:
    print('Você está na categoria "Obesidade"')
else:
    print('Você tem Obesidade mórbida.')
