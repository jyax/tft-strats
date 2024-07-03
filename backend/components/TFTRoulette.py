import requests, json

from backend.components.TFTUpdater import TFTUpdater

"""so
TFT Roulette: Random TFT Strategy Generator

Returns:
    TFTRoulette Object: Service for generating random TFT strategies & updating data
"""
class TFTRoulette:
    
    
    def __init__(self, paths):
        
        self.updater = TFTUpdater(paths=paths)
        
        self.game_version = self.updater.game_version
        self.data_path = paths["data_path"]
        self.current_set = None
        
        self.data = self.updater.get_all_file_paths() # Contains Routing for all TFT Data 
    
    
    
    #
    # Data
    #
    
    
    def update(self): self.updater.update()    
        
        

    #
    # Randomized Strategy Generation
    #
    
    def get_current_data(self):
        """
        Get Current TFT Data
        """
        with open(self.data["en_us"], "r") as f:
            data = json.load(f)
            
        items = data["items"]
        set_data = data["setData"]
        current_set = -1
        for selected_set in set_data:
            if selected_set["number"] > current_set:
                current_set = selected_set["number"]
                
        self.current_set = current_set

        current_set_data = [selected_set for selected_set in set_data if selected_set["number"] == current_set]
        
        
        champions = {
            1: {},
            2: {},
            3: {},
            4: {},
            5: {}
        }
        for selected_champion in current_set_data[0]["champions"]:
            if len(selected_champion["traits"]) == 0:
                continue
            champions[selected_champion["cost"]][selected_champion["name"]] = selected_champion
            
        champions_by_trait = {}
        for selected_champion in current_set_data[0]["champions"]:
            for selected_trait in selected_champion["traits"]:
                if selected_trait not in champions_by_trait.keys():
                    champions_by_trait[selected_trait] = {}
                champions_by_trait[selected_trait][selected_champion["name"]] = selected_champion
            
        traits = {}
        for selected_trait in current_set_data[0]["traits"]:
            traits[selected_trait["name"]] = selected_trait
            
        
        x = 0
        
        

        