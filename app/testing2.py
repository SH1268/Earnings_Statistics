
import os
import json
import requests
import pandas as pd
from pandas import read_csv
from dotenv import load_dotenv
import csv

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


request_url = f"https://www.alphavantage.co/query?function=EARNINGS&symbol=IBM&apikey={API_KEY}&datatype=csv"
df = read_csv(request_url)
print(df["annualEarnings"])