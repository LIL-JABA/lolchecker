import asyncio
import sys
from collections import OrderedDict
from ssl import PROTOCOL_TLSv1_2
from tkinter import *

import requests
from requests.adapters import HTTPAdapter
from urllib3 import PoolManager

from codeparts.data import links
from codeparts.riot_auth import *


class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block,
                                       ssl_version=PROTOCOL_TLSv1_2)


class auth:
    def __init__(self, login, password) -> None:
        self.session = requests.session()
        # self.session.mount('https://', TLSAdapter())
        self.useragent = OrderedDict({
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "application/json, text/plain, */*",
            'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)'
        })
        # self.authdata={
        #     "client_id": "riot-client",
        #     "nonce": "1",
        #     "redirect_uri": "http://localhost/redirect",
        #     "response_type": "token id_token",
        #     "scope": "openid lol ban profile email phone",
        # }

        # self.login_data = {
        #     "language": "en_US",
        #     "password": password,
        #     "remember": "true",
        #     "type": "auth",
        #     "username": login,
        # }
        self.login = login
        self.password = password

    def auth(self, proxy):
        # self.session.post(links.AUTH_URL,headers=self.useragent,json=self.authdata,proxies=proxy)
        # response=self.session.put(url=links.AUTH_URL,headers=self.useragent,json=self.login_data,proxies=proxy)
        # data=response.json()
        # if "access_token" in response.text:
        #    pattern = compile(
        #        'access_token=((?:[a-zA-Z]|\d|\.|-|_)*).*id_token=((?:[a-zA-Z]|\d|\.|-|_)*).*expires_in=(\d*)')
        #    data = pattern.findall(data['response']['parameters']['uri'])[0]
        #    token = data[0]
        # elif "auth_failure" in response.text:
        #     return 0,0,0,0
        # elif 'rate_limited' in response.text:
        #     return 1,1,1,1
        # elif 'multifactor' in response.text:
        #     return 3,3,3,3
        # elif 'rate_limited' in response.text:
        #     return 9,9,9,9
        if sys.platform == "win32":
            asyncio.set_event_loop_policy(
                asyncio.WindowsSelectorEventLoopPolicy())

        auth = RiotAuth()
        try:
            asyncio.run(auth.authorize(self.login, self.password))
        except RiotMultifactorError:
            return 3, 3, 3, 3
        except RiotRatelimitError:
            return 1, 1, 1, 1
        except RiotAuthError:
            return 0, 0, 0, 0
        token = auth.access_token
        entitlement = auth.entitlements_token
        self.data = auth.data2

        # headers = {
        #     'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
        #     'Authorization': f'Bearer {token}'
        # }
        # r=self.session.post('https://entitlements.auth.riotgames.com/api/token/v1', headers=headers, json={},proxies=proxy)
        # entitlement = r.json()['entitlements_token']
        # r = self.session.post('https://auth.riotgames.com/userinfo', headers=headers, json={},proxies=proxy)
        # data = r.json()
        puuid = self.data['sub']
        data2 = self.data['ban']
        data3 = data2['restrictions']
        for x in data3:
            typebanned = x['type']
        try:
            if typebanned == "PERMANENT_BAN" or typebanned == 'PERMA_BAN' or typebanned == 'TIME_BAN' or typebanned or typebanned == 'LEGACY_BAN':
                return 4, 4, 4, 4
            else:
                pass
        except:
            pass
        try:
            mailverif = bool(self.data['email_verified'])
        except:
            mailverif = True
        if mailverif == True:
            mailverif = False
        else:
            mailverif = True

        return token, entitlement, puuid, mailverif

    def get_region(self, token, proxy):
        try:
            # HEADERS= {
            #             'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
            #             'Authorization': f'Bearer {token}'
            #         }
            # uinfo=self.session.post(url=links.INFO_URL,headers=HEADERS,proxies=proxy).json()
            self.region_id = self.data["region"]["id"]
            self.formatter_region = self.region_id.replace(
                '1', '').replace('2', '').upper()
            self.region_tag = self.data["region"]["tag"]
        except:
            self.region_id = None
            self.formatter_region = 'N/A'
        try:
            self.level = self.data["lol_account"]["summoner_level"]
        except:
            self.level = 'N/A'
        return self.formatter_region, self.level, self.region_id

    @staticmethod
    def getuserinfo(self, token):
        uinfosession = requests.session()
        uinfosession.mount('https://', TLSAdapter())
        HEADERS = {
            'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
            'Authorization': f'Bearer {token}'
        }
        return uinfosession.post(url=links.INFO_URL, headers=HEADERS).json()
