def remove_val(store_val, day_set, roomArea_set):

    if type(store_val) != dict:
        raise TypeError("Store_val must be dictionary")
    
    if type(day_set) != set or type(roomArea_set) != set:
        raise TypeError("day and roomArea must be set.")

    for i in range(len(day_set) * len(roomArea_set)):
        for roomArea in roomArea_set:
            for day in day_set:
                store_val[roomArea + "-" + day].pop('temperature_list', None)
                store_val[roomArea + "-" + day].pop('humidity_list', None)
    
    return store_val