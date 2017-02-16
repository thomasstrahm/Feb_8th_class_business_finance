

```python
import pandas as pd
import numpy as np
import datetime
from datetime import date
import matplotlib.pyplot as plt
import pandas_datareader.data as web

```


```python
start = date(2015, 8, 1)
end = date.today()
```


```python
data = pd.DataFrame()
data = web.DataReader("MSFT", 'yahoo', start, end)
data.tail(2)
```


```python
data.sort_values(['Adj Close'], ascending=False).head()
```


```python
data['Low'].min()
```




    39.720001000000003




```python
data['High'].max()
```




    65.910004000000001




```python
data.resample('W-MON').mean().head()
```


```python
diff = data["Close"].max() - data["Close"].min()
diff
```


```python
data["Adj Close"].plot()
plt.show()
```


```python
returns = np.log(data["Adj Close"]/data["Adj Close"].shift(1))
returns.tail()
```


```python
returns.mean() * 252
```


```python

```
