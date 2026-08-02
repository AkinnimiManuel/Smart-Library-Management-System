import json

#function for loading data
def load_data(file_path): 
    try: 
        with open(file_path, "r") as file:
            return json.load(file) 

    except FileNotFoundError:
        return []


#function for saving data
def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)