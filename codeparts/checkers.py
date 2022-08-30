from codeparts import data,auth
import requests
import concurrent.futures
from ssl import PROTOCOL_TLSv1_2
from urllib3 import PoolManager
from requests.adapters import HTTPAdapter

links=data.links()

class TLSAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize, block=block,
                                       ssl_version=PROTOCOL_TLSv1_2)

session=requests.session()
session.mount('https://', TLSAdapter())

class ChampionData:
    def __init__(self):
        game_version = requests.get(links.VERSION_URL).json()
        self.game_version = game_version[0]

    def build_champion_data(self):
        champion_ids = requests.get(
            links.CHAMPION_IDS_URL.format(game_version=self.game_version)
        ).json()
        champion_data_builder = {
            "champions": {
                int(value["key"]): champion_name
                for (champion_name, value) in champion_ids["data"].items()
            }
        }
        champion_data_builder["version"] = self.game_version
        champion_data_builder["skins"] = {}

        champion_urls = [
            links.CHAMPION_DATA_URL + str(champion_id) + "/data"
            for champion_id in champion_data_builder["champions"].keys()
        ]

        def load_url(url):
            champion_data = requests.get(url)
            return champion_data

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_url = (executor.submit(load_url, url) for url in champion_urls)
            for future in concurrent.futures.as_completed(future_to_url):
                data = future.result().json()
                for skin in data["skins"]:
                    champion_data_builder["skins"][skin["id"]] = skin["name"]
                    if "chromas" in skin:
                        for chroma in skin["chromas"]:
                            champion_data_builder["skins"][chroma["id"]] = (
                                chroma["name"] + " (Chroma)"
                            )

        return champion_data_builder

class checkers:
    def balance(self,token,region_id):
        try:
            HEADERS= {
                        'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
                        'Authorization': f'Bearer {token}'
                    }
            response = session.get(
                links.STORE_URL.format(
                    store_front_id=links.STORE_FRONTS[region_id]
                ),headers=HEADERS
            ).json()
            rp=response['player']['rp']
            be=response['player']['ip']
        except:
            rp='N/A'
            be='N/A'
        return rp,be


    def get_inventory(self, token, sub,region_id,types=data.links.INVENTORY_TYPES):
        print(region_id)
        input()
        HEADERS= {
                    'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
                    'Authorization': f'Bearer {token}'
                }
        champion_data_builder = ChampionData()
        champion_data = champion_data_builder.build_champion_data()

        query = {
            "puuid": sub,
            "location": links.LOCATION_PARAMETERS[region_id.upper()],
            "accountId": auth.auth.getuserinfo(auth,token)["pvpnet_account_id"],
        }
        query_string = "&".join(
            [f"{k}={v}" for k, v in query.items()]
            + [f"inventoryTypes={t}" for t in types]
        )
        print(query_string)
        input()

        response = session.get(
            url=links.INVENTORY_URL.format(region_id=region_id) + query_string,
            headers=HEADERS
        )
        print(response)
        input()

        try:
            result = response.json()["data"]["items"]
        except:
            return {"CHAMPION": [], "CHAMPION_SKINS": []}

        result["CHAMPION"] = [
            champion_data["champions"][str(id)] for id in result["CHAMPION"]
        ]
        result["CHAMPION_SKIN"] = [
            champion_data["skins"][str(id)] for id in result["CHAMPION_SKIN"]
        ]

        return result