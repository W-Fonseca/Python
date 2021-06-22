j = 0
k = 0
f = 0
c = 0
while c == 0:
    f = int(input('Digite um numero: '))
    k += f
    if f == 999:
        print('exit')
        c = 1
    else:
        j += 1
b = (k-999)

print('foram digitados {} numeros'.format(j))
print('Soma dos numeros deu o total de: {}'.format(b))

