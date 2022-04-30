lista = []
while True:
    num = int(input("Digite um número: "))
    if num not in lista:
        print("Número adicionado com sucesso!")
        lista.append(num)
    else:
        print("Número já adicionado...")
    resp = str(input("Quer continuar [S/N]: ")).upper()
    if resp == "N":
        break
lista.sort()
print(f"Números em ordem crescente: {lista}")
