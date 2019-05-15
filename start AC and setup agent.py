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


def click_coordinate (coordinate):
        m = re.search(r'L(\d+), T(\d+), R(\d+), B(\d+)', str(coordinate))
        left = int(m.group(1))
        top = int(m.group(2))
        print (coordinate)
        pywinauto.mouse.click(button='left', coords=(left + 5, top + 5))


def start_AC():
        start = Application(backend="uia").start(r"C:\Program Files\Falcongaze SecureTower\Administrator Console\FgStAdminConsoleLaunch.exe")
        time.sleep (10)
        PROCNAME = "FalconGaze.SecureTower.AdminConsole.exe"

        for proc in psutil.process_iter():
                if proc.name() == PROCNAME:
                        print(proc)
                        app = Application(backend="uia").connect(process = proc.pid)


        time.sleep (1)
        dlg = app.window(title="Connection to the Central Server")
        time.sleep (1)
        app.dlg.Connect.click()
        try:
                app.dlg.Login.click()
        except:
                print("Логин не нужне")
        time.sleep(25)
        print ("АС запущена")

def install_agent():
        shell = win32com.client.Dispatch("WScript.Shell")
        PROCNAME = "FalconGaze.SecureTower.AdminConsole.exe"

        for proc in psutil.process_iter():
                if proc.name() == PROCNAME:
                        print(proc)
                        app = Application(backend="uia").connect(process = proc.pid)

        dlg = app.window(title="Falcongaze SecureTower Administrator console")
        print ("ГОТОВ")

        coordinate = app.dlg['Agents'].rectangle()
        click_coordinate (coordinate)

        try:
                for proc in psutil.process_iter():
                        if proc.name() == PROCNAME:
                                print(proc)
                                app = Application(backend="uia").connect(process = proc.pid)

                dlg = app.window(title="Falcongaze SecureTower Administrator console")
                coordinate = app.dlg['Endpoint agents options'].rectangle()
                click_coordinate (coordinate)
        except:
                print ("Не смог найти элемент Endpoint agents options. Перезапускаю АС")
                os.system("taskkill /im FalconGaze.SecureTower.AdminConsole.exe")
                start_AC()
                install_agent()
        else:
                print ("Наконец блять")

        coordinate = app.dlg['Computers to install agents on'].rectangle()
        click_coordinate (coordinate)

        dlg = app.window(title="Computer list")

        coordinate = app.dlg['Add object'].rectangle()
        click_coordinate (coordinate)

        coordinate = app.dlg['Computer name'].rectangle()
        click_coordinate (coordinate)

        coordinate = app.dlg['Manually'].rectangle()
        click_coordinate (coordinate)

        shell.SendKeys("name_agent22")
        shell.SendKeys('^{ENTER}')
        shell.SendKeys('{ENTER}')
                
        coordinate = app.dlg['Install agents on specified computers only'].rectangle()
        click_coordinate (coordinate)
        shell.SendKeys('+{TAB}')
        shell.SendKeys('+{TAB}')
        shell.SendKeys('{ENTER}')

        print ("Тест завершен. Агент поставлен на установку!")

start_AC()
time.sleep(1)
<<<<<<< HEAD
install_agent()
=======
install_agent()

#It's my first change on the desktop
#This is my second change on the desktop
>>>>>>> test
