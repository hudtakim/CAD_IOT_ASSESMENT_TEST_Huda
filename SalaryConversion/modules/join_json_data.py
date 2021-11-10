def join_json_data(json1, json2):
    if type(json1) != list or type(json2) != list:
        raise TypeError("Invalid format for JSON")

    for data1 in json1:
        if type(data1) != dict:
            raise TypeError("Invalid format for JSON1")
        for data2 in json2:
            if type(data2) != dict:
                raise TypeError("Invalid format for JSON2")
            if data1['id'] == data2['id']:
                data1.update(data2)
                break

    return json1