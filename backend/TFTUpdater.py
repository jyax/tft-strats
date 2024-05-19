import json, requests, os


class TFTUpdater:
    """
    Class to update TFT data.
    """
    
    def __init__(self, data_path):
        """
        Initializes the TFTUpdater class.
        """
        
        self.data_path = data_path


    def get_latest_game_version(self):
            """
            Pulls the latest game version from the Riot API.

            Returns:
                str: Current game version
            """
            
            url = "https://ddragon.leagueoflegends.com/api/versions.json"
            response = requests.get(url)
            return response.json()[0]
        
        
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