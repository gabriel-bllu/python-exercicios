import random
tupla = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f"Lista dos números: {tupla}")
tupla = sorted(tupla)
print(f"Maior número: {tupla[-1]}")
print(f"Menor número: {tupla[0]}")