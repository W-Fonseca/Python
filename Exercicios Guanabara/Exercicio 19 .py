import random
a = input('me diz o nome do primeiro aluno: ')
b = input('nome do segundo aluno: ')
c = input('terceiro nome: ')
d = input('quarto nome: ')
e = input('primeiro menino: ')
f = input('segundo menino: ')
g = input('terceiro menino: ')
h = input(' quarto menino: ')
nomes = [a,b,c,d,e,f,g,h]
calculo2 = random.choice(nomes)
print('vou escolher um nome:  {}'.format(calculo2))