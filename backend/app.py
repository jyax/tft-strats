import toml, os
from components.TFTRoulette import TFTRoulette
from components.TFTScheduler import TFTScheduler


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
    
    current_set = cfg["data"]["current_set"]
    game_version = cfg["data"]["game_version"]
    patch_version = cfg["data"]["patch_version"]
    
    tftr = TFTRoulette(paths=paths)
    tfts = TFTScheduler(paths=paths)
    
    game_version = tftr.game_version
    print(f"Current Game Version: {game_version}")
    
    data = tftr.get_current_data()
    # Add a check to see if current files are up-to-date
    #tftr.get_files()


if __name__ == "__main__":
    main()
    