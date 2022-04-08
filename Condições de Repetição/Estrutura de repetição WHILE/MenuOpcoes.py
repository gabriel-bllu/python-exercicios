from time import sleep

num1 = float(input("Valor 1: "))
num2 = float(input("Valor 2: "))
escolha = 0
while escolha != 5:
    print("\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n")
    escolha = int(input("\nInforme o que deseja fazer: "))
    while escolha == 4:
        print("Novos valores.")
        num1 = float(input("Valor 1: "))
        num2 = float(input("Valor 2: "))
        print("\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos números\n[5] Sair do programa\n")
        escolha = int(input("\nInforme o que deseja fazer: "))
    if escolha == 1:
        print("\nSOMA")
        print(f"{num1} + {num2} = {num1 + num2}")
    elif escolha == 2:
        print("\nMULTIPLICAÇÃO")
        print(f"{num1} x {num2} = {num1 * num2}")
    elif escolha == 3:
        if num1 > num2:
            print(f"O maior dentre os números informados é {num1}")
        elif num2 > num1:
            print(f"O maior dentre os números informados é {num2}")
        else:
            print(f"Os dois número são iguais. {num1} = {num2}")
    if escolha > 5 or escolha <= 0:
        print("Opção inválida.")
        sleep(1)
print("Tenha um bom dia!\nAté mais!")
