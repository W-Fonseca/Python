jk = 0
zx = 0
iu = []
a = []
b = []
s = []
k = 0
print('lista de produtos ')
while k == 0:
    a = str(input('Nome do produto: ')).strip().upper()
    b = float(input('Valor do produto: '))
    if b >= 1000:
        jk += +1
    c = ' '
    zx += b
    s += [b]
    iu += [b]+[a]
    while c not in 'SN':
        c = str(input('deseja continuar: [S/N]')).strip().upper()
        if c == 'N':
            k += 1
            break
ew = min(s)
m = iu.index(ew)
vor = iu[m+1]
print(f'Total gasto na compra foi {zx}')
print(f'O produto mais barato foi {vor}')
print(f'Total de produtos maior que mil reais é {jk}')