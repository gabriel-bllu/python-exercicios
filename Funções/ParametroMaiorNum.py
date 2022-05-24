from time import sleep


def maior(*valor):
    lista = []
    tam = len(valor)
    print("-=" * 25)
    print("Analisando os valores passados...")
    sleep(1)
    for num in valor:
        lista.append(num)
        print(f"{num}", end=" ", flush=True)
        sleep(0.5)
    print(f"Foram informados {tam} valores ao todo.")
    lista.sort()
    if len(lista) == 0:
        print(f"O maior valor informado foi 0.")
    else:
        print(f"O maior valor informado foi {lista[-1]}")
    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
 
  