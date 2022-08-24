from modules import data
import requests

links=data.links()

session=requests.session()
class checkers:
    def get_inventory(self, user_info,region_id,username,token,types=links.INVENTORY_TYPES):
        champion_data_builder = data.ChampionData()
        champion_data = champion_data_builder.get_champion_data()

        query = {
            "puuid": user_info["sub"],
            "location": links.LOCATION_PARAMETERS[region_id],
            "accountId": user_info["pvpnet_account_id"],
        }
        query_string = "&".join(
            [f"{k}={v}" for k, v in query.items()]
            + [f"inventoryTypes={t}" for t in types]
        )
        HEADERS= {
                    'User-Agent': 'RiotClient/51.0.0.4429735.4381201 rso-auth (Windows;10;;Professional, x64)',
                    'Authorization': f'Bearer {token}'
                }
        response = session.get(
            url=links.INVENTORY_URL.format(region_id=region_id) + query_string,headers=HEADERS
        )

        try:
            result = response.json()["data"]["items"]
        except:
            print(f"Failed to get inventory data on {username}")
            print(f"Response: {response.json()}")
            return {"CHAMPION": [], "CHAMPION_SKINS": []}

        result["CHAMPION"] = [
            champion_data["champions"][str(id)] for id in result["CHAMPION"]
        ]
        result["CHAMPION_SKIN"] = [
            champion_data["skins"][str(id)] for id in result["CHAMPION_SKIN"]
        ]

        return result