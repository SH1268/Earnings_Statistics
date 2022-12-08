# this is the "app/earnings_table.py" file..

import json
from pprint import pprint

import pandas


import requests

from app.alpha import API_KEY

print("Earnings Report")

def fetch_annual_earnings_data(symbol):

        request_url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}"
        
        response = requests.get(request_url)
        
        parsed_response = json.loads(response.text)

        return parsed_response["annualEarnings"]

def fetch_quarterly_earnings_data(symbol):

        request_url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}"
        
        response = requests.get(request_url)
        
        parsed_response = json.loads(response.text)

        return parsed_response["quarterlyEarnings"]

if __name__ == "__main__":
        symbol = input("Input company symbol: ")
         
        data_type = input("Would you like to look at annual data or quarterly data?: ") or "annual"

        if data_type == "annual":
                data = fetch_annual_earnings_data(symbol=symbol)
                print(data)

        elif data_type == "quarterly":
                data = fetch_quarterly_earnings_data(symbol=symbol)
                print(data)

        