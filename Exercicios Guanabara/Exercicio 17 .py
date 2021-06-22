import math
co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (co ** 2+ ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
h1 = math.hypot(co,ca)
print(' a Hipotenusa vai medir {:.2f}'.format(h1))

