import ctypes
import json
import os
import random
import tkinter
from tkinter import filedialog

import time
import requests

from codeparts import systems
import checker

sys=systems.system()

class program():
    def __init__(self) -> None:
        self.count=0

    def start(self):
        while True:
            ctypes.windll.kernel32.SetConsoleTitleW(f'LoLChecker by liljaba1337')
            os.system('cls')
            print(sys.center(f'''

██╗░░░░░░█████╗░██╗░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██║░░░░░██╔══██╗██║░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░░░░██║░░██║██║░░░░░██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░░░░██║░░██║██║░░░░░██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
███████╗╚█████╔╝███████╗╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚══════╝░╚════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
            '''))
            print(sys.center('\nhttps://github.com/LIL-JABA/lolchecker\n'))
            print('  [1] - START CHECKER')
            print('  [2] - EDIT SETTINGS')
            print('  [3] - INFO/HELP')
            res=str(input('\n>>>'))
            if res=='1':
                self.main()
                break
            elif res=='2':
                sys.edit_settings()
                pass
            elif res=='3':
                os.system('cls')
                print(f'''
    lolchecker by liljaba1337

    discord: LIL JABA#1895
    server: https://discord.gg/r3Y5KhM7kP

  [1] - check valid/invalid/ban and save them to valid.txt in output folder
  [2] - edit checker settings

  [~] - press ENTER to return
                ''')
                input()
                continue
            else:
                continue


    def get_accounts(self,filename):
        while True:
            os.system('cls')
            try:
                with open (str(filename), 'r', encoding='UTF-8') as file:
                    lines = file.readlines()
                    ret=[]
                    for logpass in lines:
                        logpass=logpass.split(' - ')[0].replace('\n','').replace(' ','')
                        if logpass not in ret and ':' in logpass:
                            ret.append(logpass)
                        self.count+=1
                    print(f'\ndetected {self.count} accounts\n')
                    return ret
            except Exception as e:
                print(f"can't find the default file ({filename})\nplease select a new one")
                root = tkinter.Tk()
                file = filedialog.askopenfile(parent=root, mode='rb', title='select file with accounts (login:password)',
                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))
                root.destroy()
                if file==None:
                    print('u chose nothing')
                    input('press ENTER to choose again')
                    continue
                filename=str(file).split("name='")[1].split("'>")[0]
                print(filename)
                with open('system\\settings.json','r+') as f:
                    data = json.load(f)
                    data['default_file']=filename
                    f.seek(0)
                    json.dump(data, f, indent=4)
                    f.truncate()
                continue


    def main(self):
        settings=sys.load_settings()
        fn=settings['default_file']
        accounts=self.get_accounts(fn)
        check=checker.Checker(settings,accounts,self.count)
        check.main()
    
pr=program()
if __name__=='__main__':
    pr.start()
