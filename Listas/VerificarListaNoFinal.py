lista = []
listaPar = []
listaImpar = []
while True:
    num = int(input("\nDigite um valor: "))
    lista.append(num)
    while True:
        resp = str(input("Deseja continuar [S/N]? ")).upper()
        if resp == "S" or resp == "N":
            break
    if resp == "N":
        break
pos = 0
while pos < len(lista):
    if lista[pos] % 2 == 0:
        listaPar.append(lista[pos])
    if lista[pos] % 2 != 0:
        listaImpar.append(lista[pos])
    pos += 1
lista.sort()
listaPar.sort()
listaImpar.sort()
print(f"\nLista com todos os números: {lista}")
print(f"Lista com números Pares: {listaPar}")
print(f"Lista com números Ímpares: {listaImpar}\n")
