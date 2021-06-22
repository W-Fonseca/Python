qi = []
z = []
x = 0
w = 0
l = []
while w == 0:
    a = str(input('Nome: '))
    b = float(input('Peso: '))
    z += [a,b]
    qi += [b]
    l.append(z[:])
    z.clear()
    x += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Deseja cadastrar mais alguem? [S/N]')).upper()
        if c == 'S':
            'OK'
        elif c == 'N':
            w = 1
p1 = max(qi)
p2 = min(qi)
print(f'total de pessoas cadastradas são: {x}')
print('As pessoas mais pesadas são: ',end='')
for o in l:
    if o[1] == p1:
        print(f'{o[0]}',end=', ')
print('')
print('')
print(f'as pessoas mais leves são: ',end='')
for v in l :
    if v[1] == p2:
        print(f'{v[0]}',end=', ')