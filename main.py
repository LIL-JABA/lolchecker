import ctypes
import json
import os
import random
import tkinter
from tkinter import filedialog

import time
import requests

from modules import systems
import checker

sys=systems.system()
check=checker.Checker()

class program():
    def __init__(self) -> None:
        self.version='1.0.0'
        self.lastver=self.version
        self.count=0

    def start(self):
        while True:
            secret=''
            if random.randint(0,50)==0:
                secret='\n\ncapybaras ontop!\n\n'
            ctypes.windll.kernel32.SetConsoleTitleW(f'LoLChecker {self.version} by liljaba1337')
            os.system('cls')
            print(sys.center(f'''

██╗░░░░░░█████╗░██╗░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██║░░░░░██╔══██╗██║░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██║░░░░░██║░░██║██║░░░░░██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██║░░░░░██║░░██║██║░░░░░██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
███████╗╚█████╔╝███████╗╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚══════╝░╚════╝░╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
            '''))
            print(sys.center(f'v{self.version}{secret}'))
            if self.lastver!=self.version:
                print(sys.center(f'update to the last version ({self.lastver}) on my GitHub'))
            print(sys.center('\nhttps://github.com/LIL-JABA/lolchecker\n'))
            print('  [1] - START CHECKER')
            print('  [2] - INFO/HELP')
            res=str(input('\n>>>'))
            if res=='1':
                self.main()
                break
            elif res=='2':
                #edit settings
                pass
            elif res=='3':
                os.system('cls')
                print(f'''
    lolchecker v{self.version} by liljaba1337

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
                        self.count+=1
                        logpass=logpass.split(' - ')[0].replace('\n','').replace(' ','')
                        ret.append(logpass)
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
        check.checker(accounts,self.count)
    
pr=program()
if __name__=='__main__':
    pr.start()
