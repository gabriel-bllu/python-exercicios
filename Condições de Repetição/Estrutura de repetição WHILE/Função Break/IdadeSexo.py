a = 0
b = 0
c = 0
while True:
    idade = input("Informe sua Idade: ")
    while not idade.isnumeric() or int(idade) < 0:
        idade = input("Informe sua Idade: ")
    idade = int(idade)
    sexo = str(input("Informe seu Sexo [M/F]: ")).upper()
    while sexo != "M" and sexo != "F":
        sexo = str(input("Informe seu Sexo [M/F]: ")).upper()
    if idade > 18:
        a += 1
    if sexo == "M":
        b += 1
    if idade < 20 and sexo == "F":
        c += 1
    resposta = str(input("Deseja continuar [S/N]: ")).upper()
    while resposta != "S" and resposta != "N":
        resposta = str(input("Deseja continuar [S/N]: ")).upper()
    if resposta == "N":
        break
print(f"Pessoas com mais de 18 anos: {a}")
print(f"Total de homens cadastrados: {b}")
print(f"Total de mulheres com menos de 20 anos: {c}")