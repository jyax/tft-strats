import requests, json

def get_region_data():
    """
    Obtains static file from CDragon that contains basic trait/character relationships
    """
    url =   "https://raw.communitydragon.org/latest/cdragon/tft/en_us.json"
    response = requests.get(url=url)
    return response.json()

def get_character_data():
    """
    Obtains static file from CDragon that contains character data
    """
    url = "https://raw.communitydragon.org/latest/game/data/tftteamplanner/characters.bin.json"
    response = requests.get(url=url)
    return response.json()