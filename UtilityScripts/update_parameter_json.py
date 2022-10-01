import json
import os

parameter_file_path = os.path.join(os.path.abspath(__file__ + "/../../"), "RunParameters/parameters.json")

def update_json_parameters(key, value):

    with open(parameter_file_path, "r") as jsonfile:
        data = json.load(jsonfile)

    data[key] = value

    with open(parameter_file_path, "w") as jsonfile:
        json.dump(data, jsonfile)