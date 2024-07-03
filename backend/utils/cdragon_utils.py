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


class CDragonFileBrowser:
    def __init__():
        self.keywords = ["tft", "teamfighttactics", "team_fight_tactics", "teamfight_tactics"]
    
    
    def fetch_directory(dir_url):
        """
        Fetches a directory from CDragon and returns the JSON tree
        """
        response = requests.get(dir_url)
        response.raise_for_status()
        return response.json()
    
    def check_file_for_keywords(self, file_url):
        """
        Checks a file for keywords
        """
        response = requests.get(file_url)
        response.raise_for_status()
        file_data = response.json()
        for keyword in self.keywords:
            if keyword in file_data:
                return True
        return False