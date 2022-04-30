from random import randint
from time import sleep


numeros = []
contador = 1
print("-" * 40)
print("JOGO DA MEGA SENA".center(40))
print("-" * 40)
palpites = int(input("Quantos palpites deseja fazer? "))
print(f"=-=-=-=-= SORTEANDO {palpites} JOGOS =-=-=-=-=")
for p in range(0, palpites):
    while len(numeros) < 6:
        n = randint(1, 60)
        if n not in numeros:
            numeros.append(n)
    numeros.sort()
    print(f"Jogo {contador}: {numeros}")
    numeros.clear()
    contador += 1
    sleep(1.5)
print("=-=-=-=-= < BOA SORTE! > =-=-=-=-=")