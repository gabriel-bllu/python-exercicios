ficha = []
while True:
    nome = str(input("Nome: ")).capitalize()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input("Quer continuar [S/N]? ")).upper()
    if resp == "N":
        break
print("=-" * 15 + "=")
print(f"{'No.':<4}{'Nome':<10}{'Média':>8}")
print("-" * 28)
for i, a in enumerate(ficha):
    print(f"{i:<4}{a[0]:<10}{a[2]:>8.1f}")
print("-" * 28)
indice = int(input("Mostar notas de qual aluno? (999 interrompe): "))
while indice != 999:
    print(f"Notas de {ficha[indice][0]} são {ficha[indice][1]}")
    indice = int(input("Mostar notas de qual aluno? (999 interrompe): "))
print("Finalizando...")
print("<<< Volte Sempre >>>")