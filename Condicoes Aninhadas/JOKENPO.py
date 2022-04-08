import random
from time import sleep
print('-=-' * 20)
print('Jogo de Pedra, Papel ou Tesoura')
print('-=-' * 20)
print()
print('Escolha pedra, papel ou tesoura!')
player = str(input()).upper().strip()
lista = ['Pedra', 'Papel', 'Tesoura']
pc = random.choice(lista)
print()
if player == 'PEDRA':
    if pc == 'Pedra':
        print(pc)
        sleep(1.5)
        print()
        print('DEU EMPATE!')
    elif pc == 'Papel':
        print(pc)
        sleep(1.5)
        print()
        print('EU GANHEI! Papel embrulha Pedra!')
    elif pc == 'Tesoura':
        print(pc)
        sleep(1.5)
        print()
        print('VOCÊ GANHOU! Pedra esmaga Tesoura!')
elif player == 'PAPEL':
    if pc == 'Pedra':
        print(pc)
        sleep(1.5)
        print()
        print('VOCÊ GANHOU! Papel embrulha pedra!')
    elif pc == 'Papel':
        print(pc)
        sleep(1.5)
        print()
        print('DEU EMPATE!')
    elif pc == 'Tesoura':
        print(pc)
        sleep(1.5)
        print()
        print('EU GANHEI! Tesoura corta papel!')
elif player == 'TESOURA':
    if pc == 'Pedra':
        print(pc)
        sleep(1.5)
        print()
        print('EU GANHEI! Pedra esmaga tesoura!')
    elif pc == 'Papel':
        print(pc)
        sleep(1.5)
        print()
        print('VOCÊ GANHOU! Tesoura corta papel!')
    elif pc == 'Tesoura':
        print(pc)
        sleep(1.5)
        print()
        print('DEU EMPATE')
else:
    print('Escolha inválida.')
