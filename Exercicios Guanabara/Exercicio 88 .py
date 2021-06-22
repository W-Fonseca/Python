from random import randint
from time import sleep
print('='*40)
v = 'MEGA SENA - RANDOM'
print(v.center(40))
print('='*40)
d = int(input('me Diga o numero de jogos a ser gerado? '))
for t in range(0,d):
    z = []
    b = 0
    while b < 6:
        a = randint(1,60)
        if a not in z:
            z += [a]
            b += 1
    sleep(1)
    print(f'Jogo {t+1}: {sorted(z)}')