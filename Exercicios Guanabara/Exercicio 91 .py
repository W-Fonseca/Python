from random import randint
from time import sleep
print('='*40)
print('Jogo de Dado'.center(40))
print('='*40)
gamer = {}
j1 = 0
j2 = 0
j3 = 0
j4 = 0
gamer['Jogador 1°'] = randint(1,6)
gamer['Jogador 2°'] = randint(1,6)
gamer['Jogador 3°'] = randint(1,6)
gamer['Jogador 4°'] = randint(1,6)
print('Valores Sorteados:')
for h,s in gamer.items():
    sleep(1)
    print(f'O {h} tirou {s}')
sleep(1)
print('='*40)
print('Ranking dos jogadores:')
a = sorted(gamer.values(),reverse=True)
for k in range(0,4):
    if a[k] == gamer['Jogador 1°'] and j1 == 0:
        sleep(1)
        print(f'{k+1}° Lugar: Jogador 1° com {a[k]}')
        j1 =1
    elif a[k] == gamer['Jogador 2°'] and j2 == 0:
        sleep(1)
        print(f'{k+1}° Lugar: Jogador 2° com {a[k]}')
        j2 = 1
    elif a[k] == gamer['Jogador 3°'] and j3 == 0:
        sleep(1)
        print(f'{k+1}° Lugar: Jogador 3° com {a[k]}')
        j3 = 1
    elif a[k] == gamer['Jogador 4°'] and j4 == 0:
        sleep(1)
        print(f'{k+1}° Lugar: Jogador 4° com {a[k]}')
        j4 = 1