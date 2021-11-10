import json_stream

def stream_json_data(path):
    if type(path) != str:
        raise TypeError("Path directory must be string.")

    f = open(path)
    data = json_stream.load(f)

    return data["array"]