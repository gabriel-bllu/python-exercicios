from operator import itemgetter
from random import randint
from time import sleep


sorteio = {
    'Jogador1': randint(1, 6),
    'Jogador2': randint(1, 6),
    'Jogador3': randint(1, 6),
    'Jogador4': randint(1, 6),
}
print("Valores sorteados:")
sleep(1)
for k, v in sorteio.items():
    print(f"{k} tirou {v} no dado.")
    sleep(1.2)
ranking = dict()
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
print("\n  == Ranking dos jogadores ==")
for i, v in enumerate(ranking):
    print(f"    {i + 1}º lugar: {v[0]} com {v[1]}")
