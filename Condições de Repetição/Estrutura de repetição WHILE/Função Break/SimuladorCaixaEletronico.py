valor = int(input("Valor a ser sacado: R$"))
notas50 = 0
reais50 = 0
notas20 = 0
notas10 = 0
notas1 = 0
restante = 0

while restante + 50 <= valor:
    notas50 += 1
    restante += 50
while restante + 20 <= valor:
    notas20 += 1
    restante += 20
while restante + 10 <= valor:
    notas10 += 1
    restante += 10
while restante + 1 <= valor:
    notas1 += 1
    restante += 1
 
print(f"Notas de 50: {notas50}")
print(f"Notas de 20: {notas20}")
print(f"Notas de 10: {notas10}")
print(f"Notas de 1: {notas1}")