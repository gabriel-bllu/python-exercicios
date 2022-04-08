num = int(input('Informe um número para saber sua tabuada: '))
i = 0
print('-=-' * 5)
for z in range(1, 11):
    i += 1
    print(f'{num} x {i} = {num * i}')
print('-=-' * 5)