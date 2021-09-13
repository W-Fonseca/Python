from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

webdriver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
webdriver.get("https://outlook.live.com/mail/0/inbox")
time.sleep(5)

webdriver.find_element(By.XPATH,"/html/body/header/div/aside/div/nav/ul/li[2]/a").click()
time.sleep(3)
webdriver.find_element(By.ID,"i0116").send_keys("wellington.151@outlook.com")
time.sleep(3)
webdriver.find_element(By.XPATH,"//*[@id='idSIButton9']").click()
time.sleep(5)
webdriver.find_element(By.XPATH,"//*[@id='i0118']").send_keys("Artilharia78")
time.sleep(3)
webdriver.find_element(By.XPATH,"//*[@id='idSIButton9']").click()
time.sleep(3)
webdriver.find_element(By.XPATH,"//*[@id='idSIButton9']").click()
time.sleep(3)
webdriver.find_element(By.XPATH,"//*[@class='NsB53xFTU532cgP0ztFSC'][1]").click()
time.sleep(5)

imagemExiste = True
Contagem=0
while imagemExiste == True:
    Contagem += 1
    try:
        webdriver.find_element(By.XPATH,"//*[@class='_3FmK0GDnz9GXGERKjBkWbO']").click()
        time.sleep(5)
        ActionChains(webdriver).context_click(webdriver.find_element(By.XPATH,f"//*[@class='iVDUAPPz0v5pGspIdBxq-'][{Contagem}]")).perform() #tudo isso para apertar com botão direito do mouse
        time.sleep(2)
        webdriver.find_element(By.XPATH,"//*[@title='Baixar']").click()
    except:
        print("fim")
        imagemExiste = False


time.sleep(5000)