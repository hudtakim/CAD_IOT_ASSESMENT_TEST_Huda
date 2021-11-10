import json

def save_json(json_var):
    if type(json_var) != list:
        raise TypeError("Invalid JSON format.")
    for data in json_var:
        if type(data) != dict:
            raise TypeError("Invalid JSON format.")

    with open('output/converted_salary_data.json', 'w') as json_file:
        json.dump(json_var, json_file)