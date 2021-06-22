prod = float(input('preço do pruduto: '))

print('condição de pagamentos:')
print('1 - Avista dinheiro/cheque: 10% de desconto')
print('2 - avista no cartao: 5% de desconto')
print('3 - em até 2x no cartao: preço normal')
print('4 - 3x ou mais vezes no cartão: aumento de 20%')

a = prod-(prod*0.10) #10% de desconto
b = prod-(prod*0.05) #5% de desconto
c = (prod/2) #parcelado em 2x
d = (prod*0.20)+prod #20% a mais
v = int(input('digite o metodo de pagamento : '))
if v == 1:
    print('com 10% de desconto o valor é {}'.format(a))

elif v == 2:
    print('com 5% de desconto o valor é {}'.format(b))

elif v == 3:
    print('2x no cartao, o valor fica 2x de {}'. format(c))

elif v == 4:
    print('3x ou mais o valor é de {}'.format(d))