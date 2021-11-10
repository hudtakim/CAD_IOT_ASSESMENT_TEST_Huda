def set_val(store_val, day_set, roomArea_set):

    if type(store_val) != dict:
        raise TypeError("Store_val must be dictionary")
    
    if type(day_set) != set or type(roomArea_set) != set:
        raise TypeError("day and roomArea must be set.")


    for i in range(len(day_set) * len(roomArea_set)):
        for roomArea in roomArea_set:
            for day in day_set:
                store_val[roomArea + "-" + day]['temperature_list'].sort()
                sum_temperature = sum(store_val[roomArea + "-" + day]['temperature_list'])
                len_temperature = len(store_val[roomArea + "-" + day]['temperature_list'])
                sum_humidity = sum(store_val[roomArea + "-" + day]['humidity_list'])
                len_humidity = len(store_val[roomArea + "-" + day]['humidity_list'])

                store_val[roomArea + "-" + day].update({
                        'min_temperature': min(store_val[roomArea + "-" + day]['temperature_list']),
                        'max_temperature': max(store_val[roomArea + "-" + day]['temperature_list']),
                        'median_temperature': (store_val[roomArea + "-" + day]['temperature_list'][len(store_val[roomArea + "-" + day]['temperature_list']) // 2] + store_val[roomArea + "-" + day]['temperature_list'][~(len(store_val[roomArea + "-" + day]['temperature_list']) // 2)]) / 2,
                        'avarage_temperature': sum_temperature/len_temperature,

                        'min_humidity' : min(store_val[roomArea + "-" + day]['humidity_list']),
                        'max_humidity': max(store_val[roomArea + "-" + day]['humidity_list']),
                        'median_humidity': (store_val[roomArea + "-" + day]['humidity_list'][len(store_val[roomArea + "-" + day]['humidity_list']) // 2] + store_val[roomArea + "-" + day]['humidity_list'][~(len(store_val[roomArea + "-" + day]['humidity_list']) // 2)]) / 2,
                        'avarage_humidity': sum_humidity/len_humidity,
                })
    
    return store_val