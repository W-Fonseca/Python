k = 0
h = []
y = []
x = 0
for z in range (1,5):
    a = str(input('Digite o nome: '))
    b = int(input('Digite a Idade: '))
    j = str(input('digite o sexo: ')).upper()
    if j == 'F' and b <= 19:
        k += 1
    if j == 'M':
        y += [a]+[b]
        h += [b]
    x += b
s = x / 4
c = max(h)
u = h.index(c)
al = y.index(c)
print('Media do grupo é {}'.format(s))
print('O homem mais velho é {}'.format(y[al-1]))
print('quantas mulheres tem menos de 21 anos: {}'.format(k))