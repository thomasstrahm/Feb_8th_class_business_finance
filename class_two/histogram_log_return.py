# importiing all libriaries
import pandas as pd
import numpy as np
import datetime
from datetime import date
import matplotlib.pyplot as plt
import pandas_datareader.data as web

# defining symbols
symbols = ["ORCL","MSFT", "^GSPC"]

# creating new variable with data frame data structure
data = pd.DataFrame()

# defining start and end dates
start = date(2016, 1, 1)
end = date.today()

# using for loop to get historic prices for stocks
for ticker in symbols:
    data[ticker] = web.DataReader(ticker, 'yahoo', start, end)["Adj Close"]

# checking data
print(data.tail())

#We use 100 as a starting value
#Using ix as a primarily label-location based indexer
# (data/data.ix[0] * 100).plot()
# plt.show()

#Calculating log returns
log_returns = np.log(data/data.shift(1))
print(log_returns.tail())

# plotting histograms for log returns
log_returns.hist(bins=50)
plt.show()
