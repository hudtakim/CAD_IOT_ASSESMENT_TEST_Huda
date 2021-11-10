def get_roomArea_and_day(sensor_data, timestamp_converter):
    if type(sensor_data) != list:
        raise TypeError("Invalid format for JSON")

    for data in sensor_data:
        if type(data) != dict:
            raise TypeError("Invalid format for JSON")

    #Define empty list to store day and roomArea for each data    
    day_list = []
    roomArea_list = []

    #get the day and roomArea of each data
    for data in sensor_data:
        day = timestamp_converter(data['timestamp'])
        day_list.append(day)
        roomArea_list.append(data['roomArea'])

    return day_list, roomArea_list

