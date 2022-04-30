temporario = []
principal = []
maior = menor = 0
pesadas = []
leves = []
while True:
    temporario.append(str(input("Nome: ")).capitalize())
    temporario.append(float(input("Peso: ")))
    if len(principal) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor: 
            menor = temporario[1]
    principal.append(temporario[:])
    temporario.clear()
    resp = input("Quer continuar [S/N]: ").upper()
    while resp != "S" and resp != "N":
        resp = input("Quer continuar [S/N]: ").upper()
    if resp == "N":
        break
for p in principal:
    if p[1] == maior:
        pesadas.append(p[0])
    if p[1] == menor:
        leves.append(p[0])
print(f"Foram cadastradas {len(principal)}")
print(f"Pessoas mais pesadas: {pesadas}. {maior} Kg")
print(f"Pessoas mais leves: {leves}. {menor} Kg")
