a = int(input('me diz um numero: '))
b = int(input(' me diz outro numero: '))
c = int(input(' me diz o 3° numero: '))

if a> b and a> c:
    print('maior',a)
elif b > a and b > c:
    print('maior', b)
elif c > b or c > a:
    print('maior', c)
