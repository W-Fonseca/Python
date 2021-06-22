from time import sleep
def contador(a,b,c):
    for z in range(a,b,c):
            sleep(0.5)
            print(z,end=' ',flush=True)
    print('FIM!')
print('=-'*10)
contador(1,11,1)
print('=-'*10)
contador(10,-1,-2)
print('=-'*10)
print('sua vez de personalizar a contagem:')
a = int(input('inicio: '))
b = int(input('Fim:'))
c = int(input('Passo: '))


if c == 0 or c == -1:
    c = 1

if a > b:
    s = c - (c*2)
    c = s
    b -= 1

elif c <= -1:
    s = c+c+c
    c = s

contador(a,b,c)