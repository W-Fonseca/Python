j = 0
k = 1
c = 0
while c == 0:
    k = int(input('Gostaria de ver a tabuada de qual Valor? '))
    u = 'Gerador de tabuada'
    print('='*30)
    print(u.center(30))
    print('='*30)
    while k >= 1:
        j += 1
        b = j*k
        print(f'{k} X {j} = {b}')
        if j == 10:
            j = 0
            print('='*30)
            break
    if k <= -1:
        c = 1