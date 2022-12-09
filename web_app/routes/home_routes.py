# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    # return "Welcome Home"
    return render_template("home.html")

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return render_template("about.html")

@home_routes.route("/earnings_table_annual")
def earnings_annual_table():
    print("Annual Earnings Table")

    # if the request contains url params, for example a request to "/"
    # the request object's args property will hold the values in a dictionary-like structure
    url_params = dict(request.args)
    print("URL PARAMS:", url_params) #> 

    # get a specific key called "name" if available, otherwise use some specified default value
    # see also: https://www.w3schools.com/python/ref_dictionary_get.asp
    symbol = url_params.get("symbol")

    return render_template("earnings_table_annual.html")

@home_routes.route("/earnings_table_quarterly")
def earnings_quarterly_table():
    print("Quarterly Earnings Table")

    # if the request contains url params, for example a request to "/"
    # the request object's args property will hold the values in a dictionary-like structure
    url_params = dict(request.args)
    print("URL PARAMS:", url_params) #> 

    # get a specific key called "name" if available, otherwise use some specified default value
    # see also: https://www.w3schools.com/python/ref_dictionary_get.asp
    symbol = url_params.get("symbol")

    return render_template("earnings_table_annual.html")