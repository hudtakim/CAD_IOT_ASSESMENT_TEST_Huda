from modules.stream_json_data import stream_json_data
from modules.stream_to_csv import stream_to_csv
from modules.make_csv import make_csv

if __name__ == '__main__':
    print("The program is running, press 'ctrl + C' to stop.")
    result = stream_json_data("data/sensor_data.json")  #stream data from sensor_data.json

    path = "output/streamed_data.csv" 
    col_list = ["log","RoomArea","Temperature", "Humidity"]
    make_csv(path, col_list)                                 # Make a csv file for the output
    stream_to_csv(json_data = result, path = path, push_rates=2*60, num_of_room=3) #store the data to csv each 2 minutes every 3 roomArea. (There are only 3 kind of roomArea in the data)
    
    print("Successfully stream all data to csv")  #execute if All data streamed succesfully.
