peso = float(input('peso: '))
alt = float(input('Altura: '))

calc = peso/(alt*2)

if calc <18.5:
    print('abaixo do peso')
elif calc >= 18.5 and calc <= 25:
    print('peso ideal')
elif calc >= 26 and calc <= 30:
    print('Sobrepeso')
elif calc >= 31 and calc <=40:
    print('Obesidade')
elif calc >=41:
    print('Obesidade morbida')
print(calc)