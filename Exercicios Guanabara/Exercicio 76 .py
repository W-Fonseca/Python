listagem = ('Caderno',10.90, 'caneta',1.49,'estojo',5.00,'lapis',0.70,'bolsa',20.45,'tesoura',3.50,'cadeira gamer',
700.00,'mesa de escritorio',175.00)
print('=' * 60)
print('Lista de Compras'.center(60))
print('=' * 60)
a = '.'
j = ' '
for c in range(0, len(listagem)):
    if c % 2 ==0:
        print(f'{listagem[c]:.<30}',end='')
    else:
        print(f'R$ {listagem[c]:>6.2f}')
print('='*60)