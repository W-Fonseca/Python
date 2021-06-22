b = 0
j = 0
c = 0
while c == 0:
    j += 1
    k = int(input('Digite um numero (Digite 999 para sair): '))
    b += k
    if k == 999:
        b -= 999
        break
print(f'você digitou {j} numeros')
print(f'A soma dos valores é {b}')