def jogador(nome = '',gols = 0):
    if nome == '':
        nome = '<Desconhecido>'

    print(f'o jogador {nome} fez {gols} gols')


s = str(input('Digite o nome d jogador: '))
f = str(input('digite o numero de gols do jogador: '))
if f.isnumeric():
    f = int(f)
else:
    f = 0
jogador(s,f)