num = int(input('Digite um número inteiro qualquer: '))
print('1 para Binário\n2 para Octal\n3 para Hexadecimal')
usuario_escolha = int(input('Escolha a base de conversão: '))

if usuario_escolha == 1:
    print(f'O número {num} em binário é {bin(num)}')
elif usuario_escolha == 2:
    print(f'O número {num} em octal é {oct(num)}')
elif usuario_escolha == 3:
    print(f'O número {num} em hexadecimal é {hex(num)}')
else:
    print('Escolha inválida.')
