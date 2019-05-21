#Необходимо сделать универсаьлную ссылку на пользователя в .. start = Application(backend="uia").start(r"C:\Users\vm01\AppData\Roaming\Telegram Desktop\Telegram.exe") .. строчке
#Создать батничек для отправки документа в папку C:\Users\vm01\Documents
#Написать клиент сервер для перехвата входящих сообщение
#Создать двух пользователей
#Начать писать требования к виртуалке

from pywinauto.application import Application
from pywinauto import Desktop
import time
import pywinauto
from subprocess import Popen
import psutil
import re
import string
import win32api
import win32com.client
import os
import getpass

def click_coordinate (coordinate):
    m = re.search(r'L(\d+), T(\d+), R(\d+), B(\d+)', str(coordinate))
    left = int(m.group(1))
    top = int(m.group(2))
    print (coordinate)
    pywinauto.mouse.click(button='left', coords=(left + 5, top + 5))

def telegram_test ():
    shell = win32com.client.Dispatch("WScript.Shell") #нажатие клавиш с клавиатуры

    username = getpass.getuser()
    print(username)
    path_telegram = (r"C:\\Users\\" + username + r"\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")
    print (path_telegram)
    start = Application(backend="uia").start(path_telegram) #надо получать пользователя и подменять его
    
    PROCNAME = "Telegram.exe"
    for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
            print(proc)
            app = Application(backend="uia").connect(process = proc.pid)

    dlg = app.window(title="Telegram")
    print("GO")
    
    time.sleep(5)
    
    shell.SendKeys("Saved messages")
    time.sleep(1)
    shell.SendKeys('{ENTER}')
    time.sleep(1)
    shell.SendKeys("first message - hahaha")
    time.sleep(1)
    shell.SendKeys('{ENTER}')
    time.sleep(1)

    os.system('explorer.exe C:\test\files')
    time.sleep(1)
    shell.SendKeys('%{TAB}')
    time.sleep(1)
    shell.SendKeys('^a',0)
    time.sleep(1)
    shell.SendKeys('^c',0)
    time.sleep(1)
    shell.Sendkeys('%{F4}')
    time.sleep(1)

    shell.SendKeys('%{TAB}')
    
    time.sleep(1)
    shell.SendKeys('^v',0)
    time.sleep(2)
    shell.SendKeys('{Enter}')


time.sleep(1)    
telegram_test()