from math import sin, cos, tan, radians
n1 = int(input('Informe um ângulo: '))
ang = radians(n1)
sen = sin(ang)
cos = cos(ang)
tan = tan(ang)
print('O ângulo {}º tem como seno {:.4f}, cosseno {:.4f} e tangente {:.4f}.'.format(n1, sen, cos, tan))
