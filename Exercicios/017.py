import math
co = float(input('Insira o comprimento do cateto oposto: '))
ca = float(input('Insira o comprimento do cateto adjacente: '))
h = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(h))