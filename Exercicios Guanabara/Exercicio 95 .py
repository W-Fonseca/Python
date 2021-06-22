jogador = {}
time = []
c = 0
w = []
q = 0
while c == 0:
    s =' '
    while s not in 'SN':
        s = str(input('Deseja cadastrar um jogador [S/N]: ')).upper()
        if s == 'N':
            c = 1
        elif s == 'S':
            q += 1
            print('='*40)
            a = jogador['Nome'] = str(input('nome: '))
            b = jogador['jogos'] = int(input(f'Quantas partidas {a} jogou? '))
            for k in range(0,b):
               d = int(input(f'Quantos gols na partida {k}: '))
               w += [d]
            jogador['gols'] = w[:]
            jogador['total'] = sum(jogador['gols'])
            time.append(jogador.copy())
            w.clear()
print('=-'*40)
print('cod ',end='')
for g in jogador.keys():
    print(f'{g:<15}',end='')
print()
print('-'*40)
for p, o in enumerate(time):
    print(f'{p:>3} ',end='')
    for j in o.values():
        print(f'{str(j):<15}',end='')
    print()
print('-'*40)
while True:
    print('-'*40)
    y = int(input('qual jogador você deseja mostrar? [digite o numero do cod]'))
    if 0 <= y <= q:
        print(f'LEVANTAMENTO DO JOGADOR: ', time[y]['Nome'])
        for x,z in enumerate(time[y]['gols']):
            print(f'no jogo {x} fez {z} gols')
    elif y == 999:
        print('<<Foi um prazer>>')
        print('<<encerrando processamento>>')
        break
    else:
        print(f'ERRO! Não existe jogador com o codigo {y}')