z = 0
b = [[],[],[]]
for c in range(0,3):
    a = int(input(f'digite um valor [0,{c}]: '))
    b[0] += [a]
    if a % 2 == 0:
        z += a
for d in range(0,3):
    a = int(input(f'digite um valor [1,{d}]: '))
    b[1] += [a]
    if a % 2 == 0:
        z += a
for g in range(0,3):
    a = int(input(f'digite um valor [2,{g}]: '))
    b[2] += [a]
    if a % 2 == 0:
        z += a
print(f'[ {b[0][0]} ][ {b[0][1]} ][ {b[0][2]} ]')
print(f'[ {b[1][0]} ][ {b[1][1]} ][ {b[1][2]} ]')
print(f'[ {b[2][0]} ][ {b[2][1]} ][ {b[2][2]} ]')

x = b[0][2]+b[1][2]+b[2][2]
v = max(b[1][0],b[1][1],b[1][2])
print(f'A soma dos valores pares é {z}')
print(f'A soma da coluna 3 é {x}')
print(f'a soma da linha 2 é {v}')