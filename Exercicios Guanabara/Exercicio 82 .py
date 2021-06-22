v = []
u = 0
p = []
z = []
c = 0
while c == 0:
    a = int(input('digite um numero: '))
    b = ' '
    u += 1
    z += [a]
    while b not in 'SN':
        b = str(input('Deseja continuar [S/N] ')).upper()
        if b == 'N':
            c = 1
        elif b == 'S':
            'ok'
for o in range(0,u,1):
    x = z[o] % 2
    if x == 0:
        p += [z[o]]
    elif x == 1:
        v += [z[o]]
print(f'a lista digitada foi {z}')
print(f'a lista com numeros pares é {p}')
print(f'a lista com numeros impares é {v}')