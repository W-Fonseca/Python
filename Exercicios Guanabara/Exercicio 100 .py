from random import randint
def sorteia(valores):
    for f in range(0,5):
        valores += [randint(0,10)]
    print(valores)
def somapar(num):
    l = 0
    for x in num:
        if x % 2 == 0:
            l += x
    print(l)

numeros = []
sorteia(numeros)
somapar(numeros)