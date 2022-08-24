import requests

class links:
    AUTH_URL = "https://auth.riotgames.com/api/v1/authorization"
    INFO_URL = "https://auth.riotgames.com/userinfo"
    INVENTORY_URL = "https://{region_id}.cap.riotgames.com/lolinventoryservice/v2/inventories/simple?"
    DETAILED_INVENTORY_URL = "https://{region_id}.cap.riotgames.com/lolinventoryservice/v2/inventoriesWithLoyalty?"
    STORE_URL = "https://{store_front_id}.store.leagueoflegends.com/storefront/v3/view/misc?language=en_US"
    HISTORY_URL = "https://{store_front_id}.store.leagueoflegends.com/storefront/v3/history/purchase"
    MATCHES_URL = "https://acs.leagueoflegends.com/v1/stats/player_history/auth?begIndex=0&endIndex=1"

    # bl1tzgg rank checking endpoint
    RANK_URL = "https://riot.iesdev.com/graphql?query=query%20LeagueProfile%28%24summoner_name%3AString%2C%24summoner_id%3AString%2C%24account_id%3AString%2C%24region%3ARegion%21%2C%24puuid%3AString%29%7BleagueProfile%28summoner_name%3A%24summoner_name%2Csummoner_id%3A%24summoner_id%2Caccount_id%3A%24account_id%2Cregion%3A%24region%2Cpuuid%3A%24puuid%29%7BaccountId%20latestRanks%7Bqueue%20tier%20rank%20leaguePoints%7D%7D%7D&variables=%7B%22summoner_name%22%3A%22{summoner_name}%22%2C%22region%22%3A%22{region_id}%22%7D"

    # bl1tzgg matches checking endpoint
    NEW_MATCHES_URL = "https://league-player.iesdev.com/graphql?query=query%20matches%28%0A%20%20%24region%3A%20Region%21%0A%20%20%24accountId%3A%20String%21%0A%20%20%24first%3A%20Int%0A%20%20%24role%3A%20Role%0A%20%20%24queue%3A%20Queue%0A%20%20%24championId%3A%20Int%0A%20%20%24riotSeasonId%3A%20Int%0A%20%20%24maxMatchAge%3A%20Int%0A%29%20%7B%0A%20%20matches%28%0A%20%20%20%20region%3A%20%24region%0A%20%20%20%20accountId%3A%20%24accountId%0A%20%20%20%20first%3A%20%24first%0A%20%20%20%20role%3A%20%24role%0A%20%20%20%20queue%3A%20%24queue%0A%20%20%20%20championId%3A%20%24championId%0A%20%20%20%20riotSeasonId%3A%20%24riotSeasonId%0A%20%20%20%20maxMatchAge%3A%20%24maxMatchAge%0A%20%20%29%20%7B%0A%20%20%20%20id%0A%20%20%20%20gameCreation%0A%20%20%7D%0A%7D&variables=%7B%22maxMatchAge%22%3A300%2C%22first%22%3A1%2C%22region%22%3A%22{region_id}%22%2C%22accountId%22%3A%22{account_id}%22%7D"

    CHAMPION_DATA_URL = "https://cdn.communitydragon.org/latest/champion/"
    CHAMPION_IDS_URL = (
        "http://ddragon.leagueoflegends.com/cdn/{game_version}/data/en_US/champion.json"
    )

    VERSION_URL = "https://ddragon.leagueoflegends.com/api/versions.json"

    INVENTORY_TYPES = [
        "TOURNAMENT_TROPHY",
        "TOURNAMENT_FLAG",
        "TOURNAMENT_FRAME",
        "TOURNAMENT_LOGO",
        "GEAR",
        "SKIN_UPGRADE_RECALL",
        "SPELL_BOOK_PAGE",
        "BOOST",
        "BUNDLES",
        "CHAMPION",
        "CHAMPION_SKIN",
        "EMOTE",
        "GIFT",
        "HEXTECH_CRAFTING",
        "MYSTERY",
        "RUNE",
        "STATSTONE",
        "SUMMONER_CUSTOMIZATION",
        "SUMMONER_ICON",
        "TEAM_SKIN_PURCHASE",
        "TRANSFER",
        "COMPANION",
        "TFT_MAP_SKIN",
        "WARD_SKIN",
        "AUGMENT_SLOT",
    ]

    LOCATION_PARAMETERS = {
        "BR1": "lolriot.mia1.br1",
        "EUN1": "lolriot.euc1.eun1",
        "EUW1": "lolriot.ams1.euw1",
        "JP1": "lolriot.nrt1.jp1",
        "LA1": "lolriot.mia1.la1",
        "LA2": "lolriot.mia1.la2",
        "NA1": "lolriot.pdx2.na1",
        "OC1": "lolriot.pdx1.oc1",
        "RU": "lolriot.euc1.ru",
        "TR1": "lolriot.euc1.tr1",
    }

    STORE_FRONTS = {
        "BR1": "br",
        "EUN1": "eun",
        "EUW1": "euw",
        "JP1": "jp",
        "LA1": "la1",
        "LA2": "la2",
        "NA1": "na",
        "OC1": "oc",
        "RU": "ru",
        "TR1": "tr",
    }

class ChampionData:
    def __init__(self):
        game_version = requests.get(links.VERSION_URL).json()
        self.game_version = game_version[0]