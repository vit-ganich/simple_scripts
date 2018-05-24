import winreg


def reg_key(registry_branch, regkey): 
    '''
    Get key value from winregistry.HCLM.
    If reg has no key - send warn message
    '''
    try:
        hKey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, registry_branch)
        result = winreg.QueryValueEx(hKey, regkey)
        winreg.CloseKey(hKey)
        print (result[0])
        #return (result[0])
    except FileNotFoundError as error:
        print ('No reg_key! ')

#  For example, Viber version
registry_branch = r"SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\{41B14B3B-C2AB-4DD2-A620-BA72244CB31E}"
regkey =  "DisplayVersion"

reg_key(registry_branch, regkey)
