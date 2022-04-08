somaTotal = 0
b = 0
precoMaisBarato = 999999999
print("-" * 50)
print("LOJA PAGUE E LEVE".center(50))
print("-" * 50)
while True:
    nome = str(input("Nome do Produto: ")).capitalize()
    preco = float(input("Valor: "))
    somaTotal += preco
    if preco > 1000:
        b += 1
    if preco < precoMaisBarato:
        precoMaisBarato = preco
        produtoMaisBarato = nome
    resposta = input("Deseja continuar [S/N]? ").upper()
    while resposta != "S" and resposta != "N":
        resposta = input("Deseja continuar [S/N]? ").upper()
    if resposta == "N":
        break
print("----------  FIM DO PROGRAMA  ----------")
print(f"Total gasto: R${somaTotal:.2f}")
print(f"Qnt de produtos que custam mais de R$1000: {b}")
print(f"Produto mais barato: {produtoMaisBarato}")