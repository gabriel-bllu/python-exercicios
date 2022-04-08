num = 0
contador = 0
decisao = "S"
soma = 0
ordem = []
while decisao == "S":
    num = int(input("Digite um número: "))
    soma += num
    contador += 1
    ordem.append(num)
    decisao = str(input("Deseja continuar? [S/N] ")).upper()
media = soma / contador
ordem.sort()
print(f"Menor número digitado: {ordem[0]}\nMaior número digitado: {ordem[-1]}")
print(f"Média dos números digitados: {soma} / {contador} = {media}")
