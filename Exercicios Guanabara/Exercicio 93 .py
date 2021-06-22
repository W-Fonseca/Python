jogador = {}
c = []
d = 0
count = 0
z = jogador['Nome'] = str(input('Digite o nome do jogador: '))
a = int(input('Digite o numero de jogos: '))
for k in range(0, a):
    b = int(input(f'Digite o numero de gols no jogo {k}: '))
    c += [b]
    d += b
    jogador['gols'] = c
    jogador['total'] = d
print('=-'*30,end='=')
print('')
print(jogador)
print('=-'*30,end='=')
print('')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('=-'*30,end='=')
print('')
print(f'O Jogador {z} jogou {a} partidas')

for s in c:
    print(f' => Na partida {count}, fez {s} gols')
    count += 1