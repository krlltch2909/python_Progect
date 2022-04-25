import json


def get_data_from_json(name):
    try:
        with open(name, 'r') as file:
            base = json.load(file)
    except:
        base = ""
    return base
