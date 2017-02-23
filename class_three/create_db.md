

```python
import sqlite3 as sq3
```


```python
#creating database
conn = sq3.connect('three.db')
c = conn.cursor()
query = 'CREATE TABLE stock (symbol, price)'
# c.execute(query)
# conn.commit()
```


```python
#inserting values
c.execute("INSERT INTO stock VALUES(?,?)", ("AAPL", "119"))
conn.commit()
```


```python

```
