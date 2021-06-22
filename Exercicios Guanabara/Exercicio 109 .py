import uteis2
p = float(input('digite o preço: R$ '))
print(f'metade de R$ {uteis2.formatado(p)} é R$ {uteis2.metade(p,True)}')
print(f'O dobro de R$ {uteis2.formatado(p)} é R$ {uteis2.dobro(p,True)}')
print(f'aumento de 10%, temos R$ {uteis2.maisdezporcento(p,10,True)}')
print(f'Reduzindo 13%, temos R$ {uteis2.menostrezeporcento(p,13,True)}')