def ficha(jogador, gols=0):
    if len(jogador) == 0:
        jogador = "<desconhecido>"
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f"O jogador {jogador} fez {gols} gol(s) no campeonato."

print(ficha(input("Nome do jogador: "), input("Número de gols: ")))
