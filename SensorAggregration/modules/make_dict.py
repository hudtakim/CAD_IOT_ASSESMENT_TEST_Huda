def make_dict(day_list, roomArea_list):
    if type(day_list) != list or type(roomArea_list) != list:
        raise TypeError("day and roomArea must be list.")

    day_set = set(day_list)
    roomArea_set = set(roomArea_list)
    store_val = {}

    #Prepare a Dictionary to store temperature and humidity for each aggregated data by room Area and day 
    for i in range(len(day_set) * len(roomArea_set)):
        for roomArea in roomArea_set:
            for day in day_set:
                store_val.update({
                    roomArea + "-" + day: {
                        'temperature_list' : [],
                        'humidity_list' : [],
                    }
                })
    
    return store_val