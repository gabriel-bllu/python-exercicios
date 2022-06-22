from time import sleep


while True:
    txt = "Sistema de Ajuda PyHelp"
    print("~" * (len(txt) + 4))
    print(txt.center(len(txt) + 4))
    print("~" * (len(txt) + 4))
    comando = input("Função ou Biblioteca > ")
    if comando == "fim":
        break
    txt = (f"Acessando o manual do comando {comando}")
    print("~" * (len(txt) + 4))
    print(txt.center(len(txt) + 4))
    print("~" * (len(txt) + 4))
    sleep(2)
    print(help(comando))