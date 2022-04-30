valores = []
par = []
impar = []
valores.append(par)
valores.append(impar)
for i in range(0, 7):
    num = int(input(f"Digite o {i + 1}o° valor: "))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort()
impar.sort()
print(f"Números pares: {valores[0]}")
print(f"Número ímpares: {valores[1]}")