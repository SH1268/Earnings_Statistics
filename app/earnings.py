# this is the "app/earnings.py" file...

import json
from pprint import pprint


import requests
from dotenv import load_dotenv

from app.alpha import API_KEY



def fetch_annual_earnings_data():
        symbol = input("Input symbol: ")

        request_url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}"
        
        response = requests.get(request_url)
        
        parsed_response = json.loads(response.text)

        return parsed_response["annualEarnings"]

def fetch_quarterly_earnings_data():
        symbol = input("Input symbol: ")

        request_url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}"
        
        response = requests.get(request_url)
        
        parsed_response = json.loads(response.text)

        return parsed_response["quarterlyEarnings"]

if __name__ == "__main__":
        
        print("Earnings Report")

        data_type = input("Would you like to look at annual data or quarterly data?: ") or "annual"

        date_selected = input("Please enter a year (default = 2022): ") or "2022"

        if data_type == "annually":
                data = fetch_annual_earnings_data()
                this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
                earnings_this_year = [float(d["reportedEPS"]) for d in this_year]
                print("EPS",(earnings_this_year))

        elif data_type == "quarterly":
                data = fetch_quarterly_earnings_data()
                this_quarter = input("Please enter a quarter (default = Q1): ") or "Q1"
                if this_quarter == "Q4":
                        this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
                        earnings_this_year = [float(d["reportedEPS"]) for d in this_year]
                        print("EPS",(earnings_this_year[0]))
                elif this_quarter == "Q3":
                        this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
                        earnings_this_year = [float(d["reportedEPS"]) for d in this_year]
                        print("EPS",(earnings_this_year[1]))
                elif this_quarter == "Q2":
                        this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
                        earnings_this_year = [float(d["reportedEPS"]) for d in this_year]
                        print("EPS",(earnings_this_year[2]))
                elif this_quarter == "Q1":
                        this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
                        earnings_this_year = [float(d["reportedEPS"]) for d in this_year]
                        print("EPS",(earnings_this_year[3]))

        

        
        
