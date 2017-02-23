

```python
#first we import libraries
import wget
import re
import csv
```


```python
'''
downloding csv files and adding data to the list
'''	

def spdrHoldings(string):
    data = []
    file_url = 'http://www.sectorspdr.com/sectorspdr/IDCO.Client.Spdrs.Holdings/Export/ExportCsv?symbol='
    etf = wget.download(file_url + string)

    with open(etf,'r',errors='replace') as holdings:
        for line in holdings.readlines()[2:]:
#             print(line)
            #cleaning line a bit and split it
            split_line = line.replace('"','').strip().split(',')[:-1]
#             print(split_line)
#             we have to change volume, check split_line[6]
#             print(split_line[6])
#             converting volume into int
            if "K" in split_line[6]:
                split_line[6] = int(float(re.sub('["".KM]', '', split_line[6])))*1000
            elif "M" in split_line[6]:
                split_line[6] = int(float(re.sub('["".KM]', '', split_line[6])))*1000000
#             coverting last price into int
#             print(split_line[3])
            split_line[3] = int(float(re.sub('[""]', '', split_line[3])))
#             print(split_line[3])

            data.append(list(split_line))
    
#         print(data)
        return data
# spdrHoldings("XLF")
```


```python
'''
returns the largest last price
''' 

def highestValue():
    data = spdrHoldings("XLF")
    values = []
    for line in data:
        symbol = line[0]
        last = line[3]
        values.append({'price':last,"symbol":symbol})
#     print(max(values,key=lambda item: item['price']))
    return max(values,key=lambda item: item['price'])


highestValue()
```




    {'price': 390, 'symbol': 'BLK'}




```python
'''
Summing up VOLUME in csv file if name of the co contains GROUP
'''

def findAllHoldings(etf):
    data = spdrHoldings(etf)
    group_count = []
    for line in data:
        # print(line)
        if re.search(r'[Gg]roup', line[1]):
            symbol = line[1]
            print("SYMBOL", symbol)
            volume = line[6]
            group_count.append(volume)

   
    return group_count
# findAllHoldings()
```


```python
def etf_exercise():
    etfs = ["XLF"]
    all_values =[]
    for symbol in etfs:
#         high_value = highestValue(symbol)
#         print('\n', "for ETF", symbol, "highest last price", high_value)
        group_count = findAllHoldings(symbol)
        if group_count not in all_values:
            all_values.append(group_count)

    print('\n',"Total trading volume for companies with name 'Group' is {0:,}".format(sum(sum(i) for i in all_values)))

etf_exercise()
```

    SYMBOL Citigroup Inc
    SYMBOL Goldman Sachs Group Inc
    SYMBOL American Intl Group Inc
    SYMBOL PNC Finl Services Group
    SYMBOL CME Group Inc A
    SYMBOL Citizens Financial Group Inc
    SYMBOL Hartford Finl Services Group
    SYMBOL T Rowe Price Group Inc
    SYMBOL Principal Financial Group
    SYMBOL Unum Group
    SYMBOL XL Group Ltd
    
     Total trading volume for companies with name 'Group' is 4,428,394,000



```python

```
