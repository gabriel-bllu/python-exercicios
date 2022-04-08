par = 0
soma = 0
for z in range(1, 7):
    num = int(input('Digite um número: '))
    par = num % 2
    if par == 0:
        soma += num
print(soma)
