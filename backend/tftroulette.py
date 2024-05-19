import os
import requests, toml, json
from riotwatcher import TftWatcher

from TFTUpdater import TFTUpdater

"""
TFT Roulette: Random TFT Strategy Generator

Returns:
    TFTRoulette Object: Service for generating random TFT strategies & updating data
"""
class TFTRoulette:
    
    
    def __init__(self, api_key, paths):
        
        self.tft_api = TftWatcher(api_key)
        self.updater = TFTUpdater(paths=paths)
        
        self.game_version = self.updater.get_latest_game_version()
        self.data_path = paths["data_path"]
        
        self.data = self.updater.get_all_names() # Contains Routing for all TFT Data
        
    
    #
    # Data
    #
    
    def get_files(self):
        """
        Get all TFT Data Files
        """
        self.updater.update()
    
    def get_latest_version(self):
        """
        Get the latest game version
        """
        return self.updater.get_latest_game_version()
    
    
        
#
# Main Function
#

def main():
    """
    Main function for API call testing.
    """
    
    data_path = "./backend/data/"
    download_path = data_path + "tars/"
    extract_path = data_path + "source_files/"
    paths = {
        "download_path": download_path,
        "extract_path": extract_path,
        "data_path": data_path
        }
    
    cfg = toml.load("config.toml")
    riot_api_key = cfg["api"]["riot_api_key"]
    
    
    tftr = TFTRoulette(api_key=riot_api_key, paths=paths)
    
    version = tftr.get_latest_version()
    print(f"Current Game Version: {version}")
    
    tftr.get_files()
        
if __name__ == "__main__":
    main()