boletim = {}
boletim['Nome'] = str(input("Digite o nome: ")).capitalize()
boletim['Média'] = float(input(f"Digite a média de {boletim['Nome']}: "))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
else:
    boletim['Situação'] = 'Reprovado'
print('-' * 20)
for k, v in boletim.items():
    print(f" - {k}: {v}")
