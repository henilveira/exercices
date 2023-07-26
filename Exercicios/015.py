n1 = float(input('Quantos dias alugados? '))
n2 = float(input('Quantos Km rodados? '))
d = n2 * 0.15
km = n1 * 60
p = d + km
print('O total a pagar é de R${:.1f}'.format(p))

