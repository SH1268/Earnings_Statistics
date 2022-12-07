
import os
import json
from pprint import pprint

import requests
from app.alpha import API_KEY

symbol = input("Please enter a symbol (default = IBM): ") or "IBM"
print("SYMBOL: ", symbol)

def fetch_earnings_data():
        request_url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}"
        response = requests.get(request_url)
        parsed_response = json.loads(response.text)


if __name__ == "__main__":
        print("Earnings Report")

        data = fetch_earnings_data
        
        annual = "annualEarnings"
        quarterly = "quarterlyEarnings"
        
        data_selected = input("Would you like to look at annual data or quarterly data?: ") or "annual"
        
        if data_selected == "annual":
                data_selected = annual
        elif data_selected == "quarterly": 
                data_selected = quarterly
                
        data[data_selected]
        
        date_selected = input("Please enter a year (default = 2022): ") or "2022"