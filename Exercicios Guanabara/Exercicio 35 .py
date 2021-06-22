r1 = float(input(' me diz 3 numeros de retas para eu ver se forma um triangulo: '))
r2 = float(input('2° numero: '))
r3 = float(input('3°numero: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('triangulo formado')
else:
    print('triangulo nao formado')
