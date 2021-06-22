b = [[],[]]
for c in range(0,8):
    a = int(input('Digite um valor: '))
    if a % 2 == 0:
        b[0] += [a]
    elif a % 2 == 1:
        b[1] += [a]
print(sorted(b[0]))
print(sorted(b[1]))