import json, requests, os

from utils.ddragon_utils import get_tft_json, get_latest_static_files
import utils.cdragon_utils as cdu

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

class TFTUpdater:
    """
    Class to update TFT data.
    """
    
    def __init__(self, paths):
        """
        Initializes the TFTUpdater class.
        """
        
        
        self.data_path = paths["data_path"]
        self.download_path = paths["download_path"]
        self.extract_path = paths["extract_path"]
        
        self.game_version = self.get_latest_game_version()
        self.file_names = self.get_all_names()


    def update(self):
        """
        Updates TFT data.
        """
        
        # Get the latest static files
        #static_files = get_latest_static_files(game_version)

        files = ['tft-augments', 'tft-champion', 'tft-item', 'tft-region-portals', 'tft-trait', 
                 'tft-arena', 'tft-hero-augments', 'tft-queues', 'tft-regalia', 'tft-tactician']
        
        for file in files:
            print(f"Updating {file} for version {self.game_version}")
            self.save_json_data(get_tft_json(self.game_version, file), self.data_path + "jsons/" + file + '.json')
        
        # Save the latest static files
        #for file_name, file_data in static_files.items():
        #    self.save_json_data(file_data, f"{self.data_path}/{file_name}.json")


    def get_latest_game_version(self):
        """
        Pulls the latest game version from the Riot API.

        Returns:
            str: Current game version
        """
        
        url = "https://ddragon.leagueoflegends.com/api/versions.json"
        response = requests.get(url, headers=headers)
        return response.json()[0]
        
        
    def get_file_data(self, data_type, file_name):
        """
        Gets the JSON data for a specific TFT data type from the Riot CDN.

        Args:
            data_type (str): Type of TFT data to fetch

        Returns:
            dict: JSON data fetched from URL
        """

        with open("{self.data_path}/{data_type}/{file_name}.json") as f:
            return json.load(f)
        
        
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
        
        
    def get_all_names(self):
        """
        Gets all TFT data types from current saved data.

        Returns:
            dict: JSON data fetched from current data.
        """
        file_names = {}
        for root, dirs, files in os.walk(self.data_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                file_names[file_name] = file_path
        return file_names
    