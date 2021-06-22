from calendar import isleap
ano = int(input('escreva um ano e te direi se é bissexto ou não: '))
a = isleap(ano)
if a == False:
    print('Ano não é Bissexto')
else:
    print('Ano Bissexto')