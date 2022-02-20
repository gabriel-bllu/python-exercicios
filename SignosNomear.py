dia = int(input('Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento: '))

if mes == 1 and 21 <= dia <= 31 or mes == 2 and dia <= 18:
    print('Você pertence ao signo de Áquario!')
if mes == 2 and dia >= 19 or mes == 3 and dia <= 20:
    print('Você pertence ao signo de Peixes!')
if mes == 3 and dia >= 21 or mes == 4 and dia <= 20:
    print('Você pertence ao signo de Áries!')
if mes == 4 and dia >= 21 or mes == 5 and dia <= 20:
    print('Você pertence ao signo de Touro!')
if mes == 5 and dia >= 21 or mes == 6 and dia <= 20:
    print('Você pertence ao signo de Gêmeos!')
if mes == 6 and dia >= 21 or mes == 7 and dia <= 22:
    print('Você pertence ao signo de Câncer!')
if mes == 7 and dia >= 23 or mes == 8 and dia <= 22:
    print('Você pertence ao signo de Leão!')
if mes == 8 and dia >= 23 or mes == 9 and dia <= 22:
    print('Você pertende ao signo de Virgem!')
if mes == 9 and dia >= 23 or mes == 10 and dia <= 22:
    print('Você pertence ao signo de Libra!')
if mes == 10 and dia >= 23 or mes == 11 and dia <= 21:
    print('Você pertence ao signo de Escorpião!')
if mes == 11 and dia >= 22 or mes == 12 and dia <= 21:
    print('Você pertence ao signo de Sagitário!')
if mes == 12 and dia >= 22 or mes == 1 and dia <= 20:
    print('Você pertence ao signo de Capricórnio!')
if mes < 1 or mes > 12 or dia < 1 or dia > 31:
    print('Essa data não existe...')