v = 0
u = 0
j = 0
idade = []
sexo = []
c = 0
print('Cadastramento de Pessoas')
while c == 0:
    sexo = str(input('Informe o Sexo: [M/F] ')).upper()
    if sexo == 'M' or sexo == 'N':
        if sexo == 'M':
            j += 1
        idade = int(input('Informe a idade '))
        if idade >= 0:
            if idade > 18:
                v += 1
            elif idade <20 and sexo == 'F':
                u += 1
        z = str(input('Deseja cadastrar + 1 pessoa? [S/N]')).upper()
        if z == 'N':
            break
p = 'Estatistica'
print('='*30)
print(p.center(30))
print('='*30)
print(f'total de Homens cadastrado {j}')
print(f'Total de pessoas com menos de 18 anos é {v}')
print(f'Total de mulheres com menos de 20 anos é {u}')