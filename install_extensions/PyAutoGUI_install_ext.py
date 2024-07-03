import pyautogui
import time
import os

pyautogui.hotkey('ctrl','alt','t')
time.sleep(2)

pyautogui.write('code .')
pyautogui.hotkey('enter')
time.sleep(5)

pyautogui.hotkey('ctrl','shift','x')
time.sleep(3)
pyautogui.hotkey('escape')
lst=['clangd','c++ testmate','cmake','cmake tools','c++ helper']

for item in lst:
    pyautogui.write(item)
    time.sleep(3)

    pyautogui.moveTo(200,200)
    pyautogui.click()
    time.sleep(5)

    point=None
    
    try:
        point=pyautogui.locateOnScreen("install_pic.png",confidence=0.7)
        pyautogui.moveTo(point[0]+25,point[1]+15)
        print('found')
        pyautogui.click()
        time.sleep(2)
    except:
        print('Not found')
        pyautogui.moveTo(800,295)
        pyautogui.click()


    
    
    pyautogui.hotkey('ctrl','shift','x')
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('delete')
    time.sleep(2)
    
pyautogui.hotkey('alt','f4')

