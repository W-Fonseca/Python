salario = float(input('salario: '))
if salario >= 1250.00:
     conta = (salario * 0.10)+salario
     print('salario MAIOR de R$1250,00 - Então esse salario tera 10% de aumento com resultado de R${:.2f}'.format(conta))
else:
    conta2 = (salario * 0.15) +salario
    print('salario MENOR que R$1250,00 - Então o aumento sera de 15% com resultado de R${:.2f}'.format(conta2))