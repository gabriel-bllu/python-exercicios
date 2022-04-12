tupla = ("parada", "flutuador", "travesseiro", "aroma", "sangrar", "segundos", "eleito", "roxo", "gala", "gado")
for p in tupla:
    print(f"\nNa palavra {p.upper()} temos: ", end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
