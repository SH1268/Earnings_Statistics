# this is the "app/earnings_table.py" file..

import json
from pprint import pprint
import requests
from plotly.express import line
import plotly.graph_objects as go

import pandas

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

                dates = [d["fiscalDateEnding"] for d in data]
                eps = [float(d["reportedEPS"]) for d in data]
                fig = line(x=dates, y=eps, title="Reported Earnings per Share (Annual)", labels= {"x": "Year", "y": "Earnings per Share"})
                fig.show()

                df = pandas.DataFrame(data)
                fig2 = go.Figure(data=[go.Table(
                        header=dict(values=list(df.columns)),
                        cells=dict(values= [df.fiscalDateEnding, df.reportedEPS]))
                        ])
                fig2.show()


        elif data_type == "quarterly":
                data = fetch_quarterly_earnings_data(symbol=symbol)

                dates = [d["fiscalDateEnding"] for d in data]
                eps = [float(d["reportedEPS"]) for d in data]
                fig = line(x=dates, y=eps, title="Reported Earnings per Share (Quarter)", labels= {"x": "Month & Year", "y": "Earnings per Share"})
                fig.show()

                df = pandas.DataFrame(data)
                fig2 = go.Figure(data=[go.Table(
                        name= "Stock Data Report",
                        header=dict(values=list(df.columns)),
                        cells=dict(values= [df.fiscalDateEnding, df.reportedDate, df.reportedEPS, df.estimatedEPS, 
                        df.surprise, df.surprisePercentage]))
                ])

                fig2.show()