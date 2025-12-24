import yaml
import os 





def load_config(file_path:str ="config\config.yaml"):

    with open(file_path,"r") as file:
        config=yaml.safe_load(file)
        print(config)
    return config