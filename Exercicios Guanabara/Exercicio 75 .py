q = ''
d = 0
b = ''
j = ''
for c in range (0, 4):
    a = int(input('Digite um numero de 0 a 10: '))
    z = a % 2
    if z == 0:
        q += str(a)
    if a == 9:
        d += 1
    b += str(a)+' '
    if a == 3:
        j = 'ok'
if j == 'ok':
    f = b.index('3')
    print(f'o numero 3 foi o {f+1}° numero digitado')
print(f'o numero 9 foi digitado {d} vezes')
print(f'os numeros pares são {q}')
print(f'os numeros digitados foi {b}')