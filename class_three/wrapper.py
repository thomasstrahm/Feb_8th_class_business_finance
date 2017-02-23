import requests

#Creating a wrapper with requests
def company_search(ticker):
    lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
    r = requests.get(lookup_url + ticker)
    print(r.json())
company_search("aapl")


#Creating a wrapper with requests
def get_quote(ticker):
        quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="
        r = requests.get(quote_url + ticker)
        print(r.json())
get_quote("aapl")