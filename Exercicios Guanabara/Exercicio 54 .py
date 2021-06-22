s = 0
n = 0
for c in range (0,8):
    idade = int(input('qual o ano de nascimento: '))
    v = int(2020 - idade)

    if v >= 21:
        s += 1
    elif v <= 20:
        n+=1
print('Numero de pessoas maior de 18 anos é: '.format(s))
print('Numero de Pessoas menor de 18 anos é: '.format(v))