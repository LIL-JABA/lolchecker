from modules import data
import requests

links=data.links()

session=requests.session()
class checkers:
    def balance(self,token,region_id):
        try:
            HEADERS= {
                        'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
                        'Authorization': f'Bearer {token}'
                    }
            response = session.get(
                data.links.STORE_URL.format(
                    store_front_id=data.links.STORE_FRONTS[region_id]
                ),headers=HEADERS
            ).json()
            rp=response['player']['rp']
            be=response['player']['ip']
        except:
            rp='N/A'
            be='N/A'
        return rp,be