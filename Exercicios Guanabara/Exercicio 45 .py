from random import choice
print('vamos jogar jokenpo')
print('aperte "a" para Pedra')
print('aperte "b" para Papel')
print('aperte "c" para tesoura')
v = str(input('insira o valor: '))
xi = ['a', 'b', 'c']
p = choice(xi)
print('eu coloquei {}'.format(p))
result = str(v+p)

if result == 'cb' or result == 'ba' or result == 'ac':
    print('Voce Ganhou')

elif result == 'aa' or result =='bb' or result == 'cc':
    print('deu empate')

elif result == 'bc' or result =='ab' or result =='ca':
    print('Eu ganhei')