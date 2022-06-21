def vota(anoDeNascimento):
    from datetime import date

    anoAtual = date.today().year
    idade = anoAtual - anoDeNascimento

    if idade < 16:
        return f"Com {idade} anos: NÃO VOTA."
    elif 16 <= idade < 18 or idade > 65:
        return f"Com {idade} anos: VOTO OPCIONAL."
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO."

print(vota(int(input("Em que ano você nasceu? "))))
