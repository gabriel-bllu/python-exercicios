import random
print("-=-" * 7)
print(" JOGO DA ADIVINHAÇÃO")
print("-=-" * 7, '\n')
print("Tente adivinhar o número exato que o computador vai pensar!\n")

usuario = int(input("Digite um número de 0 a 10: "))
print()
pc = random.randint(0, 10)
palpites = 1
while usuario != pc:
    print("Você errooou!")
    if usuario > pc:
        print("Menos... Tente mais uma vez.")
        usuario = int(input('Tente novamente: '))
    elif usuario < pc:
        print("Mais... Tente mais uma vez.")
        usuario = int(input('Tente novamente: '))
    palpites += 1
print()
print(f'Você acertooooou! E em apenas {palpites} palpite(s).')
print(f'O computador pensou em {pc}\nPARABÉNS!!!')
