import numpy as np 
import pandas as pd 
from pandas import DataFrame as df
import pandas_datareader.data as web
from datetime import date
import matplotlib.pyplot as plt
import csv

def get_sp_data():
    sdate = date(2016,1,3)
    edate = date(2017,1,16)

    sp = web.DataReader('^GSPC','yahoo',sdate, edate)
    return sp

# get_sp_data()

def plot_price():
    sp = get_sp_data()
    data = pd.DataFrame(sp['Close'], index=sp.index)
    
    min_close_price = pd.DataFrame.min(sp['Close'])
    print(min_close_price)
    data.plot()
    
    verical_line = plt.axvline(date(2016,7,1), linewidth=1, color='r')
    horizontal_line = plt.axhline(y=min_close_price, linewidth=1, color='r')
    plt.show()
    plt.savefig('SPYPrice2015.pdf', format='pdf')

plot_price()

def monthly_returns():
    sp = get_sp_data()
    sp_monthly = sp.resample('MS').mean()
    data = pd.DataFrame(sp_monthly['Adj Close'], index=sp_monthly.index)
    data[['sp_returns']] = (data[['Adj Close']]/data[['Adj Close']].shift(1)-1 )*100
    print(data[['sp_returns']])
    sp_returns = pd.DataFrame(data[['sp_returns']], columns =['sp_returns'])
    sp_returns.to_csv('SPYReturn.csv')

monthly_returns()