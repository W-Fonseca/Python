import math
angulo = float(input('digite o angulo que deseja: '))
angulo1 = math.radians(angulo)
senno = math.sin(angulo1)
print('seno = {:.2f}'.format(senno))
coseno = math.cos(angulo1)
print('coseno = {:.2f}'.format(coseno))
tangente = math.tan(angulo1)
print('tangente = {:.2f}'.format(tangente))