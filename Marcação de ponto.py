from selenium import webdriver
import time
x = 0
y = 0
z = 0
driver = webdriver.Chrome(executable_path='C:\chromedriver.exe')
driver.get("https://sapmobile.duratex.com.br/sap/bc/ui5_ui5/ui2/ushell/shells/abap/FioriLaunchpad.html#Shell-home")

while z == 0:
    try:
        a = driver.find_element_by_class_name("sapUshellAnchorItemInner").text
        print(a)
        if a == 'Minha página inicial':
            driver.find_element_by_id("__tile1").click()
            z = 1
    except:
        time.sleep(1)
while y == 0:
    try:
        a = driver.find_element_by_id("__section3-title").text
        print(a)
        if a == "BANCO HORAS":
            driver.find_element_by_id("__item3-__xmlview0--PointTreatmentTable-0-selectMulti-CbBg").click()
            y = 1
    except:
        time.sleep(1)
driver.find_element_by_id("__xmlview0--editMarks-BDI-content").click()
while x == 0:
    try:
        a = driver.find_element_by_id("__popover1-title-inner").text
        print(a)
        if a == "Inserir Marcações":
            driver.find_element_by_id("__input1-__clone12-inner").click()
            driver.find_element_by_id("__input1-__clone12-inner").send_keys("08:30")
            driver.find_element_by_id("__input1-__clone15-inner").click()
            driver.find_element_by_id("__input1-__clone15-inner").send_keys("17:43")
            driver.find_element_by_id("__box4-__clone14-inner").click()
            driver.find_element_by_id("__box4-__clone14-inner").send_keys("Home Office")
            driver.find_element_by_id("__input1-__clone12-inner").click()
            driver.find_element_by_id("__box4-__clone17-inner").click()
            driver.find_element_by_id("__box4-__clone17-inner").send_keys("Home Office")
            x = 1
    except:
        time.sleep(1)
driver.find_element_by_id("__button11-BDI-content").click()