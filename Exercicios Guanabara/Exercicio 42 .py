r1 = float(input(' me diz 3 numeros de retas para eu ver se forma um triangulo: '))
r2 = float(input('2° numero: '))
r3 = float(input('3°numero: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('triangulo formado')
else:
    print('triangulo nao formado')

print('ESPECIFICAÇÃO:')
if r1 == r2 and r1 == r3 and r2 == r3:
    print('EQUILATRO: todos os lados sao guais')

elif r1 != r2 and r2 != r3 and r1 != r3:
    print('ESCALENO: todos os lados sao diferentes')

elif r2 == r1 and r2 != r3:
    print('ISOSCELES: dois lados iguais')
elif r1==r3 and r2 != r3:
    print('ISOSCELES: dois lados iguais')
elif r3==r2 and r1 != r3:
    print('ISOSCELES: dois lados iguais')