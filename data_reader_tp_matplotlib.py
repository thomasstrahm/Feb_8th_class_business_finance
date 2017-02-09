# Importing liabraries and DataReader
import pandas as pd 
import pandas_datareader.data as web
import matplotlib.pyplot as plt 
import datetime
from datetime import date

# Setting time range
start = date(2016,1,1)
end = date.today()

# Getting data for a stock
stock_price = web.DataReader("TWTR", "yahoo", start, end)
# stock_price.tail(5)

stock_price["MA"] = stock_price["Adj Close"].rolling(window=10).mean()
# stock_price.head()
# stock_price.tail()

# we create grids
price_fig = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
volume_fig = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=price_fig)
price_fig.plot(stock_price.index, stock_price['Adj Close'])
price_fig.plot(stock_price.index, stock_price['MA'])
volume_fig.bar(stock_price.index, stock_price['Volume'])

plt.show()

