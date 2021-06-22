print('vamos pintar')

alt = float(input('qual altura da parede: '))
larg = float(input('qual a largura da parede: '))

soma = float(alt * larg)
litro = float(soma / 2)
print('voce tem {} metros quadrados e ira usar {} litros'.format(soma,litro))