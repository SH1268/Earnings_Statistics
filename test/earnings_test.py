from app.earnings import format_usd, fetch_quarterly_earnings_data, fetch_annual_earnings_data
 


def test_usd_formatting():

     #assert 2 + 2 == 4

     assert format_usd(4.5) == "$4.50"

     assert format_usd(4.5555555) == "$4.56"

     assert format_usd(1234567890) == "$1,234,567,890.00"

     #assert format_usd("OOPS") == "______"


def test_fetch_quarterly_earnings_data():
    result = fetch_quarterly_earnings_data("IBM")
    assert isinstance (result, list)

    latest = result[0]

    assert "fiscalDateEnding" in latest.keys()
    assert isinstance(latest["fiscalDateEnding"], str)
    assert "reportedDate" in latest.keys()
    assert isinstance(latest["reportedDate"], str)
    assert "reportedEPS" in latest.keys()
    assert isinstance(latest["reportedEPS"], str)
    assert "estimatedEPS" in latest.keys()
    assert isinstance(latest["estimatedEPS"], str)       
    assert "surprise" in latest.keys()
    assert isinstance(latest["surprise"], str)
    assert "surprisePercentage" in latest.keys()
    assert isinstance(latest["surprisePercentage"], str)


def test_fetch_annual_earnings_data():
    result = fetch_annual_earnings_data("IBM")
    assert isinstance (result, list)

    latest = result[0]
    
    assert "fiscalDateEnding" in latest.keys()
    assert isinstance(latest["fiscalDateEnding"], str)
    assert "reportedEPS" in latest.keys()
    assert isinstance(latest["reportedEPS"], str)