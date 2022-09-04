import random
import requests
import json
import os
from tkinter import filedialog
import tkinter

class system():
    def __init__(self) -> None:
        pass

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