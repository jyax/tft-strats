import os
import requests, toml, json
from riotwatcher import TftWatcher


from utils.ddragon_utils import get_tft_json
import utils.cdragon_utils as cdu

import TFTUpdater as TFTUpdater

"""
TFT Roulette: Random TFT Strategy Generator

Returns:
    TFTRoulette Object: Service for generating random TFT strategies & updating data
"""
class TFTRoulette:
    
    
    def __init__(self, api_key, data_path):
        
        self.tft_api = TftWatcher(api_key)
        self.updater = TFTUpdater(data_path)
        
        self.game_version = self.updater.get_latest_game_version()
        self.data_path = data_path
        
        self.data = self.updater.get_all_names() # Contains Routing for all TFT Data
        
    
    #
    # Data
    #
    
    
        
#
# Main Function
#
             
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