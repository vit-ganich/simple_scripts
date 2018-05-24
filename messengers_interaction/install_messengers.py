import os
import time
import glob
import pyautogui
from datetime import datetime


"""
Download and install messengers:
Telegram - in silent mode,
ICQ10 - in default mode (with kostyl' - pressing 'enter')
"""


def take_screenshot(err):
    '''Takes screenshots and stores them in the script folder'''
    
    try:
        time_now = datetime.today().strftime("%H-%M-%S")
        pyautogui.screenshot('%s_(err_%s).png' % (time_now, err))
    except:
        print('screenshot error')

        
def writeLog(message):    
    time_now = datetime.today().strftime("%d.%m.%Y %H:%M:%S")
    with open(r'C:\Sikuli\log.txt','a') as f:
        f.write(time_now + message + '\n')
        
        
def install_telegram(browser, download_link, exe_name):
    """Start Chrome and download Telegram.exe"""
    
    test_name = r' "Установка Telegram" '
    
    try:
        err = 0
        os.system('start %s %s' % (browser, download_link))
        time.sleep(30)
        take_screenshot(err)
        time.sleep(30)
        os.system(r'TASKKILL /IM chrome.exe /F')
        time.sleep(5)
        # Find installer file in Downloads folder and run it
        err = 1
        installer = glob.glob(r'C:\users\admin\downloads\%s' % exe_name)
        if installer:
            print(installer)
            os.system('%s /SP- /VERYSILENT' % installer[0])
            err = ' Успешно пройден. '
            take_screenshot(err)
        else:
            err = ' Инсталлятор не найден '
        time.sleep(5)
    except:
        take_screenshot(err)
        writeLog(r' Ошибка при установке ' + 'Строка: ' + str(err) + test_name)
    else:
        writeLog(str(err) + test_name)


def install_ICQ(browser, download_link, exe_name):
    """Start Chrome and download ICQ.exe"""
    
    test_name = r' "Установка ICQ10" '
    
    try:
        err = 0
        os.system('start %s %s' % (browser, download_link))
        time.sleep(30)
        take_screenshot(err)
        time.sleep(30)
        os.system(r'TASKKILL /IM chrome.exe /F')
        time.sleep(5)
        # Find installer file in Downloads folder and run it
        err = 1
        installer = glob.glob(r'C:\users\admin\downloads\%s' % exe_name)
        if installer:
            print(installer)
            os.system('%s' % installer[0])
            time.sleep(10)
            pyautogui.press('enter')
            err = ' Успешно пройден. '
            take_screenshot(err)
        else:
            err = ' Инсталлятор не найден '
        time.sleep(30)
    except:
        take_screenshot(err)
        writeLog(r' Ошибка при установке ' + 'Строка: ' + str(err) + test_name)
    else:
        writeLog(str(err) + test_name)
    os.system(r'TASKKILL /IM icq.exe /F')


browser = r'C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe'
download_telegram = r'https://telegram.org/dl/desktop/win'
download_ICQ = r'https://r.mail.ru/clo12053242/icq.mail.ru/exe.icq.com/icqsetup.exe'


try:
    os.chdir(r'C:\Sikuli\Scripts\Protocols_intercept\install_messengers')
except:
    print("error while changing directory")
    
install_telegram(browser, download_telegram, 'tsetup*.exe')
install_ICQ(browser, download_ICQ, 'icq*.exe')
