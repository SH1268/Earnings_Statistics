from app.earnings_table import fetch_quarterly_earnings_data, fetch_annual_earnings_data
from pandas import DataFrame

def test_fetch_quarterly_earnings_data():
    result = fetch_quarterly_earnings_data("IBM")
    assert isinstance (result, DataFrame)

    assert "fiscalDateEnding" in result.columns
    assert "reportedDate" in result.columns
    assert "reportedEPS" in result.columns
    assert "estimatedEPS" in result.columns
    assert "surprise" in result.columns
    assert "surprisePercentage" in result.columns

def test_fetch_annual_earnings_data():
    result = fetch_annual_earnings_data("IBM")
    assert isinstance (result, DataFrame)
    

    assert "fiscalDateEnding" in result.columns
    assert "reportedEPS" in result.columns
    
