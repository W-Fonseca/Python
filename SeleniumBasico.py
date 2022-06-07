#1° baixei um chromium-driver do Synaptic 
#2° installei o python 3.7
#3° instalei o pip3
#4° instalei o selenium do pip
#5° baixei o chromium do site e movi para /bin/
#6° escrevi no code:

#se for linux usar o geckodriver e firefox, confome o descritivo: 
# https://www.dev2qa.com/how-to-resolve-webdriverexception-geckodriver-executable-needs-to-be-in-path/

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#webdriver = webdriver.Firefox(executable_path= '/home/codex/Downloads/geckodriver')
webdriver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
webdriver.get("https://www.google.com/")
#se for para clicar em algo que contenha um valor especifico, pode colocar o exemplo: no xpath //div[text()='Em aberto']
############################################################################# https://devhints.io/xpath
webdriver.find_element(By.NAME,"q").send_keys("ola")
time.sleep(30)

