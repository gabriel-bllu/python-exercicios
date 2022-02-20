speed = int(input('A quantos km/h estava o carro? '))
if speed > 80:
    print(f'Você foi multado! Sua multa vai lhe custar R${(speed - 80) * 7}')
else:
    print('Você dirige dentro da lei!')
