import time
import csv
 
def stream_to_csv(json_data, path, push_rates, num_of_room):
    if type(path) != str or type(push_rates) != int or type(num_of_room) != int:
        raise TypeError("Invalid input")

    log = 0 
    
    for i, data in enumerate(json_data):
        temperature = data["temperature"]
        humidity = data["humidity"]
        roomArea = data["roomArea"]

        with open(path, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([ log+1, roomArea, temperature, humidity])

        if (i+1) % num_of_room == 0:
            print("Log", log+1, "Successfully stream data")
            time.sleep(push_rates)
            log += 1
        