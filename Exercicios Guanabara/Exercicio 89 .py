x = 0
q = 0
l = [[],[],[]]
while x == 0:
    z = ' '
    while z not in 'SN':
        z = str(input('deseja adicionar um aluno: [S/N]')).upper()
        if z == 'S':
            q += 1
            a = str(input('nome: '))
            b = float(input('primeira nota: '))
            c = float(input('Segunda nota: '))
            l[0] += [a]
            l[1] += [b]
            l[2] += [c]
        elif z == 'N':
            x = 1
print('='*40)
lu = 'NOTAS DA SALA DE AULA'
print(lu.center(40))
print('='*40)
for f in range(0,q):
    h = l[1][f]+l[2][f] / 2
    print(f'Cod.Aluno: {f} | Nome: {l[0][f]} | média: {h}')
    print('_' * 40)
while True:
    z = int(input('Digite o Cod.Aluno para mostrar a nota: (Obs.: Digite 999 para sair)'))
    if z != 999:
        print(f'as notas de {l[0][z]} São {l[1][z]} e {l[2][z]}')
    elif z == 999:
        break