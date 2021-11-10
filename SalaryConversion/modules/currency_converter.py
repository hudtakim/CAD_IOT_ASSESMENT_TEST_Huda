import requests

def get_IDR_currency():
    try:
        url = "https://v6.exchangerate-api.com/v6/ec74c4d96bf960e4ee817c0e/latest/USD"
        response = requests.get(url)
        data = response.json()
        IDR_currency = data['conversion_rates']['IDR']
        
        return IDR_currency
        
    except Exception as e:
        print("api url for currency converter error!!!")
        exit()

def convertIDRToUSD(salaryInIDR, IDR_currency):
    if type(salaryInIDR) not in [int, float] or type(IDR_currency) not in [int, float]:
        raise TypeError("Both input must be integer or float.")

    if (salaryInIDR < 0) or (IDR_currency < 0):
        raise ValueError("Both input can not be negative")

    return salaryInIDR / IDR_currency

    
                