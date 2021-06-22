from random import choice
s = 0
tu = 0
c = 0
d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Vamos jogar Par ou Impar:')
while c == 0:
    tu += 0
    k = choice(d)
    v = int(input('Digite um numero de 1 a 10: '))
    qu = str(input('Você quer par ou impar: [P/I]')).upper()
    if qu == 'P':
        iu = (k+v) % 2
        s = (k+v)
        if iu == 0:
            print('parabéns você ganhou')
            print(f'eu coloquei {k} e vc {v} total de {s}')
            tu += 1
            print('Vamos jogar novamente...')
        elif iu == 1:
            print('Você errou')
            print(f'eu coloquei {k} e vc {v} total de {s}')
            print(f'você teve um total de {tu} acertos')
            print('GAME OVER!')
            break
    elif qu == 'I':
        iu = (k+v) % 2
        if iu == 0:
            print('Você errou')
            print(f'eu coloquei {k} e vc {v} total de {s}')
            print(f'Você teve um total de {tu} acertos')
            print('GAME OVER!')
            break
        elif iu == 1:
            print('Você acertou')
            print(f'eu coloquei {k} e vc {v} total de {s}')
            tu += 1
            print('Vamos jogar novamente...')