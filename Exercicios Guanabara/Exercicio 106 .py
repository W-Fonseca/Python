def ajuda(nomefun):
    print('\033[1;40m',end='')
    print('~'*40)
    print(nomefun.center(40))
    print('~'*40)
    print('\033[m')

def func(s):
        import time
        print('\033[1;45m')
        print('~'*40)
        print(f'Acessando o manual do comando {s}')
        print('~'*40)
        print('\033[m')
        time.sleep(1)
        print('\033[1;44m')
        help(s)
        print('\033[m')
c = 0
while c == 0:
    ajuda('SISTEMA DE AJUDA PyHELP')
    f = str(input('Função ou Biblioteca > '))
    if f == 'fim':
        print('\033[1;47m',end='')
        print('~'*40)
        print(f'Finalizando processo!')
        print('~'*40)
        print('\033[m')
        c = 1
    else:
        func(f)