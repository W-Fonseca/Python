import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup
class windowspython:
    def __init__(self):
        layout = [
            [sg.Text('Pesquisa'),sg.Input(size=(15,0),key='Pesquisa')],
            [sg.Button('Pesquisar')],
            [sg.Output(size=(80,20))]
        ]
        self.Janela = sg.Window("Pesquisa Wikipédia").layout(layout)


    def Iniciar(self):
        while True:

            self.button, self.values = self.Janela.Read()
            pesquisa = self.values['Pesquisa']
            Cont = 0
            page = requests.get("https://pt.wikipedia.org/w/index.php?search="+pesquisa)
            soup = BeautifulSoup(page.content, 'html.parser')
            contagem = len(soup.select_one("body").select("p"))
            texto = ""
            for numero in range(0, contagem):
                texto += soup.select_one("div.mw-parser-output p").extract().text
                texto += "\n"
            print(texto)

tela= windowspython()
tela.Iniciar()