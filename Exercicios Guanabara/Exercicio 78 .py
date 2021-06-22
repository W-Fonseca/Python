f = []
for c in range (0,5):
    a = int(input('Digite um valor: '))
    f += [a]
print(f'os valores digitados foram: {f}')
b = max(f)
z = f.index(b)
k =f[:]
k.remove(b)
if b in k:
    g = max(k)
    v = k.index(g)+1
    print(f'os valores mais altos são {b} que se encontra na posição {z} e {v}')
else:
    print(f'o Valor mais alto é {b} que se encontra na posição {z}')
c = min(f)
x = f.index(c)
s = f[:]
s.remove(c)
if c in s:
    d = min(s)
    q = s.index(d)+1
    print(f'os menores valores são {c} que se encontra na posição {x} e {q}')

else:
    print(f'o menor valor é {c} que se encontra na posição {x}')