# this is the "app/earnings.py" file...

import json
from pprint import pprint

import requests

from app.alpha import API_KEY

def format_usd(my_price):
     return f"${my_price:,.2f}"


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

all_datapoints = []

if __name__ == "__main__":
        
        add_data = "Yes"
        
        while add_data == "Yes":
                
                symbol = input("Input company symbol: ") or "IBM"
                
                data_type = input("Would you like to look at annual data or quarterly data?: ") or "annual"
                
                date_selected = input("Please enter a year: ") or "2022"
                 
                if data_type == "annual":
                         data = fetch_annual_earnings_data(symbol=symbol)
                         this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
                         earnings_this_year = [float(d["reportedEPS"]) for d in this_year]
                         raw_datapoint = ("EPS for ",symbol," in ", date_selected," is ", format_usd(earnings_this_year[0]))
                         new_datapoint = ''.join(raw_datapoint)
                         all_datapoints.append(new_datapoint)
                         add_data = input("Would you like to add a new datapoint? (Yes/No) ") or "Yes"
                
                elif data_type == "quarterly":
                        data = fetch_quarterly_earnings_data(symbol=symbol)
                        this_quarter = input("Please enter a quarter: ") or "Q1"
                        
                        if this_quarter == "Q4":
                                this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
                                earnings_Q4 = [float(d["reportedEPS"]) for d in this_year]
                                raw_datapoint = ("EPS for ",symbol," in ", date_selected," Q4 is ", format_usd(earnings_Q4[0]))
                                new_datapoint = ''.join(raw_datapoint)
                                all_datapoints.append(new_datapoint)
                                add_data = input("Would you like to add a new datapoint? (Yes/No) ") or "Yes"
                        
                        elif this_quarter == "Q3":
                                this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
                                earnings_Q3 = [float(d["reportedEPS"]) for d in this_year]
                                raw_datapoint = ("EPS for ",symbol," in ", date_selected," Q3 is ", format_usd(earnings_Q3[1]))
                                new_datapoint = ''.join(raw_datapoint)
                                all_datapoints.append(new_datapoint)
                                add_data = input("Would you like to add a new datapoint? (Yes/No) ") or "Yes"
                        
                        elif this_quarter == "Q2":
                                this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
                                earnings_Q2 = [float(d["reportedEPS"]) for d in this_year]
                                raw_datapoint = ("EPS for ",symbol," in ", date_selected," Q2 is ", format_usd(earnings_Q2[2]))
                                new_datapoint = ''.join(raw_datapoint)
                                all_datapoints.append(new_datapoint)
                                add_data = input("Would you like to add a new datapoint? (Yes/No) ") or "Yes"
                        
                        elif this_quarter == "Q1":
                                this_year = [d for d in data if date_selected in d["fiscalDateEnding"]]
                                earnings_Q1 = [float(d["reportedEPS"]) for d in this_year]
                                raw_datapoint = ("EPS for ",symbol," in ", date_selected," Q1 is ", format_usd(earnings_Q1[3]))
                                new_datapoint = ''.join(raw_datapoint)
                                all_datapoints.append(new_datapoint)
                                add_data = input("Would you like to add a new datapoint? (Yes/No) ") or "Yes"

print(all_datapoints)
