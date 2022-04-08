termo1 = int(input("Informe o primeiro termo da PA: "))
razao = int(input("Informe a razão da PA: "))
n = 10
termos = termo1
print("Os dez primeiros termos dessa PA são:")
while n > 0:
    print(termos, end=" ")
    termos += razao
    n -= 1
resp = input("\nDeseja vez mais termos dessa PA? [S/N] ").upper()
while resp == "S":
    termos = termo1
    if resp == "S":
        qnttermos = int(input("Quantos termos deseja ver agr? "))
    while qnttermos > 0:
        print(termos, end=" ")
        termos += razao
        qnttermos -= 1
    resp = input("\nDeseja vez mais termos dessa PA? [S/N] ").upper()
print("Tenha um bom dia!")
