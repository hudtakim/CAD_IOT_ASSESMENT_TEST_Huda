import csv

def make_csv(path, col_list):
    if type(path) != str or type(col_list) != list: 
        raise TypeError("Invalid input")

    f = open(path, 'w', encoding='UTF8', newline='')
    writer = csv.writer(f)
    writer.writerow(col_list)
    return writer