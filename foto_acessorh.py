import requests
import keyboard
import time
import os
import csv
from selenium import webdriver
from selenium.webdriver import ActionChains
from pathlib import Path

my_file = Path("c:/planilha")
if my_file.is_dir():
    print('Diretorio existente')

else:
    os.mkdir('c:/planilha')

print('='*30)
a = 'PESCADOR DE FOTOS RH'
print(a.center(30))
print('='*30)

print('OBS.: Por gentileza digite corretamente o CPF (sem pontos) abaixo e aperte "ENTER", para que possamos fazer o seu trabalho')

cpf = str(input('CPF: '))
senha = str(input('Por favor Digite sua senha: '))

z13 = 0
z12 = 0
z10 = 0
z1 = 0
z2 = 0
z3 = 0
z4 = 0
z5 = 0
c = 0
h = 0
v=0
p=0
p1=0
p2=0
j = 0
Net = webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe' )
Net.get( "https://admin.acessorh.com.br/" )
while j == 0:
    if v == 2:
        v = 0
        z1 = 0
        z2 = 0
        z3 = 0
    try:
        while v == 0:
            while z1 == 0:
                p += 1
                try:
                    a1 = Net.find_element_by_class_name( 'field-label' ).text
                    if a1 == 'Empresa:':
                        Net.find_element_by_id( 'tenant_id' ).send_keys( 'DURATEX' )
                        Net.find_element_by_class_name( 'button' ).click()
                        z1 = 1
                except:
                    time.sleep(1)
                    if p == 15:
                        Net.get("https://admin.acessorh.com.br/")
                        v=2
            while z2 == 0:
                p1+=1
                try:
                    a1 = Net.find_element_by_xpath( "//label[@for='userIdentifier']" ).text
                    if a1 == 'CPF ou Usuário:':
                        Net.find_element_by_id( 'userIdentifier' ).send_keys( cpf )
                        Net.find_element_by_class_name( 'button' ).click()
                        z2 = 1
                except:
                    time.sleep( 1 )
                    if p1 == 15:
                        Net.get("https://admin.acessorh.com.br/")
                        v=2
            while z3 == 0:
                p2+=1
                try:
                    a1 = Net.find_element_by_xpath( "//label[@for='password']" ).text
                    if a1 == 'Senha:':
                        Net.find_element_by_id( 'password' ).send_keys( senha )
                        Net.find_element_by_class_name( 'button' ).click()
                        j = 1
                        v=1
                        z3 = 1
                except:
                    time.sleep( 1 )
                    if p2 == 15:
                        Net.get("https://admin.acessorh.com.br/")
                        v=2
    except:
        'ok'
while z4 == 0:
    try:
        a1 = Net.find_element_by_xpath( "//button[@aria-label='Candidatos em andamento']" ).text
        if a1 == 'EM ANDAMENTO':
            Net.find_element_by_id( 'open-sidebar-account' ).click()
            time.sleep( 1 )
            Net.find_element_by_class_name( 'current-company-image' ).click()
            time.sleep( 1 )
            Net.find_element_by_xpath("//button[@aria-label='Trocar para a empresa Duratex']").click()
            z4 = 1
    except:
        time.sleep( 1 )
while z5 == 0:
    try:
        a1 = Net.find_element_by_xpath( "//button[@aria-label='Candidatos em andamento']" ).text
        if a1 == 'EM ANDAMENTO':
            Net.find_element_by_xpath("//button[@aria-label='Candidatos arquivados']").click()
            z5 = 1
    except:
        time.sleep( 1 )

while z10 == 0:
    try:
        z11= 0
        Net.find_element_by_class_name( 'button-share' ).click()
        time.sleep( 1 )
        Net.find_element_by_class_name( 'export-payroll' ).click()
        time.sleep( 1 )
        Net.find_element_by_xpath( "//select[@formcontrolname='exportPeriod']/option[text()='Última semana']" ).click()
        Net.find_element_by_xpath( "//select[@formcontrolname='reference']/option[text()='Data de conclusão']" ).click()
        Net.find_element_by_xpath( "//select[@formcontrolname='kind']/option[text()=' csv ']" ).click()
        Net.find_element_by_xpath( "//select[@formcontrolname='version']/option[text()='v3']" ).click()
        Net.find_element_by_xpath( "//button[@class='button-confirm button-default']" ).click()
        while z11 == 0:
            try:
                a = Net.find_element_by_xpath("//div[@class='exporting-container error']").text
                if a == "Ops! Ocorreu um erro na geração do arquivo. Tente novamente mais tarde.":
                    print(f'\033[31m{a}')
                    Net.find_element_by_class_name('button-cancel button-default').click()
                    z11 = 1
            except:
                try:
                    a = Net.find_element_by_xpath("//div[@class='exporting-container success']").text
                    if a == 'Arquivo gerado e exportado com sucesso.':
                        print(f'\033[32m{a}')
                        Net.quit()
                        z10 = 1
                        z11 = 1
                except:
                    print('aguardando gerar relatorio')
                    time.sleep(1)
    except:
        time.sleep(1)
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


a = os.listdir('c:/planilha/') [0]
x = 'c:/planilha/' + a
if x != 'c:/planilha/acesso.csv':
    os.rename(r'' + x, 'c:/planilha/acesso.csv')
    a = os.listdir('c:/planilha/') [0]
    x = 'c:/planilha/' + a
os.startfile(x)

z = 0
z1 = 0
z2 = 0
z3 = 0
z4 = 0
z5 = 0
z6 = 0
nlinhas = 0
v=0
p=0
p1=0
p2=0
j = 0
with open('c:/planilha/acesso.csv', newline='') as csvfile:
    for linha in csvfile:
        nlinhas += 1
    print(f'numero de matriculas na planilha é {nlinhas}')
for l in range(1, nlinhas):
    with open('c:/planilha/acesso.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar=',')
        next(spamreader)

        for row in spamreader:
            try:
                for celula in row:
                    z += 1
                    if z == 1:
                        t1 = celula
                    if z == 4:
                        d1 = celula
                    if z == 17:
                        q1 = celula
                        Net = webdriver.Chrome(executable_path='C:\webdriver\chromedriver.exe')
                        Net.get("https://admin.acessorh.com.br/")
                        while j == 0:
                            if v == 2:
                                v = 0
                                z1 = 0
                                z2=0
                                z3=0
                                print('passou em v=2')
                            try:
                                while v == 0:
                                    while z1 == 0:
                                        p += 1
                                        print(p)
                                        try:
                                            a1 = Net.find_element_by_class_name('field-label').text
                                            if a1 == 'Empresa:':
                                                Net.find_element_by_id('tenant_id').send_keys('DURATEX')
                                                Net.find_element_by_class_name('button').click()
                                                z1 = 1
                                                p = 0
                                        except:
                                            time.sleep(1)
                                            if p == 15:
                                                Net.get("https://admin.acessorh.com.br/")
                                                v=2
                                                p = 0
                                                z1 = 1
                                    while z2 == 0:
                                        p1 += 1
                                        print(p1)
                                        try:
                                            a1 = Net.find_element_by_xpath("//label[@for='userIdentifier']").text
                                            if a1 == 'CPF ou Usuário:':
                                                Net.find_element_by_id('userIdentifier').send_keys(cpf)
                                                Net.find_element_by_class_name('button').click()
                                                z2 = 1
                                                p1 = 0
                                        except:
                                            time.sleep(1)
                                            if p1 == 15:
                                                Net.get("https://admin.acessorh.com.br/")
                                                v = 2
                                                p1 = 0
                                                z2 = 1
                                    while z3 == 0:
                                        print(p2)
                                        p2 += 1
                                        try:
                                            a1 = Net.find_element_by_xpath("//label[@for='password']").text
                                            if a1 == 'Senha:':
                                                Net.find_element_by_id('password').send_keys(senha)
                                                Net.find_element_by_class_name('button').click()
                                                j = 1
                                                v = 1
                                                z3 = 1
                                                p2 = 0
                                        except:
                                            time.sleep(1)
                                            if p2 == 15:
                                                Net.get("https://admin.acessorh.com.br/")
                                                v = 2
                                                p2 = 0
                                                z3 = 1
                            except:
                                print('erro')
                            link = "https://admin.acessorh.com.br/"
                            Net.get(link)
                            page = requests.get(link)
                            while z6 == 0:
                                if page.status_code == 200:
                                    time.sleep(2)
                                    z6 = 1
                                else:
                                    time.sleep(1)
                        link = "https://admin.acessorh.com.br/candidate/documents?p=" + d1 + "&u=" + t1
                        Net.get(link)
                        page = requests.get(link)
                        while z5 == 0:
                            if page.status_code == 200:
                                time.sleep(2)
                                z5 = 1
                            else:
                                time.sleep(1)
                        while z4 == 0:
                            try:
                                Net.find_element_by_xpath(
                                 "/HTML[1]/BODY[1]/APP-ROOT[1]/APP-CONTENT-LAYOUT[1]/MAIN[1]/DIV[1]/APP-DASHBOARD[1]/APP-EMPLOYEE[1]/SECTION[1]/DIV[1]/SECTION[1]/SECTION[1]/APP-EMPLOYEE-DOCUMENTS[1]/DIV[1]/CARD-DEFAULT[6]/DIV[1]/DIV[2]/DIV[1]/APP-INFOS-CRACHA[1]/DIV[2]/FILE-MANAGER[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/SPAN[1]/A[1]/IMG-CLOUD[1]/IMG[1]").click()
                                z4 = 1
                            except:
                                try:
                                    Net.find_element_by_xpath(
                                     "/HTML[1]/BODY[1]/APP-ROOT[1]/APP-CONTENT-LAYOUT[1]/MAIN[1]/DIV[1]/APP-DASHBOARD[1]/APP-EMPLOYEE[1]/SECTION[1]/DIV[1]/SECTION[1]/SECTION[1]/APP-EMPLOYEE-DOCUMENTS[1]/DIV[1]/CARD-DEFAULT[5]/DIV[1]/DIV[2]/DIV[1]/APP-INFOS-CRACHA[1]/DIV[2]/FILE-MANAGER[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/SPAN[1]/A[1]/IMG-CLOUD[1]/IMG[1]").click()
                                    z4 = 1
                                except:
                                    try:
                                        Net.find_element_by_xpath("/HTML[1]/BODY[1]/APP-ROOT[1]/APP-CONTENT-LAYOUT[1]/MAIN[1]/DIV[1]/APP-DASHBOARD[1]/APP-EMPLOYEE[1]/SECTION[1]/DIV[1]/SECTION[1]/SECTION[1]/APP-EMPLOYEE-DOCUMENTS[1]/DIV[1]/CARD-DEFAULT[7]/DIV[1]/DIV[2]/DIV[1]/APP-INFOS-CRACHA[1]/DIV[2]/FILE-MANAGER[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/SPAN[1]/A[1]/IMG-CLOUD[1]/IMG[1]").click()
                                        z4 = 1
                                    except:
                                        try:
                                            Net.find_element_by_xpath("/HTML[1]/BODY[1]/APP-ROOT[1]/APP-CONTENT-LAYOUT[1]/MAIN[1]/DIV[1]/APP-DASHBOARD[1]/APP-EMPLOYEE[1]/SECTION[1]/DIV[1]/SECTION[1]/SECTION[1]/APP-EMPLOYEE-DOCUMENTS[1]/DIV[1]/CARD-DEFAULT[8]/DIV[1]/DIV[2]/DIV[1]/APP-INFOS-CRACHA[1]/DIV[2]/FILE-MANAGER[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/SPAN[1]/A[1]/IMG-CLOUD[1]/IMG[1]").click()
                                            z4 = 1
                                        except:
                                            try:
                                                Net.find_element_by_xpath("/HTML[1]/BODY[1]/APP-ROOT[1]/APP-CONTENT-LAYOUT[1]/MAIN[1]/DIV[1]/APP-DASHBOARD[1]/APP-EMPLOYEE[1]/SECTION[1]/DIV[1]/SECTION[1]/SECTION[1]/APP-EMPLOYEE-DOCUMENTS[1]/DIV[1]/CARD-DEFAULT[9]/DIV[1]/DIV[2]/DIV[1]/APP-INFOS-CRACHA[1]/DIV[2]/FILE-MANAGER[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/SPAN[1]/A[1]/IMG-CLOUD[1]/IMG[1]").click()
                                                z4 = 1
                                            except:
                                                try:
                                                    Net.find_element_by_xpath("/HTML[1]/BODY[1]/APP-ROOT[1]/APP-CONTENT-LAYOUT[1]/MAIN[1]/DIV[1]/APP-DASHBOARD[1]/APP-EMPLOYEE[1]/SECTION[1]/DIV[1]/SECTION[1]/SECTION[1]/APP-EMPLOYEE-DOCUMENTS[1]/DIV[1]/CARD-DEFAULT[10]/DIV[1]/DIV[2]/DIV[1]/APP-INFOS-CRACHA[1]/DIV[2]/FILE-MANAGER[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/DIV[1]/SPAN[1]/A[1]/IMG-CLOUD[1]/IMG[1]").click()
                                                    z4 = 1
                                                except:
                                                    Net.get(link)
                                                    time.sleep(7)
                        while z12 == 0:
                            try:
                                a12 = Net.find_element_by_xpath("//button[@class='active ng-star-inserted']").text
                                if a12 == 'Foto':
                                    z12 = 1
                            except:
                                time.sleep(1)

                        window_before = Net.window_handles [0]
                        actionChains = ActionChains(Net)
                        actionChains.context_click(Net.find_element_by_id('image-container')).perform()
                        time.sleep(1)
                        keyboard.press('enter')
                        keyboard.press('enter')
                        time.sleep(4)
                        y=0

                        while z13 == 0:
                            try:
                                window_after = Net.window_handles [1]
                                Net.switch_to_window(window_after)
                                time.sleep(4)
                                keyboard.press('ctrl+s')
                                time.sleep(2)
                                keyboard.write(q1 [2:])
                                time.sleep(1)
                                keyboard.press('enter')
                                time.sleep(2)
                                z13 += 1
                            except:
                                y+=1
                                try:
                                    if y == 3:
                                        print(f'\033[31m Erro ao tentar abrir a foto e salvar, Matricula: {q1}')
                                        Net.quit()
                                except:
                                    time.sleep(3)
                    if z == 353:
                        z = 0
                        z1 = 0
                        z2 = 0
                        z3 = 0
                        z4 = 0
                        z5 = 0
                        z6 = 0
                        z12 = 0
                        z10 = 0
                        z13 = 0
                        v = 0
                        j = 0
                        p = 0
                        p1 = 0
                        p2 = 0
                        Net.quit()
                        break
            except:
                Net.quit()
                print(f'\033[31m Erro ao processar a matricula: {q1}')
