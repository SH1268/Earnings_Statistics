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

## Testing

