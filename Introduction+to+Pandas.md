

```python
#import pandas
import pandas as pd 

```


```python
# create Data Frame object
stocks = ["IBM", "APPLE", "TWTTR", "GE", "MSFT"]
prices = [115.00, 119.14, 19.77, 25.99, 26]

```


```python
portfolio = list(zip(stocks,prices))
print(portfolio)
```

    [('IBM', 115.0), ('APPLE', 119.14), ('TWTTR', 19.77), ('GE', 25.99), ('MSFT', 26)]



```python
df = pd.DataFrame(data=portfolio, columns=['stocks', 'prices'])
print(df)
```

      stocks  prices
    0    IBM  115.00
    1  APPLE  119.14
    2  TWTTR   19.77
    3     GE   25.99
    4   MSFT   26.00



```python
#lets add another col
df['new_col'] = " "
print(df)

```

      stocks  prices new_col
    0    IBM  115.00        
    1  APPLE  119.14        
    2  TWTTR   19.77        
    3     GE   25.99        
    4   MSFT   26.00        



```python
# lets write this to csv file
df.to_csv("my_portfolio.csv", index=True)
```


```python
# sort data
sort_portfolio = df.sort_values(['prices'], ascending=True)
print(sort_portfolio)
```

      stocks  prices new_col
    2  TWTTR   19.77        
    3     GE   25.99        
    4   MSFT   26.00        
    0    IBM  115.00        
    1  APPLE  119.14        



```python
# get max and min values
max_price = df["prices"].max()
print("MAX",max_price)

min_price = df["prices"].min()
print("MIN",min_price)

```

    MAX 119.14
    MIN 19.77



```python
# Now we can reset index
df.index = ['a', 'b','c','d','e']
print(df)
```

      stocks  prices new_col
    a    IBM  115.00        
    b  APPLE  119.14        
    c  TWTTR   19.77        
    d     GE   25.99        
    e   MSFT   26.00        



```python
df["new_col"] = 5
print(df)
```

      stocks  prices  new_col
    a    IBM  115.00        5
    b  APPLE  119.14        5
    c  TWTTR   19.77        5
    d     GE   25.99        5
    e   MSFT   26.00        5



```python
# slicing df
print(df.loc["b":"d"])
```

      stocks  prices  new_col
    b  APPLE  119.14        5
    c  TWTTR   19.77        5
    d     GE   25.99        5



```python
# access the item by loc
print(df.loc["c"])
```

    stocks     TWTTR
    prices     19.77
    new_col        5
    Name: c, dtype: object



```python
# Lets go to yahho.com and download historical prices for appl
new_file = pd.read_csv("Downloads/appl.csv",skiprows=0)
print(new_file.tail())

```

              Date        Open        High         Low       Close    Volume  \
    15  2017-01-13  119.110001  119.620003  118.809998  119.040001  25938300   
    16  2017-01-12  118.900002  119.300003  118.209999  119.250000  27002400   
    17  2017-01-11  118.739998  119.930000  118.599998  119.750000  27418600   
    18  2017-01-10  118.769997  119.379997  118.300003  119.110001  24420800   
    19  2017-01-09  117.949997  119.430000  117.940002  118.989998  33387600   
    
         Adj Close  
    15  119.040001  
    16  119.250000  
    17  119.750000  
    18  119.110001  
    19  118.989998  

