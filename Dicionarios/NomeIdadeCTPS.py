from datetime import date
dataAtual = date.today()
dicto = {
    'Nome': str(input("Nome: ")),
    'Idade': int(input("Ano de Nascimento: ")),
    'CTPS': int(input("Carteira de Trabalho (Digite 0 se não tiver): "))
}
if dicto['CTPS'] != 0:
    dicto['Ano de Contratação'] = int(input("Ano de Contratação: "))
    dicto['Salário'] = float(input("Salário: "))
    dicto['Aposentadoria'] =  (dicto['Ano de Contratação'] + 35) - dicto['Idade']
dicto["Idade"] = dataAtual.year - dicto["Idade"]
print()
for k, v in dicto.items():
    print(f'{k}: {v}')
