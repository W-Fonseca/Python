n1= float(input('me diz sua nota:'))
n2= float(input('segunda nota: '))
n3 = (n1+n2)/2
if n3 < 5:
    print('vc reprovou')
elif n3 >=5 and n3 <=6.9:
    print('recuperação')
elif n3 >=7:
    print('aprovado')