import math
ang = float(input('Digite o ângulo odesejado: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f} \nO ângulo de {} tem o COSSENO de {:.2f} \nO ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, sen, ang, cos, ang, tan))
