pessoa = dict()
lista = []
somaIdade = 0
while True:
    pessoa.clear()
    pessoa["Nome"] = str(input("Nome: "))
    while True:
        pessoa["Sexo"] = str(input("Sexo [M/F]: ")).upper()[0]
        if pessoa["Sexo"] in "MF":
            break
        print("Por favor, digite apenas M ou F.")
    pessoa["Idade"] = int(input("Idade: "))
    somaIdade += pessoa["Idade"]
    lista.append(pessoa.copy())
    resp = str(input("Deseja continuar [S/N]? ")).upper()[0]
    while True:
        if resp in "SN":
            break
    if resp == "N":
        break
print("-"*20)
print(f" - Total de pessoas cadastradas: {len(lista)}")
mediaIdade = somaIdade / len(lista)
print(f" - Média de idade do grupo: {mediaIdade:.2f}")
print(" - As mulheres cadastradas foram:", end=" ")
for p in lista:
    if p["Sexo"] == "F":
        print(f"{p['Nome']}", end=' ')
print()
print(" - Pessoas com idade acima da média:")
for p in lista:
    if p["Idade"] >= mediaIdade:
        for k, v in p.items():
            print(f"{k}: {v}; ", end=" ")
            print()
print("<< ENCERRADO >>")