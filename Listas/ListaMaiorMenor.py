lista = []
maior = 0
menor = 0
for i in range(0, 5):
    num = lista.append(int(input("Digite um número: ")))
    if i == 0:
        maior = menor = lista[i]
    else:
        if lista[i] > maior:
            maior = lista[i]
        if lista[i] < menor:
            menor = lista[i]
print(lista)
print(f"Maior número: {maior}\nMenor número: {menor}")
print(f"O maior número está na posição {lista.index(maior) + 1} e o menor número está na posição {lista.index(menor) + 1}")
