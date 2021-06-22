T = []
p = 1
while p != 0:
    n = str(input('Digite um numero: '))
    if n in T:
        print('esse numero ja foi digitado: ')
    else:
        T += [n]
    s = ' '
    while s not in 'SN':
        s = str(input('deseja continuar [S/N]: ')).upper().strip()[0]
    if s == 'S':
        print('continue')
    elif s == 'N':
        break
print(sorted(T))