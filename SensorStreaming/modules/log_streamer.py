import time
import csv
from statistics import mean, median

def log_streamer(input_path, output_path, streamed_data, push_rates):

    if type(input_path) != str or type(output_path) != str or type(streamed_data) != dict or type(push_rates) != int:
        raise TypeError("Input Invalid")

    with open(input_path) as file:
        my_reader = csv.reader(file, delimiter=',')
        for i, row in enumerate(my_reader):
            if i != 0: #exclude column_name

                streamed_data[row[1]]["temperature"].append(float(row[2]))
                streamed_data[row[1]]["humidity"].append(float(row[3]))

            if (i) % 3 == 0 and i != 0:
                ra1_min_temp = min(streamed_data["roomArea1"]["temperature"])
                ra1_min_humid = min(streamed_data["roomArea1"]["humidity"])
                ra2_min_temp = min(streamed_data["roomArea2"]["temperature"])
                ra2_min_humid = min(streamed_data["roomArea2"]["humidity"])
                ra3_min_temp = min(streamed_data["roomArea3"]["temperature"])
                ra3_min_humid = min(streamed_data["roomArea3"]["humidity"])
           
                ra1_max_temp = max(streamed_data["roomArea1"]["temperature"])
                ra1_max_humid = max(streamed_data["roomArea1"]["humidity"])
                ra2_max_temp = max(streamed_data["roomArea2"]["temperature"])
                ra2_max_humid = max(streamed_data["roomArea2"]["humidity"])
                ra3_max_temp = max(streamed_data["roomArea3"]["temperature"])
                ra3_max_humid = max(streamed_data["roomArea3"]["humidity"])

                ra1_med_temp = median(streamed_data["roomArea1"]["temperature"])
                ra1_med_humid = median(streamed_data["roomArea1"]["humidity"])
                ra2_med_temp = median(streamed_data["roomArea2"]["temperature"])
                ra2_med_humid = median(streamed_data["roomArea2"]["humidity"])
                ra3_med_temp = median(streamed_data["roomArea3"]["temperature"])
                ra3_med_humid = median(streamed_data["roomArea3"]["humidity"])

                ra1_mean_temp = mean(streamed_data["roomArea1"]["temperature"])
                ra1_mean_humid = mean(streamed_data["roomArea1"]["humidity"])
                ra2_mean_temp = mean(streamed_data["roomArea2"]["temperature"])
                ra2_mean_humid = mean(streamed_data["roomArea2"]["humidity"])
                ra3_mean_temp = mean(streamed_data["roomArea3"]["temperature"])
                ra3_mean_humid = mean(streamed_data["roomArea3"]["humidity"])

                with open(output_path, 'a', encoding='UTF8', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow([ i/3, "roomArea1", ra1_min_temp, ra1_max_temp, ra1_med_temp, ra1_mean_temp,  ra1_min_humid, ra1_max_humid, ra1_med_humid, ra1_mean_humid])
                    writer.writerow([ i/3, "roomArea1", ra2_min_temp, ra2_max_temp, ra2_med_temp, ra2_mean_temp,  ra2_min_humid, ra2_max_humid, ra2_med_humid, ra2_mean_humid])
                    writer.writerow([ i/3, "roomArea1", ra3_min_temp, ra3_max_temp, ra3_med_temp, ra3_mean_temp,  ra3_min_humid, ra3_max_humid, ra3_med_humid, ra3_mean_humid])
                    
                    print("Log", int(i/3), "- Successfully stream data")

                time.sleep(push_rates)