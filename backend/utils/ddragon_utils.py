import requests, tarfile, json


headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

def get_tft_json(version, file):
    """
    Generic Request function for TFT JSON data from DDragon

    Args:
        version (str): Current game version
        file (str): What file to fetch from DDragon
    
    Returns:
        dict: JSON data fetched from URL
    """
    url = f"https://ddragon.leagueoflegends.com/cdn/{version}/data/en_US/{file}.json"
    response = requests.get(url)
    
    return response.json()
    
    
def get_latest_static_files(download_path, extract_path, version):
        """
        Pulls the latest static files from the Riot DataDragon CDN.

        Returns:
            dict: Latest static files
        """
        
        url = "https://ddragon.leagueoflegends.com/cdn/dragontail-{version}.tgz"
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        with open(download_path) as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
                
        print("Data saved to", download_path)
        
        with tarfile.open(download_path, "r:gz") as tar:
            tar.extractall(extract_path)
            
        print("Data saved to", extract_path)
        
        
        
if __name__ == "__main__":
    version = "14.10.1"
    print(get_tft_json(version, "tft-augments"))