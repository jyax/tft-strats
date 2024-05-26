import toml, os
from components.TFTRoulette import TFTRoulette

# Load Config



def main():
    """
    Main function for API call testing.
    """
    
    data_path = "./data/"
    download_path = data_path + "tars/"
    extract_path = data_path + "source_files/"
    paths = {
        "download_path": download_path,
        "extract_path": extract_path,
        "data_path": data_path
        }
    
    cfg = toml.load("./config.toml")
    riot_api_key = cfg["api"]["riot_api_key"]
    
    tftr = TFTRoulette(api_key=riot_api_key, paths=paths)
    
    game_version = tftr.game_version
    print(f"Current Game Version: {game_version}")
    
    tftr.get_files()

if __name__ == "__main__":
    main()