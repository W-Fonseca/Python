Nome = str(input('Digite seu nome completo:')).strip()
Nome2 = Nome.split()
Conta = Nome.count(' ')
Nome3 = Nome2[0]
Nome4 = Nome2[Conta]
print('Seu primeiro nome: {}'.format(Nome3))
print('Seu Sobrenome é: {}'.format(Nome4))
