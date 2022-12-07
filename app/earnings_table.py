import json
from pprint import pprint


import requests
from dotenv import load_dotenv

from app.alpha import API_KEY


def fetch_annual_earnings_data():
        symbol = input("Input company symbol: ")

        request_url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}"
        
        response = requests.get(request_url)
        
        parsed_response = json.loads(response.text)

        return parsed_response["annualEarnings"]

def fetch_quarterly_earnings_data():
        symbol = input("Input company symbol: ")

        request_url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}"
        
        response = requests.get(request_url)
        
        parsed_response = json.loads(response.text)

        return parsed_response["quarterlyEarnings"]

if __name__ == "__main__":

        data_selected = input("Would you like to look at annual data or quarterly data?: ") or "annual"

        annual = "annualEarnings"
        quarterly = "quarterlyEarnings"

        if data_selected == "annual":
                data = fetch_annual_earnings_data()
        elif data_selected == "quarterly": 
                data = fetch_quarterly_earnings_data

        data = fetch_annual_earnings_data()
        new_data = pandas.DataFrame(data)
        print(new_data)

        