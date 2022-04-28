lista = []
listaPar = []
listaImpar = []
while True:
    num = int(input("\nDigite um valor: "))
    lista.append(num)
    if num % 2 == 0:
        listaPar.append(num)
    else:
        listaImpar.append(num)
    while True:
        resp = str(input("Deseja continuar [S/N]? ")).upper()
        if resp == "S" or resp == "N":
            break
    if resp == "N":
        break
print(f"\nLista com todos os números: {lista}")
print(f"Lista com números Pares: {listaPar}")
print(f"Lista com números Ímpares: {listaImpar}\n")
