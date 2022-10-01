import json
import os

parameter_file_path = os.path.join(os.path.abspath(__file__ + "/../../"), "RunParameters/parameters.json")

def get_server_value_from_parameter_file():

    with open(parameter_file_path) as jsonfile:
        data = json.load(jsonfile)
        return data["server"]