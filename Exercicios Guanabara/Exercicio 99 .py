from time import sleep
def maior(val):
    h = 0
    s = len(val)
    k = max(val)
    print(f'foi digitado ',end='')
    if h == 0:
        for z in val:
            sleep(1)
            print(f'{z} ',end='')
    print(f'com total de {s} valores e o maior é {k}')


x = []
c = 0
while c == 0:
    b = ' '
    z = int(input('Digite um valor: '))
    x += [z]
    while b not in 'SN:':
        b = str(input('deseja continuar [S/N]: ')).upper()
        if b == 'S':
            'ok'
        elif b == 'N':
            c = 1
maior(x)