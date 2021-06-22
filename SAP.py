import win32com.client
import os
import subprocess
import time
import sys

# Função para abrir a tela inicial do SAP.

def saplogin(nome_conexao):
    try:

        path = "C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe"
        subprocess.Popen(path)
        time.sleep(10)

        SapGuiAuto = win32com.client.GetObject('SAPGUI')
        if not type(SapGuiAuto) == win32com.client.CDispatch:
            return

        application = SapGuiAuto.GetScriptingEngine
        if not type(application) == win32com.client.CDispatch:
            SapGuiAuto = None
            return
        connection = application.OpenConnection(nome_conexao, True)

        if not type(connection) == win32com.client.CDispatch:
            application = None
            SapGuiAuto = None
            return

        session = connection.Children(0)
        if not type(session) == win32com.client.CDispatch:
            connection = None
            application = None
            SapGuiAuto = None
            return

        session.findById("wnd[0]/usr/txtRSYST-BNAME").text = "USERNAME"
        session.findById("wnd[0]/usr/pwdRSYST-BCODE").text = "PASSWORD"
        session.findById("wnd[0]").sendVKey(0)

    except:
        print(sys.exc_info()[0])

    finally:
        session = None
        connection = None
        application = None
        SapGuiAuto = None

def logonMultiplo():
    SapGui = win32com.client.GetObject("SAPGUI").GetScriptingEngine
    session = SapGui.FindById("ses[0]")
    session.findById("wnd[1]/usr/radMULTI_LOGON_OPT1").selected = 'true'
    session.findById("wnd[1]/tbar[0]/btn[0]").press()

def JanelaPrincipal():
    SapGui = win32com.client.GetObject("SAPGUI").GetScriptingEngine
    session = SapGui.FindById("ses[0]")
    session.findById("wnd[0]").sendVKey(0) #Apertar 1 Enter
    while True:
        JanelaPrincipal = session.findById("wnd[0]/titl").text
        if 'Easy Access' in JanelaPrincipal:
            print('Janela Principal Encontrada')
            break
        else:
            session.findById("wnd[0]/tbar[0]/btn[3]").press()

def EntrarTransação(Transacao):
    # SapGui.FindById("ses[0]").StartTransaction(Transaction="pa20")  # Start MM02 transaction
    SapGui = win32com.client.GetObject("SAPGUI").GetScriptingEngine
    session = SapGui.FindById("ses[0]")
    session.findById("wnd[0]").sendVKey(0)  # Apertar 1 Enter
    while True:
        JanelaPrincipal = session.findById("wnd[0]/titl").text
        if 'Easy Access' in JanelaPrincipal:
            session.findById("wnd[0]/tbar[0]/okcd").text = Transacao
            session.findById("wnd[0]").sendVKey(0)
            break
        else:
            session.findById("wnd[0]/tbar[0]/btn[3]").press()

def session():
    session = win32com.client.GetObject("SAPGUI").GetScriptingEngine.FindById("ses[0]")
    return session


def kill():
    os.system("taskkill /f /im saplogon.exe")

def LeiaTudo():
    SapGui = win32com.client.GetObject("SAPGUI").GetScriptingEngine
    session = SapGui.FindById("ses[0]")
    dados = session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").text
    for texto in (0,500):
        return print(dados[texto])

def LeiaColuna(coluna):
    SapGui = win32com.client.GetObject("SAPGUI").GetScriptingEngine
    session = SapGui.FindById("ses[0]")
    cont = 0
    ListaColuna = []
    while True:
        item = session.findById("wnd[0]/usr/cntlGRID1/shellcont/shell").GetCellValue(cont, coluna)
        if item > '':
            ListaColuna += [item]
            cont += 1
        else:
            break
    lista = ('')
    for valor in ListaColuna:
        lista += valor
        lista += os.linesep
    return lista

