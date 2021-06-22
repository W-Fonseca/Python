import uteis
p = float(input('digite o preço: R$ '))
print(f'metade de R$ {uteis.formatado(p)} é R$ {uteis.formatado(uteis.metade(p))}')
print(f'O dobro de R$ {p} é R$ {uteis.formatado(uteis.dobro(p))}')
print(f'aumento de 10%, temos R$ {uteis.formatado(uteis.maisdezporcento(p,10))}')
print(f'Reduzindo 13%, temos R$ {uteis.formatado(uteis.menostrezeporcento(p,13))}')
