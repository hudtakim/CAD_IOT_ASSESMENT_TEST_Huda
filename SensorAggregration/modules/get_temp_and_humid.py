def get_temp_and_humid(sensor_data, store_val, roomArea_list, day_list):
    if type(sensor_data) != list:
        raise TypeError("Invalid format for JSON")

    
    if type(day_list) != list or type(roomArea_list) != list:
        raise TypeError("day and roomArea must be list.")

    #Store the value of temperature and humidity from each data to the dictionary
    for i, data in enumerate(sensor_data):
        store_val[roomArea_list[i] + "-" + day_list[i]]['temperature_list'].append(data['temperature'])
        store_val[roomArea_list[i] + "-" + day_list[i]]['humidity_list'].append(data['humidity'])

    return store_val