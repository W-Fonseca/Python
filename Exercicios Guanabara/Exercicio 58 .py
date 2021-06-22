from random import choice
c=0
B = 0
while c == 0:
    B += 1
    P = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Q = choice(P)
    k = int(input('Digite um numero de 1 a 10, vamos ver se você acerta: '))
    if Q == k:
        print("""Parabens, Você acertou! Meu numero foi {} e o seu {}
Numero de tentativas foi {}""".format(Q,k,B))
        c = 1
    else:
        print('Você errou: eu escolhi {} e Você {}'.format(Q, k))
