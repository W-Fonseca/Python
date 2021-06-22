def planilha(cpf,senha):
    from selenium import webdriver
    import time
    z1 = 0
    z2 = 0
    z3 = 0
    z4 = 0
    z5 = 0
    Net = webdriver.Chrome('C:\chromedriver.exe')
    Net.get("https://admin.acessorh.com.br/")

    while z1 == 0:
        try:
            a1 = Net.find_element_by_class_name('field-label').text
            if a1 == 'Empresa:':
                Net.find_element_by_id('tenant_id').send_keys('DURATEX')
                Net.find_element_by_class_name('button').click()
                z1 = 1
        except:
            time.sleep(1)
    while z2 == 0:
        try:
            a1 = Net.find_element_by_xpath("//label[@for='userIdentifier']").text
            if a1 == 'CPF ou Usuário:':
                Net.find_element_by_id('userIdentifier').send_keys(cpf)
                Net.find_element_by_class_name('button').click()
                z2 = 1
        except:
            time.sleep(1)

    while z3 == 0:
        try:
            a1 = Net.find_element_by_xpath("//label[@for='password']").text
            if a1 == 'Senha:':
                Net.find_element_by_id('password').send_keys(senha)
                Net.find_element_by_class_name('button').click()
                z3 = 1
        except:
            time.sleep(3)
    while z4 == 0:
        try:
            a1 = Net.find_element_by_xpath("//button[@aria-label='Candidatos em andamento']").text
            if a1 == 'EM ANDAMENTO':
                Net.find_element_by_id('open-sidebar-account').click()
                time.sleep(1)
                Net.find_element_by_class_name('current-company-image').click()
                time.sleep(1)
                Net.find_element_by_xpath(
                    "/HTML[1]/BODY[1]/APP-ROOT[1]/APP-CONTENT-LAYOUT[1]/APP-SIDEBAR-ACCOUNT[1]/ASIDE[1]/DIV[1]/DIV[2]/APP-COMPANIES[1]/DIV[1]/UL[4]/LI[1]/BUTTON[1]").click()
                z4 = 1
        except:
            time.sleep(1)
    while z5 == 0:
        try:
            a1 = Net.find_element_by_xpath("//button[@aria-label='Candidatos em andamento']").text
            if a1 == 'EM ANDAMENTO':
                Net.find_element_by_xpath(
                    "/HTML[1]/BODY[1]/APP-ROOT[1]/APP-CONTENT-LAYOUT[1]/MAIN[1]/DIV[1]/APP-DASHBOARD[1]/APP-DASHBOARD-HOME[1]/DIV[1]/UL[1]/LI[3]/BUTTON[1]").click()
                z5 = 1
        except:
            time.sleep(1)

    Net.find_element_by_class_name('button-share').click()
    time.sleep(1)
    Net.find_element_by_class_name('export-payroll').click()
    time.sleep(1)

    Net.find_element_by_xpath("//select[@formcontrolname='exportPeriod']/option[text()='Última semana']").click()
    Net.find_element_by_xpath("//select[@formcontrolname='reference']/option[text()='Data de conclusão']").click()
    Net.find_element_by_xpath("//select[@formcontrolname='kind']/option[text()=' csv ']").click()
    Net.find_element_by_xpath("//select[@formcontrolname='version']/option[text()='v3']").click()
    Net.find_element_by_xpath("//button[@class='button-confirm button-default']").click()