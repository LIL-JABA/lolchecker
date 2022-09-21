import random
import requests
import json
import os
from tkinter import filedialog
import tkinter

class system():
    def __init__(self) -> None:
        path = os.getcwd()
        self.parentpath=os.path.abspath(os.path.join(path, os.pardir))
        self.proxylist=[]
        self.proxy = set()

    def center(self,var:str, space:int=None): # From Pycenter
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())

    def load_settings(self):
        try:
            f = open('system\\settings.json')
            data = json.load(f)
            f.close()
            return data
        except:
            print("can't find settings.json\nplease download it from my github\n")
            return False

    def edit_settings(self):
        while True:
            try:
                f = open('system\\settings.json','r+',encoding='UTF-8')
                data = json.load(f)
            except:
                print("can't find settings.json\nplease download it from my github\n")
                return False
            os.system('cls')
            deffile=data['default_file']
            webhook=data['webhook']
            print(f'[1] defaut file - {deffile}')
            print(f'[2] webhook - {webhook}')
            print(f'[~] any other number to return')
            what=int(input('what to edit? >>>'))
            if what == 1:
                root = tkinter.Tk()
                file = filedialog.askopenfile(parent=root, mode='rb', title='select file with accounts (login:password)',
                    filetype=(("txt", "*.txt"), ("All files", "*.txt")))
                root.destroy()
                if file==None:
                    filename='None'
                else:
                    filename=str(file).split("name='")[1].split("'>")[0]
                data['default_file']=filename
            elif what==2:
                newwebhook=input('ented the discord webhook to use (leave it empty if u dont wanna use it): ')
                data['webhook']=newwebhook
            else:
                return
            f.seek(0)
            json.dump(data, f, indent=4)
            f.truncate()
            f.close()

    def load_proxy(self):
        with open(f"{self.parentpath}\\proxy.txt", "r") as f:
            file_lines1 = f.readlines()
            if len(file_lines1) == 0:
                return
            for line1 in file_lines1:
                self.proxy.add(line1.strip())

        for i in list(self.proxy):
            if '.' in i:
                self.proxylist.append({
                    'http': i,
                    'https':i,
                })
        return self.proxylist

    def getproxy(self,proxlist):
        try:
            if proxlist == None:
                return None
            elif len(proxlist) <= 1:
                return None
            if self.num>len(proxlist)-1:
                self.num=0
            nextproxy=proxlist[self.num]
            self.num+=1
        except Exception as e:
            #input(e)
            nextproxy=None
        return nextproxy