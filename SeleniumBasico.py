#1° baixei um chromium-driver do Synaptic
#2° installei o python 3.7
#3° instalei o pip3
#4° instalei o selenium do pip
#5° baixei o chromium do site e movi para /bin/
#6° escrevi no code:

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

webdriver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
webdriver.get("https://www.google.com/")
webdriver.find_element(By.NAME,"q").send_keys("ola")
time.sleep(30)

