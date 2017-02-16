

```python
import pandas as pd 
import pandas_datareader.data as web
import matplotlib.pyplot as plt 
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates
```


```python
import datetime
from datetime import date
```


```python
start = date(2016,1,1)
end = date(2017,1,20)
```


```python
# creating object stock_price
stock_price = web.DataReader("TWTR", "yahoo", start, end)
```


```python
# resampling data to 10days period
ten_days = stock_price['Adj Close'].resample('10D').ohlc()
stock_volume = stock_price['Volume'].resample('10D').sum()
stock_volume.tail()


```




    Date
    2016-12-09     85977500
    2016-12-19    135499100
    2016-12-29     87224000
    2017-01-08     69821500
    2017-01-18     39457600
    Freq: 10D, Name: Volume, dtype: int64




```python
# resetting index for OHLC
ten_days.reset_index(inplace=True)
```


```python
# have to create new datetime objects for matplotlib
ten_days["Date"] = ten_days["Date"].map(mdates.date2num)
```


```python
# creating two ficures
price_fig = plt.subplot2grid((6,1),(0,0), rowspan=5, colspan=1)
volume_fig = plt.subplot2grid((6,1),(5,0), rowspan=1, colspan=1, sharex=price_fig)
```


```python
# plotting data
price_fig.xaxis_date()
candlestick_ohlc(price_fig, ten_days.values, width=5)
volume_fig.fill_between(stock_volume.index.map(mdates.date2num), stock_volume.values, 0)

plt.show()
```


![png](output_8_0.png)



```python

```
