from modules.fetch_json_data import fetch_json_data
from modules.read_json_data import read_json_data
from modules.join_json_data import join_json_data
from modules.currency_converter import convertIDRToUSD, get_IDR_currency
from modules.filter_json_data import filter_json_data
from modules.save_json import save_json

if __name__ == '__main__':
    fetched_data = fetch_json_data("http://jsonplaceholder.typicode.com/users") #fetch json from url
    salary_data = read_json_data("data/salary_data.json") #read json from local directory
    joined_data = join_json_data(fetched_data, salary_data) #join json_data with salary json

    IDR_currency = get_IDR_currency()

    for data in joined_data:
        data["salaryInUSD"] = convertIDRToUSD(data["salaryInIDR"], IDR_currency)   #Add new field (salaryInUSD) for each data

    filtered_data = filter_json_data(joined_data)  #filter_data

    save_json(filtered_data) #save final result of json file

    print("Salary Conversion Success!!!")