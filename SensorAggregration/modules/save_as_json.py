import json

def save_as_json(store_val):

    if type(store_val) != dict:
        raise TypeError("Store_val must be dictionary")

    with open('output/aggregated_sensor_data.json', 'w') as json_file:
        json.dump(store_val, json_file)
    
    print("aggregated_sensor_data.json successfully created")