

```python
import pandas as pd
import numpy as np
import datetime
from datetime import date
import pandas_datareader.data as web
```


```python
start = date(2016, 1, 1)
end = date.today()
```


```python
stock = web.DataReader("TWTR", 'yahoo', start, end)
stock.info()
stock.tail()
```

    <class 'pandas.core.frame.DataFrame'>
    DatetimeIndex: 281 entries, 2016-01-04 to 2017-02-13
    Data columns (total 6 columns):
    Open         281 non-null float64
    High         281 non-null float64
    Low          281 non-null float64
    Close        281 non-null float64
    Volume       281 non-null int64
    Adj Close    281 non-null float64
    dtypes: float64(5), int64(1)
    memory usage: 15.4 KB





<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Adj Close</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-02-07</th>
      <td>18.000000</td>
      <td>18.670000</td>
      <td>17.990000</td>
      <td>18.260000</td>
      <td>26719600</td>
      <td>18.260000</td>
    </tr>
    <tr>
      <th>2017-02-08</th>
      <td>18.770000</td>
      <td>18.770000</td>
      <td>18.049999</td>
      <td>18.719999</td>
      <td>37049000</td>
      <td>18.719999</td>
    </tr>
    <tr>
      <th>2017-02-09</th>
      <td>18.719999</td>
      <td>18.719999</td>
      <td>16.260000</td>
      <td>16.410000</td>
      <td>109007400</td>
      <td>16.410000</td>
    </tr>
    <tr>
      <th>2017-02-10</th>
      <td>15.960000</td>
      <td>16.000000</td>
      <td>15.500000</td>
      <td>15.580000</td>
      <td>72812600</td>
      <td>15.580000</td>
    </tr>
    <tr>
      <th>2017-02-13</th>
      <td>15.630000</td>
      <td>15.990000</td>
      <td>15.510000</td>
      <td>15.810000</td>
      <td>29055500</td>
      <td>15.810000</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Creating new column
stock["Return"] = 0.0
```


```python
#Calculating return
stock['Return'] = np.log(stock['Adj Close']/stock['Adj Close'].shift(1))
```


```python
stock[["Adj Close", "Return"]].tail()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Adj Close</th>
      <th>Return</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-02-07</th>
      <td>18.260000</td>
      <td>0.018238</td>
    </tr>
    <tr>
      <th>2017-02-08</th>
      <td>18.719999</td>
      <td>0.024880</td>
    </tr>
    <tr>
      <th>2017-02-09</th>
      <td>16.410000</td>
      <td>-0.131702</td>
    </tr>
    <tr>
      <th>2017-02-10</th>
      <td>15.580000</td>
      <td>-0.051903</td>
    </tr>
    <tr>
      <th>2017-02-13</th>
      <td>15.810000</td>
      <td>0.014655</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
