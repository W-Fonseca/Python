v = int(input('velocidade do carro:'))
if v <= 80:
    print('voce não recebe multa!')
elif v >= 81:
    conta = (v-80)*7
    print('Valor da multa é: R${:.2f}'.format(float(conta)))