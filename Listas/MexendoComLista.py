lista = []
while True:
    num = lista.append(int(input("\nDigite um número: ")))
    while True:
        resp = str(input("Deseja continuar [S/N]? ")).upper()
        if resp == "S" or resp == "N":
            break
    if resp == "N":
        break
print(f"\nTotal de números digitados: {len(lista)}")
lista.sort(reverse=True)
print(f"Lista em ordem decrescente: {lista}")
if lista.count(4) > 0:
    print("O número 4 faz parte da lista.")
else:
    print("O número 4 não faz parte da lista.")