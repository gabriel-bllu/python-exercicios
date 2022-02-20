import random
import time
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar!!!')
print('-=-' * 20)
num = int(input('Em que número pensei? '))
print('PROCESSANDO...')
time.sleep(2)
numr = random.randint(0, 5)
if num == numr:
    print(f'VOCÊ VENCEU! O número que pensei foi {numr}!')
else:
    print(f'VOCÊ PERDEU! O número que pensei foi {numr}!')
