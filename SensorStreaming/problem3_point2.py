from modules.make_csv import make_csv
from modules.log_streamer import log_streamer
from modules.create_storer import create_storer

if __name__ == '__main__':
    print("Program is running, press 'ctrl + C' to stop.") 

    input_path = "output/streamed_data.csv"
    output_path = "output/streamed_log.csv"
    
    col_list = ["log", "roomArea", "min_temp", "max_temp", "median_temp", "avg_temp", "min_humid", "max_humid", "median_humid", "avg_humid"]
    make_csv(output_path, col_list) # Make a csv file for the output

    data_storer = create_storer() #Create a dictionary to store data (min, max, median, avarage)

    log_streamer(input_path, output_path, streamed_data = data_storer, push_rates= 15*60) #store the data to csv each 15 minutes every 3 roomArea.
        
    print("Stream data complete, The data successfully saved at: '" + output_path + "'") #execute if All data streamed succesfully.

       

