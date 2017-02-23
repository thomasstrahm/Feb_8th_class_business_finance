

```python
import requests

```


```python
#Creating a wrapper with requests
def company_search(ticker):
    lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
    r = requests.get(lookup_url + ticker)
    print(r.json())
company_search("aapl")
```

    [{'Exchange': 'NASDAQ', 'Symbol': 'AAPL', 'Name': 'Apple Inc'}, {'Exchange': 'NASDAQ', 'Symbol': 'AVSPY', 'Name': 'AAPL ALPHA INDEX'}, {'Exchange': 'NASDAQ', 'Symbol': 'AIX', 'Name': 'NAS OMX Alpha   AAPL vs. SPY  Settle'}]



```python
#Creating a wrapper with requests
def get_quote(ticker):
        quote_url = "http://dev.markitondemand.com/Api/v2/Quote/json?symbol="
        r = requests.get(quote_url + ticker)
        print(r.json())
get_quote("aapl")
```

    {'Timestamp': 'Fri Jan 27 00:00:00 UTC-05:00 2017', 'ChangePercent': 0.00820075446941538, 'Open': 122.14, 'MarketCap': 641190661200, 'Volume': 20562944, 'Change': 0.0100000000000051, 'ChangeYTD': 115.82, 'ChangePercentYTD': 5.2926955620791, 'MSDate': 42762, 'High': 122.35, 'Name': 'Apple Inc', 'Status': 'SUCCESS', 'Low': 121.6, 'LastPrice': 121.95, 'Symbol': 'AAPL'}



```python

```
