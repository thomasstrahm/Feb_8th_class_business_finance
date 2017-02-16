import pandas as pd
import numpy as np
import datetime
from datetime import date
import pandas_datareader.data as web

start = date(2016, 1, 1)
end = date.today()
stock = web.DataReader("TWTR", 'yahoo', start, end)
print(stock.info())
print(stock.tail())
#Creating new column
stock["Return"] = 0.0
#Calculating return
stock['Return'] = np.log(stock['Adj Close']/stock['Adj Close'].shift(1))
print(stock[["Adj Close", "Return"]].tail())