num = int(input('Digite um valor: '))
c = num
f = 1
while c > 0:
    f *= c
    c -= 1
print(f"{num}! = {f}")
