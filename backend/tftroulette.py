import os
import requests, toml, json
from riotwatcher import TftWatcher

from utils.ddragon_utils import get_tft_json


"""
TFT Roulette: Random TFT Strategy Generator

Returns:
    TFTRoulette Object: Service for generating random TFT strategies & updating data
"""
class TFTRoulette:
    
    
    def __init__(self, api_key, data_path):
        
        self.tft = TftWatcher(api_key)
        self.game_version = self.get_latest_game_version()
        self.data_path = data_path
        
        self.data = self.get_all_names() # Contains Routing for all TFT Data
        
        
    def get_latest_game_version(self):
        """
        Pulls the latest game version from the Riot API.

        Returns:
            str: Current game version
        """
        
        url = "https://ddragon.leagueoflegends.com/api/versions.json"
        response = requests.get(url)
        return response.json()[0]
    
    
    
    #
    # Data
    #
    
    def get_file_data(self, data_path, data_type, file_name):
        """
        Gets the JSON data for a specific TFT data type from the Riot CDN.

        Args:
            data_type (str): Type of TFT data to fetch

        Returns:
            dict: JSON data fetched from URL
        """

        with open("{data_path}/{data_type}/{file_name}.json") as f:
            return json.load(f)
        
        
    def get_all_names(self, data_path):
        """
        Gets all TFT data types from current saved data.

        Returns:
            dict: JSON data fetched from current data.
        """
        
        
        return file_names
    
    
    def save_json_data(self, data, filename):
        """
        Saves JSON data to a file.

        Args:
            data (dict): JSON data being saved.
            filename (str): Path of file to save data within.
        """
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved to", filename)
        
def main():
    """
    Main function for API call testing.
    """
    
    data_path = "./backend/data/"
    cfg = toml.load("config.toml")
    riot_api_key = cfg["api"]["riot_api_key"]
    
    tftr = TFTRoulette(api_key=riot_api_key, data_path=data_path)
    
    version = tftr.game_version
    print("Current Game Version: {version}")
    
    files = ['tft-augments', 'tft-champions', 'tft-items', 'tft-region-portals', 'tft-traits']
    for file in files:
        tftr.save_json_data(get_tft_json(version, file), data_path + "jsons/" + file + '.json')
        
if __name__ == "__main__":
    main()