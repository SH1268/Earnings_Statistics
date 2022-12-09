# this is the "web_app/routes/unemployment_routes.py" file...

from flask import Blueprint, request, render_template, redirect
    
from app.earnings_table import fetch_annual_earnings_data, fetch_quarterly_earnings_data
    
earnings_table_routes = Blueprint("earnings_table_routes", __name__)
    
@earnings_table_routes.route("/earnings_table_annual/form")
def annual_earnings_table_form():
        print("A EARNINGS FORM...")
        return render_template("earnings_table_annual_form.html")

@earnings_table_routes.route("/earnings_table_quarterly/form")
def quarterly_earnings_table_form():
        print("Q EARNINGS FORM...")
        return render_template("earnings_table_quarterly_form.html")
    
@earnings_table_routes.route("/earnings_table/annual_dashboard",  methods=["GET", "POST"])
def earnings_table_annual_dashboard():
        print("EARNINGS DASHBOARD...")
    
        if request.method == "POST":
            # for data sent via POST request, form inputs are in request.form:
            request_data = dict(request.form)
            print("FORM DATA:", request_data)
        else:
            # for data sent via GET request, url params are in request.args
            request_data = dict(request.args)
            print("URL PARAMS:", request_data)
    
        symbol = request_data.get("symbol") or "IBM"
    
        try:
            data = fetch_annual_earnings_data(symbol=symbol)
            latest = data[0]
            latest_eps = float(latest["reportedEPS"])
            latest_date = latest["fiscalDateEnding"]

            #flash("Fetched Real-time Market Data!", "success")
            return render_template("earnings_table_annual.html",
                symbol=symbol,
                latest_eps=latest_eps,
                latest_date=latest_date,
                data=data
            )
        except Exception as err:
            print('OOPS', err)
    
            #flash("Market Data Error. Please check your symbol and try again!", "danger")
            return redirect("/earnings_table_annual/form")

@earnings_table_routes.route("/earnings_table/quarterly_dashboard",  methods=["GET", "POST"])
def earnings_table_quarterly_dashboard():
        print("EARNINGS DASHBOARD...")
    
        if request.method == "POST":
            # for data sent via POST request, form inputs are in request.form:
            request_data = dict(request.form)
            print("FORM DATA:", request_data)
        else:
            # for data sent via GET request, url params are in request.args
            request_data = dict(request.args)
            print("URL PARAMS:", request_data)
    
        symbol = request_data.get("symbol") or "IBM"
    
        try:
            data = fetch_quarterly_earnings_data(symbol=symbol)
            latest = data[0]
            latest_eps = float(latest["reportedEPS"])
            latest_date = latest["fiscalDateEnding"]

            #flash("Fetched Real-time Market Data!", "success")
            return render_template("earnings_table_quarterly.html",
                symbol=symbol,
                latest_eps=latest_eps,
                latest_date=latest_date,
                data=data
            )
        except Exception as err:
            print('OOPS', err)
    
            #flash("Market Data Error. Please check your symbol and try again!", "danger")
            return redirect("/earnings_table_quarterly/form")
    
    #
    # API ROUTES
    #
    
@earnings_table_routes.route("/api/earnings_table.json")
def earnings_table_api():
        print("EARNINGS DATA (API)...")
    
        # for data supplied via GET request, url params are in request.args:
        url_params = dict(request.args)
        print("URL PARAMS:", url_params)
        symbol = url_params.get("symbol") or "IBM"
    
        try:
            data = fetch_annual_earnings_data(symbol=symbol)
            df = str(data)
            return df
        except Exception as err:
            print('OOPS', err)
            return {"message":"Market Data Error. Please try again."}, 404