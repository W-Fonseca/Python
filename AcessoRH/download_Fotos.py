from Lib.AcessoRH import ExportandoExcel, Pescandofotos
import time
c = 0
h = 0
print('='*30)
a = 'PESCADOR DE FOTOS RH'
print(a.center(30))
print('='*30)

print('OBS.: Por gentileza digite corretamente o CPF (sem pontos) abaixo e aperte "ENTER", para que possamos fazer o seu trabalho')
cpf = str(input('CPF: '))
senha = str(input('Por favor Digite sua senha: '))

s = ExportandoExcel.planilha(cpf, senha)
print('~-'*30)
print('Por Favor coloque o arquivo "CSV" que esta na pasta "Downloads" para pasta "C:\Planilha"')
print('~-'*30)
while c == 0:
    l = ' '
    while h == 0:
        l = str(input('Você colocou: [Digite Sim ou Nao]')).upper()
        if l == 'SIM':
            c = 1
            h = 1
        elif l == 'NAO':
            print('Por favor coloque a planilha baixada em "C:\Planilha"')
        else:
            print('Nao entendi o que você digitou!!!')

j = Pescandofotos.download(cpf, senha)