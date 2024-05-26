import requests, json
from riotwatcher import TftWatcher

from .TFTUpdater import TFTUpdater

"""
TFT Roulette: Random TFT Strategy Generator

Returns:
    TFTRoulette Object: Service for generating random TFT strategies & updating data
"""
class TFTRoulette:
    
    
    def __init__(self, api_key, paths):
        
        self.tft_api = TftWatcher(api_key)
        self.updater = TFTUpdater(paths=paths)
        
        self.game_version = self.updater.game_version
        self.data_path = paths["data_path"]
        
        self.data = self.updater.get_all_file_paths() # Contains Routing for all TFT Data 
    
    
    
    #
    # Data
    #
    
    
    def get_files(self):
        """
        Get all TFT Data Files
        """
        self.updater.update()
        