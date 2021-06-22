bo = []
p = 0
g = 0
f = 0
a = 0
b = 0
c = 0
d = 'S'
while c <= 11:
    c += 1
    g += 1
    p += 1
    a = int(input('Digite um valor:'))
    bo += [a]
    f += a
    print(c)
    if p == 10:
        d = str(input('deseja continuar [S/N]: ')).upper()
        if d == 'S':
            c -= c
            p -= p
        elif d == 'N':
            c = 999
            print('saindo')
pi = f / g
li = max(bo)
lj = min(bo)
print('A media do valor é {}'.format(pi))
print('Qual o maior valor inserido {}'.format(li))
print('Menor valor foi {}'.format(lj))
print('numero de valores inseridos foi {} '.format(g))