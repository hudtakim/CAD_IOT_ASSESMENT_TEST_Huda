import json

def read_json_data(path):
    if type(path) != str:
        raise TypeError("Path directory must be string.")

    f = open(path)
    data = json.load(f)
    f.close()

    return data["array"]