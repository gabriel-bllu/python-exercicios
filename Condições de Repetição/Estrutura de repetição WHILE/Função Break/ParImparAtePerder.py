from random import randint

print("\n[Brincadeira de Par ou Ímpar]\n")

numUsuario = int(input("Escolha um número: "))
escUsuario = input("Par ou Ímpar [P/I]: ")
pc = randint(0, 10)
resultado = numUsuario + pc
contador = 0

while True:
    resultado = numUsuario + pc
    if resultado % 2 == 0:

        if escUsuario == "P":
            print(f"\nVencedor!\nSua escolha: {numUsuario}\nEscolha do pc: {pc}\n{numUsuario} + {pc} = {numUsuario + pc}")
            contador += 1

        elif escUsuario == "I":
            break

    elif resultado % 2 != 0:

        if escUsuario == "P":
            break

        elif escUsuario == "I":
            print(f"\nVencedor!\nSua escolha: {numUsuario}\nEscolha do pc: {pc}\n{numUsuario} + {pc} = {numUsuario + pc}")
            contador += 1

    numUsuario = int(input("\nEscolha um número: "))
    escUsuario = input("Par ou Ímpar [P/I]: ")
    pc = randint(0, 10)

print(f"\nVocê perdeu...\nSua escolha: {numUsuario}\nEscolha do pc: {pc}\n{numUsuario} + {pc} = {numUsuario + pc}")
print(f"Total de Vitórias: {contador}")