num = int(input('Digite um número: '))
tot = 0
for z in range(1, num + 1):
    if num % z == 0:
        tot += 1
if tot == 2:
    print('Número primo')
else:
    print('Número não primo')