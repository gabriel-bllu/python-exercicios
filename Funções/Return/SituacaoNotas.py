def notas(*n, situacao = False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param situacao: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    dicto = {}
    dicto["Quantidade de Alunos"] = len(n)
    dicto["Maior Nota"] = max(n)
    dicto["Menor Nota"] = min(n)
    dicto["Média"] = sum(n)/len(n)
    if situacao:
        if dicto["Média"] >= 7:
            dicto["Situação"] = "Boa"
        elif dicto["Média"] < 6:
            dicto["Situação"] = "Ruim"
        else:
            dicto["Situação"] = "Razoável"
    return dicto

print(notas(6, 8, 5.4, 10, situacao=True))
help(notas)