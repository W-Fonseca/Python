import random
n = int(input('me diz um numero de 0 a 5, vamos ver se vc acerta: '))
lista = 0, 1, 2, 3, 4, 5
escolha = random.choice(lista)
if escolha == n:
    print('parabens você acertou!')
    print('Numero que eu escolhi foi {} e o seu {}'.format(escolha,n))
else:
    print('Desculpas mas você errou!')
    print('Seu numero foi {} e o meu {}'.format(n,escolha))