km = float(input('quantos KM rodado voce fez: '))
dias = float(input('Quantos dias alugado: '))
# 60 reias por dia / 0.15 centavos por km rodado
resultado = (dias*60)+(km*0.15)
print('Total a pagar é de: R$ ',resultado)
