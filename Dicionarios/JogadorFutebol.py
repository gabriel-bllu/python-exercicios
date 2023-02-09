dicto = {
    'Nome': str(input('Nome: '))
}
gols = []
total = 0
qntPartidas = int(input('Quantidades de partidas jogadas: '))
for i in range(0, qntPartidas):
    gols.append(int(input(f'Quantos gols na partida {i + 1}? ')))
    total += gols[i]
dicto['Gols'] = gols
dicto['Total'] = total
print('-=-' * 10)
for k, v in dicto.items():
    print(f'{k}: {v}')
print('-=-' * 10)
print(f'O jogador {dicto["Nome"]} jogou {qntPartidas} partidas.')
for i in range(0, qntPartidas):
    print(f'    => Na partida {i + 1}, fez {dicto["Gols"][i]} gols.')
print(f"Foi um total de {total} gols.\n")
