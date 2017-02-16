

```python
import pandas as pd
import numpy as np
import datetime
from datetime import date
import matplotlib.pyplot as plt
import pandas_datareader.data as web
```


```python
symbols = ["ORCL","MSFT", "^GSPC"]
```


```python
data = pd.DataFrame()
```


```python
start = date(2016, 1, 1)
end = date.today()
```


```python
for ticker in symbols:
    data[ticker] = web.DataReader(ticker, 'yahoo', start, end)["Adj Close"]
```


```python
data.tail()
```


```python
#We use 100 as a starting value
#Using ix as a primarily label-location based indexer
(data/data.ix[0] * 100).plot()
plt.show()
```


```python
#Calculating log returns
log_returns = np.log(data/data.shift(1))
log_returns.tail()
```


```python
log_returns.hist(bins=50)
plt.show()
```


```python

```
