anonasc = int(input('em qual ano vc nasceu? '))
n = 2020 - anonasc
n2 = n - 18

if anonasc >= 2003:
    print('falta {} ano(s) para se alistar no exercito!'.format(n2))
elif anonasc == 2002:
    print('vc tem que se alistar este ano!')
elif anonasc <= 2001:
    print('vc ja passou {} do tempo de alistamento!'.format(n2))