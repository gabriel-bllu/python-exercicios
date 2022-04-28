expressao = str(input("Digite uma expressão: "))
lst = []
erro = 0
parentenseAberto = 0
parentenseFechado = 0
pos = 0
while True:
    for i in expressao:
        lst.append(i)
        if lst.count("(") == 0 and lst.count(")") == 1:
            erro += 1
            break
    if erro > 0:
        break
    if lst.count("(") != lst.count(")"):
        erro += 1
        break
    while pos < len(lst):
        if lst[pos] == "(":
            parentenseAberto += 1
        if lst[pos] == ")":
            parentenseFechado += 1
        if parentenseAberto < parentenseFechado:
            erro += 1
            break
        pos += 1
    break
if erro > 0 :
    print("Sua expressão está errada!")
else:
    print("Sua expressão é válida!")