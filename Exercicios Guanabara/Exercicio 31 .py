km = float(input('quantos km vc vai andar: '))

if km <= 200:

    v = float(km*0.50)

    print('valor da viagem é R$ {:.2f}'.format(v))

elif km >= 201:

    f = float(km*0.45)

    print('valor da viagem é R$ {:.2f}'.format(f))