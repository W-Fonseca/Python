import requests
page = requests.get("https://relogioonline.com.br/horario/")
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
a = soup.find(id="lbl-time").text
print(a)
import os
os.startfile('C:\Command Prompt')