temp = {}
jogadores = []
gols = []
total = 0
while True:
    temp["Nome"] = str(input("Nome: "))
    partidas = int(input(f"Quantas partidas {temp['Nome']} jogou? "))
    for i in range(partidas):
        gols.append(int(input(f"Quantidade de gols na partida {i + 1}: ")))
        total += gols[i]
    temp["Gols"] = gols[:]
    temp["Total"] = total
    jogadores.append(temp.copy())
    temp.clear()
    gols.clear()
    total = 0
    while True:
        r = str(input("Deseja continuar [S/N]? ")).upper()[0]
        if r in "SN":
            break
    if r == "N":
        break
print("=" * 38)
print(f"{'cod'}{'nome':>5}{'gols':>15}{'total':>15}")
print("-"*38)
for k, v in enumerate(jogadores):
    print(f"{k:>3} ", end="")
    for d in v.values():
        print(f"{str(d):<15}", end="")
    print()
print('-'*38)
while True:
    busca = int(input("Mostrar dados de qual jogador? (999 para parar) "))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f"Erro! Não existe jogador com código {busca}")
    else:
        print(f' -- Levantamento do Jogador {jogadores[busca]["Nome"]}')
        for i, g in enumerate(jogadores[busca]["Gols"]):
            print(f"    No jogo {i+1} fez {g} gols.")
    print("-" * 30)
