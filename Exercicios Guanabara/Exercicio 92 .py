dados = {}
dados['Nome'] = str(input('Digite o nome: '))
a = int(input('Digite o ano de nascimento: '))
b = 2020 - a
dados['Idade'] = b
dados['CTPS'] = int(input('Digite o numero de CTPS: [Digite "zero" para se não tem]: '))
if dados['CTPS'] == 0:
    print('=-'*40,end='=')
    print('')
    print(dados)
    for k,v in dados.items():
        print(f'{k} tem o valor {v}')
else:
    dados['Contrato'] = int(input('Digite o ano do 1° contrato: '))
    dados['Salario'] = float(input('Digite o salario: '))
    dados['aposentadoria'] = (dados['Contrato'] - a) + 35
    print('=-'*40,end='=')
    print('')
    print(dados)
    for k,v in dados.items():
        print(f'{k} tem o valor {v}')