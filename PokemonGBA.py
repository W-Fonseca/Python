import pyautogui
import subprocess
import time
from PIL import ImageGrab


#screenshot = pyautogui.screenshot()
#screenshot.save("screen.png")
c = 0
hora_inicio = time.time()

resetes = 0
while c == 0:

    subprocess.call("C:\Program Files\BlueStacks_nxt\HD-Player.exe --instance Nougat64")
    pyautogui.hotkey ('f11')
    pyautogui.hotkey ('alt','shift', 't')
    time.sleep(12)
    pyautogui.hotkey ('alt','f4')

    
    image = ImageGrab.grab(bbox=(440,248,463,274))
    #image = ImageGrab.grab(bbox=(440,243,463,274))
    #image = ImageGrab.grab(bbox=(450,240,467,294))
    #image.save('pokemon.png')

    check_pixel = image.getpixel((10, 20))
    print("Check pixel", check_pixel)

    if check_pixel != (255,146,66):
        c = 1
        print('Charmander Shyne é vc?')
    resetes += 1
    print(f'Numero de resetes é {resetes}')
    tempo_Atual = time.time()
    print(format(tempo_Atual-hora_inicio))
