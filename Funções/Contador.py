from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print("=-=" * 12)
    print(F"Contagem de {inicio} até {fim} de {passo} em {passo}")
    sleep(2)
    if inicio > fim:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=" ", flush=True)
            sleep(0.5)
        print("FIM!")
    else:
        for i in range(inicio, fim + 1, passo):
            print(i, end=" ", flush=True)
            sleep(0.5)
        print("FIM!")

contador(1, 10, -1)
contador(10, 0, 2)
print("=-=" * 12)
print("Agora é sua vez de personalizar a contagem!")
contador(int(input("Início: ")), int(input("Fim: ")), int(input("Passo: ")))