pessoa = {}
cadastro = []
mulheres = []
maior = []
c = 0
b = 0
x = 0
while c == 0:
    pessoa['Nome'] = str(input('Digite o nome: ')).upper()
    pessoa['Sexo'] = str(input('Digite o Sexo [M/F]:  ')).upper()
    pessoa['idade'] = int(input('Digite a idade: '))
    b += 1
    x += pessoa['idade']
    cadastro.append(pessoa.copy())
    maior += [pessoa['idade']]
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'][:])
    z = ' '
    while z not in 'SN':
        z = str(input('Deseja cadastrar mais uma pessoa [S/N]')).upper()
        if z == 'N':
            c = 1
        elif z == 'S':
            'ok'
r = x/b
print('=-'*40)
print(f'- o grupo tem {b} pessoas')
print(f'- a media de idade de todos é {r:.2f} ')
print(f'- as mulheres cadastradas são {mulheres}')
print(f'- lista da pessoas que estão a cima da média:')
for w in range(0,b):
    if maior[w] > r:
        print(cadastro[w])
    else:
        continue