numero = str(input('coloque um numero:'))
conta = numero.count('')-2
numero2 = str(numero[conta])

if numero2 == str('0'):
    print('Numero é par')
elif numero2 == str('2'):
    print('Numero é par')
elif numero2 == str('4'):
    print('Numero é par')
elif numero2 == str('6'):
    print('Numero é par')
elif numero2 == str('8'):
    print('Numero é par')

else:
    print('Numero é impar')