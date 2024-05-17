import os
import requests, toml, json
from riotwatcher import TftWatcher


"""
TFT Roulette: Random TFT Strategy Generator

Returns:
    TFTRoulette Object: Service for generating random TFT strategies & updating data
"""
class TFTRoulette:
    
    def __init__(self, api_key):
        self.tft = TftWatcher(api_key)
        
        
        
        
def main():
    """
    Main function for API call testing.
    """
    cfg = toml.load("config.toml")
    riot_api_key = cfg["api"]["riot_api_key"]
    tftr = TFTRoulette(riot_api_key)
        
if __name__ == "__main__":
    main()