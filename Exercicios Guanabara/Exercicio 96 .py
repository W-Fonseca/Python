def area(larg, compr):
    s = larg * compr
    print(f'A área de um terreno {larg}x{compr} é de {s}m²')


print('controle de terrenos')
print('--------------------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
