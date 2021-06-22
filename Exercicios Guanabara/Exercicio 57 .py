L = 1
while L != 0:
    c = str(input('Qual é seu sexo [M/F]: ')).upper()
    if c in 'F M':
        if c == 'M':
            J = 'Masculino'
            print('Obrigado pela informação, seu sexo é {}'.format(J))
        else:
            J = 'Feminino'
            print(f'Obrigado pela Informação, seu sexo é {J}')
        L=0
    else:
            print('sexo não compreendido')