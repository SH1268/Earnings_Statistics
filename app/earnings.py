
import os
import json
from pandas import read_csv
from pprint import pprint


import requests

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

def fetch_earnings_data(symbol):
        
        request_url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol={symbol}&apikey={API_KEY}&datatype=csv"
        
        df = read_csv(request_url)

        return df

if __name__ == "__main__":
        print("Earnings Report")

        symbol = input("Please select a symbol (default = IBM): ") or "IBM"
        print("SYMBOL: ", symbol)

        df = fetch_earnings_data(symbol)

        print(df.columns)
        print

parsed_response = json.loads(response.text)
#print(type(parsed_response))
#pprint(parsed_response)

annual = "annualEarnings"
quarterly = "quarterlyEarnings"

data_selected = input("Would you like to look at annual data or quarterly data?: ") or "annual"

if data_selected == "annual":
     data_selected = annual
elif data_selected == "quarterly": 
    data_selected = quarterly

data = parsed_response[data_selected]

date_selected = input("Please enter a year (default = 2022): ") or "2022"

if data_selected == annual:
    this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
    earnings_this_year = [float(d["reportedEPS"]) for d in this_year]
    print(earnings_this_year)


elif data_selected == quarterly:
    this_quarter = input("Please enter a quarter (default = Q1): ") or "Q1"
    if this_quarter == "Q4":
            this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
            earnings_this_year = [float(d["reportedEPS"]) for d in this_year]
            print(earnings_this_year[0])
    elif this_quarter == "Q3":
            this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
            earnings_this_year = [float(d["reportedEPS"]) for d in this_year]
            print(earnings_this_year[1])
    elif this_quarter == "Q2":
            this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
            earnings_this_year = [float(d["reportedEPS"]) for d in this_year]
            print(earnings_this_year[2])
    elif this_quarter == "Q3":
            this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
            earnings_this_year = [float(d["reportedEPS"]) for d in this_year]
            print(earnings_this_year[3])

