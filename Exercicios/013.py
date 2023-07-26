n = float(input('Qual é o salário do Funcionário? R$'))
d = n+(n*0.15)
print('Um funcionário que ganhavaR${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(n, d))