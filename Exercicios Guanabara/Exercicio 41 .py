print('atletas nadadores')

n = int(input('me diz a idade do atleta: '))

if n <=9:
    print('categoria mirim')
elif n >=10 and n <= 14:
    print('categoria infantil: ')
elif n >= 15 and n <= 19:
    print('Categoria Junior')
elif n >= 20:
    print('categoria SENIOR')