# Earnings_Statistics

## Setup

Create a virtual environment:
```sh 
conda create -n earnings-env python=3.8

conda activate earnings-env
```

Install package dependencies
```sh 
pip install -r requirements.txt
```

## Configuration

Obtain an AlphaVantage API Key [here](https://www.alphavantage.co/support/#api-key). 

```sh
Then create a local '.env' file that looks like this:

ALPHAVANTAGE_API_KEY="___"

```

## Usage

Runnings the earnings report:
```sh
python -m app.earnings
```

Runnings the earnings table:
```sh
python -m app.earnings_table
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run
# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```

## Testing

Run pytest:

```sh
pytest
```
