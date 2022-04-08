termo1 = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))
n = 10
termos = termo1
print("Os dez primeiros termos dessa PA são:")
while n > 0:
    print(termos, end=" ")
    termos += razao
    n -= 1
