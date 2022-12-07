

# this is the "app.alpha.py" file
# contains the api key variable

import os
from dotenv import load_dotenv

load_dotenv() # look in the ".env" file

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")