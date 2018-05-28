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

browser = r'C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe'
#  download links for Telegram, Viber and ICQ10
download_link = r'https://telegram.org/dl/desktop/win https://r.mail.ru/clo12053242/icq.mail.ru/exe.icq.com/icqsetup.exe https://download.cdn.viber.com/desktop/windows/ViberSetup.exe'
telegram_exe = r'tsetup*.exe'
icq_exe = 'icq*.exe'
viber_exe = 'viber*.exe'
working_directory = r'C:\Sikuli\Scripts\Protocols_intercept\install_messengers'


def download_telegram_and_icq_and_viber(browser, download_link):
    """Start Chrome and download Telegram.exe + ICQ10.exe"""
    
    test_name = r' "Download Telegram + Viber + ICQ10"'
    
    try:
        os.system('start %s %s' % (browser, download_link))
        time.sleep(70)
        take_screenshot(err)
        err = 'Success'
    except:
        err = 'Download error'
    finally:
        writeLog("%s - %s" % (test_name, err))
        

def install_ICQ(exe_name):
    """
    Find in Downloads folder and install ICQ.exe. Press ENTER
    """
    
    test_name = r' "Установка ICQ10" '
    try:
        err = 0
        os.system(r'TASKKILL /IM chrome.exe /F') # kill Chrome!!!
        # Find installer file in Downloads folder and run it
        installer = glob.glob(r'C:\users\admin\downloads\%s' % exe_name)
        if installer:
            print(installer)
            os.system('%s' % installer[0])
            time.sleep(10)
            pyautogui.press('enter')
            time.sleep(1)
            take_screenshot(err)
            err = ' Успешно пройден. '
    except:
        err = ' Error. Инсталлятор не найден '
        take_screenshot(err)
    finally:
        writeLog("%s - %s" % (test_name, err))


def install_telegram(exe_name):
    """
    Find in Downloads folder and install Telegram.exe in SILENT mode
    """
    
    test_name = r' "Установка Telegram"'
    try:
        err = 0
        # Find installer file in Downloads folder and run it
        installer = glob.glob(r'C:\users\admin\downloads\%s' % exe_name)
        if installer:
            print(installer)
            os.system('%s /SP- /VERYSILENT' % installer[0])
            take_screenshot(err)
            err = 'Успешно пройден.'
    except:
        err = 'Error. Инсталлятор не найден'
        take_screenshot(err)
    else:
        writeLog("%s - %s" % (test_name, err))


def install_viber(exe_name):
    """
    Find in Downloads folder and run ViberSetup.exe
    """
    
    test_name = r' "Установка Viber" '
    try:
        err = 0
        # Find installer file in Downloads folder and run it in silent mode
        installer = glob.glob(r'C:\users\admin\downloads\%s' % exe_name)
        if installer:
            print(installer)
            os.system('%s /S' % installer[0])
            time.sleep(5)
            take_screenshot(err)
            err = ' Успешно пройден. '
    except:
        err = ' Error. Инсталлятор не найден '
        take_screenshot(err)
    finally:
        os.system("TASKKILL /IM icq.exe /F")
        os.system("TASKKILL /IM chrome.exe /F") # kill Chrome!!!
        os.system("TASKKILL /IM viber.exe /F")
        writeLog("%s - %s" % (test_name, err))


def change_working_dir(working_dir):
    """Need for prompt screenshots saving"""
    try:
        os.chdir(working_dir)
    except:
        print("error while changing directory")


def take_screenshot(err):
    '''Take screenshot and store into a script folder'''
    try:
        pyautogui.screenshot('%s_(err_%s).png' % (time.time(), err))
    except:
        print('screenshot error')

        
def writeLog(message):    
    time_now = datetime.today().strftime("%d.%m.%Y %H:%M:%S")
    with open(r'C:\Sikuli\log.txt','a') as f:
        f.write(time_now + message + '\n')


change_working_dir(working_directory)
download_telegram_and_icq_and_viber(browser, download_link)
install_ICQ(icq_exe)
install_telegram(telegram_exe)
install_viber(viber_exe)

