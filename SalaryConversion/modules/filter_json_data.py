def filter_json_data(json):
    if type(json) != list:
        raise TypeError("Invalid JSON format.")
    
    temp = []
    unused_keys = {"website", "company"}
    for data in json:
        if type(data) != dict:
            raise TypeError("Invalid JSON format.")
        data = {key: data[key] for key in data if key not in unused_keys}
        temp.append(data)
    
    return temp        