u = 0
v = []
while u == 0:
    print('='*30)
    h = 'Menu De Inicialização'
    print(h.center(30))
    print('='*30)
    a = int(input('Digite um numero: '))
    b = int(input('Digite o segundo numero: '))
    q = int(input("""
Opções:
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa

Escolha um valor para uma ação: """))
    if q == 1:
        z = a + b
        print('A soma dos valores é igual a {}'.format(z))
        print('Reboot')
    elif q == 2:
        z = a*b
        print('A multiplicação dos 2 numeros é {}'.format(z))
        print('Reboot')
    elif q == 3:
        v = [a]+[b]
        z = max(v)
        print('O valor maior é {}'.format(z))
        print('Reboot')
    elif q == 5:
        u=1
    elif q == 4:
        print('Reboot')