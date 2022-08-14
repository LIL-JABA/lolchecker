from modules import auth,checkers,systems
import traceback
import os
import ctypes
from colorama import Fore,Style
import datetime
check=checkers.checkers()
sys=systems.system()

class Checker:
    def __init__(self) -> None:
        self.err=0
        self.count=0
        self.valid=0
        self.checked=0
        self.banned=0
        self.bad=[0,1,3,4]

    def checker(self,accounts,count) -> None:
        self.count=count
        os.system(f'mode con: cols=60 lines=40')
        for account in accounts:
            ctypes.windll.kernel32.SetConsoleTitleW(f'LoLChecker by liljaba1337 | Checked {self.checked}/{count}')
            os.system('cls')
            print(f'''
    {sys.center('https://github.com/LIL-JABA/lolchecker')}
    {sys.center(f'checking {account}')}
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    >                   checked              >[{Fore.YELLOW}{self.checked}/{count}{Style.RESET_ALL}]<
    >                   valid                >[{Fore.GREEN}{self.valid}{Style.RESET_ALL}]<
    >                   banned               >[{Fore.LIGHTRED_EX}{self.banned}{Style.RESET_ALL}]<
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    >                   errors               >[{Fore.LIGHTRED_EX}{self.err}{Style.RESET_ALL}]<
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            ''')
            try:
                login=account.split(':')[0]
                password=account.split(':')[1]
                ath=auth.auth(login,password)
                token,ent,puuid,unverifmail=ath.auth()
                if token in self.bad:
                    if token==4:
                        self.banned+=1
                    self.checked+=1
                    continue
                self.user_info=ath.uinfo(token)
                self.region_id = self.user_info["region"]["id"]
                self.region_tag = self.user_info["region"]["tag"]
                self.summoner_name = self.user_info["lol_account"]["summoner_name"]
                self.valid+=1
                with open (f'output\\valid.txt', 'a', encoding='UTF-8') as file:
                    file.write(account)

                #inventory=check.get_inventory(self.user_info,self.region_id,login,token)
                #print(inventory)
            except Exception as e:
                with open('log.txt','a') as f:
                    f.write(f'({datetime.datetime.now()}) {str(traceback.format_exc())}\n_________________________________\n')
                self.err+=1
                #print(e)
            self.checked+=1

        os.system('cls')
        if self.err>0:
            print(f'checker has caught {self.err} errors.\nplease send the log.txt file to me (link in my github) so i will be able to improve the checker')
        print(f'''
    {sys.center('https://github.com/LIL-JABA/lolchecker')}
    {sys.center('F I N I S H E D')}
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    >                   checked              >[{Fore.YELLOW}{self.checked}/{count}{Style.RESET_ALL}]<
    >                   valid                >[{Fore.GREEN}{self.valid}{Style.RESET_ALL}]<
    >                   banned               >[{Fore.LIGHTRED_EX}{self.banned}{Style.RESET_ALL}]<
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    >                   errors               >[{Fore.LIGHTRED_EX}{self.err}{Style.RESET_ALL}]<
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            ''')