print('-#'*21+'-')
casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual seu salario: '))
anos = int(input('quantos anos você vai pagar: '))
print('-#-'*20)
prestacao = casa/(anos*12)

trinta = (salario *0.30)

if trinta < prestacao:
    print('-#-'*20+'-')
    print('Emprestimo Negado')
    print('Valor da Prestação: {:.f2}'.format(prestacao))
    print('-#-'*20+'-')
elif trinta > prestacao:
    print('-#-'*20+'-')
    print('Empretimo Concedido')
    print('Valor da Prestação: {:.f2}'.format(prestacao))
    print('-#-'*20+'-')