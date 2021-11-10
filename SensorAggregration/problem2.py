from modules.read_json_data import read_json_data
from modules.convert_timestamp import convert_timestamp_to_day
from modules.get_roomArea_and_day import get_roomArea_and_day
from modules.make_dict import make_dict
from modules.get_temp_and_humid import get_temp_and_humid
from modules.set_val import set_val
from modules.remove_val import remove_val
from modules.save_as_json import save_as_json

if __name__ == '__main__':
    sensor_data = read_json_data("data/sensor_data.json")  #read json data

    #Get roomArea and day for each data   
    day_list, roomArea_list = get_roomArea_and_day(sensor_data, convert_timestamp_to_day)

    #Prepare a Dictionary to store temperature and humidity for each aggregated data by room Area and day 
    store_val = make_dict(day_list, roomArea_list)

    #Store the value of temperature and humidity from each data to the dictionary
    store_val = get_temp_and_humid(sensor_data, store_val, roomArea_list, day_list)

    #count the min, max, median, and avarage, then store them to the dictionary
    store_val = set_val(store_val, day_set= set(day_list), roomArea_set = set(roomArea_list))

    #Remove temperature_list and humidity_list from dictionary
    store_val = remove_val(store_val, day_set= set(day_list), roomArea_set = set(roomArea_list))

    #Export json file from the dictionary (The file consist of min, max, median, avarage 
    # of temperature and humidity for each roomArea for certain day)
    save_as_json(store_val)

    print("Sensor Aggregation Success!!!")
            




        
        

    

    
