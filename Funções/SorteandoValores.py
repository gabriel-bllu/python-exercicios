from random import randint
from time import sleep


def sorteia(lista):
    print("Sorteando 5 valores: ", end="")
    for i in range(5):
        lista.append(randint(0, 10))
        print(f"{lista[i]}", end=" ", flush=True)
        sleep(0.5)
    print('Pronto!')


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f"Somando os valores pares de {lista}, temos {soma}")

numeros = []
sorteia(numeros)
somaPar(numeros)