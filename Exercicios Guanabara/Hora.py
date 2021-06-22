from pynput.keyboard import Key, Controller
keyboard = Controller
#import os
import requests
page = requests.get("https://relogioonline.com.br/horario/")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
a = soup.find(id="lbl-time").text
print(a)
#os.startfile('c:\Command Prompt')
keyboard.press(Key.left)
keyboard.release(Key.left)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
keyboard.press(a)
keyboard.release(a)