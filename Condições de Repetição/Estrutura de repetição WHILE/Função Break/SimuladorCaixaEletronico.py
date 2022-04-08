valor = int(input("Valor a ser sacado: R$"))
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
moedas1 = 0
restante = 0

while restante + 100 <= valor:
    notas100 += 1
    restante += 100
while restante + 50 <= valor:
    notas50 += 1
    restante += 50
while restante + 20 <= valor:
    notas20 += 1
    restante += 20
while restante + 10 <= valor:
    notas10 += 1
    restante += 10
while restante + 5 <= valor:
    notas5 += 1
    restante += 5
while restante + 2 <= valor:
    notas2 += 1
    restante += 2
while restante + 1 <= valor:
    moedas1 += 1
    restante += 1

if notas100 > 0:
    print(f"Notas de R$100: {notas100}")
if notas50 > 0:
    print(f"Notas de R$50: {notas50}")
if notas20 > 0:
    print(f"Notas de R$20: {notas20}")
if notas10 > 0:
    print(f"Notas de R$10: {notas10}")
if notas5 > 0:
    print(f"Notas de R$5: {notas5}")
if notas2 > 0:
    print(f"Notas de R$2: {notas2}")
if moedas1 > 0:
    print(f"Moedas de R$1: {moedas1}")