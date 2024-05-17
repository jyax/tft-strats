import requests

def get_tft_json(version, file):
    """
    Generic Request function for TFT JSON data from DDragon

    Args:
        version (str): Current game version
        file (str): What file to fetch from DDragon
    
    Returns:
        dict: JSON data fetched from URL
    """
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_us/{file}.json"