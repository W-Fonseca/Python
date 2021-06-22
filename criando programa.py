from tkinter import *

import webbrowser

def bt_click(): 
        webbrowser.open('https://drive.google.com/drive/my-drive')

        lb["text"] = "funcionou"
        
janela = Tk()

bt = Button(janela, width=20, text="Vamos conectar?",command=bt_click)
bt.place(x=1, y=1)

lb = Label(janela, text="Conectando REDE")
lb.place(x=1, y=30)


