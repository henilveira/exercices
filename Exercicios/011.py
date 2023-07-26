n = float(input('Largura da parede em metros: '))
a = float(input('Altura da parede em metros: '))
m = n*a
t = m/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m²'.format(n, a, m))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'. format(t))
