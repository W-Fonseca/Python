z = 0
d = []
c = 0
k = 0
while k == 0:
    a = int(input('Digite um numero: '))
    c += 1
    b = ' '
    d += [a]
    if a == 5:
     z+= 1
    while b not in 'SN':
        b = str(input('Deseja continuar [S/N]: ')).upper()
        if b == 'N':
            k += 1
        elif b == 'S':
            'ok'
print(f'foi digitado um total de {c} numeros')
d.sort(reverse=True)
print(f'os valores foram {d}')
if z == 0:
    print('não foi digitado nenhum numero 5')
elif z >= 1:
    print(f'foi digitado {z} numero 5')