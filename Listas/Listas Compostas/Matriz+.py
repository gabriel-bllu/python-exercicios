matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somaTerceiraColuna = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]: "))
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            somaTerceiraColuna += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        if matriz[1][c] > maior:
            maior = matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()
print(f"Soma dos números pares: {soma}")
print(f"Soma dos valores na terceira coluna: {somaTerceiraColuna}")
print(f"Maior número da segunda linha: {maior}")