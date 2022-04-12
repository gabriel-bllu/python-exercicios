num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite mais um número: "))
num4 = int(input("Digite um último número: "))
tupla = (num1, num2, num3, num4)
if 9 in tupla:
    print(f"\nAparece o número nove {tupla.count(9)} vezes.")
else:
    print(f"\nNão aparece o número '9' nenhuma vez.")
if 3 in tupla:
    print(f"O primeiro '3' aparece na posição {tupla.index(3) + 1}")
else:
    print(f"Não existe '3' na sequência")
print("Os números pares são: ", end='')
for z in range(tupla[0], tupla[3] + 1):
    if z % 2 == 0:
        print(z, end=' ')
