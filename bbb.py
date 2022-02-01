
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import subprocess

webdriver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
while True:
    #webdriver = webdriver.Firefox(executable_path= '/home/codex/Downloads/geckodriver')
    #webdriver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
    webdriver.get("https://gshow.globo.com/realities/bbb/bbb22/votacao/paredao-bbb22-vote-para-eliminar-luciano-naiara-azevedo-ou-natalia-269bfafb-9556-4375-b66a-4fbdc9f08396.ghtml")
    webdriver.maximize_window()
    webdriver.execute_script("window.scrollTo(0,document.body.scrollTop)")
    webdriver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    pyautogui.moveTo(417, 209)
    time.sleep(5)
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(594, 393)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write('wellington.151@hotmail.com')
    time.sleep(2)
    pyautogui.moveTo(605, 496)
    pyautogui.click()
    time.sleep(2)
    pyautogui.write('Chacal78')
    time.sleep(5)
    pyautogui.moveTo(581, 624)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(687, 706)
    pyautogui.click()
    time.sleep(10)


    try:
        webdriver.find_element(By.XPATH,"//div[text()='Para você']").click
        webdriver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
    except:
        ""
    time.sleep(10)

    pyautogui.moveTo(555, 376)
    pyautogui.click()
    time.sleep(2)
    webdriver.execute_script("window.scrollTo(0,document.body.scrollTop)")

    pyautogui.moveTo(656, 475)
    pyautogui.click()

    #while True:
    webdriver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    pyautogui.moveTo(417, 209)
    time.sleep(5)
    pyautogui.click()

    pyautogui.moveTo(557, 351)
    pyautogui.click()
    time.sleep(5)
    time.sleep(2)
    webdriver.quit()
    subprocess.call("TASKKILL /f  /IM  CHROMEDRIVER.EXE")