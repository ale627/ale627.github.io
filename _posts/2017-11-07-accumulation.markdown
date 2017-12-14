---
layout: post
title:  "Quant: Accumulation"
date:   2017-11-07 12:00:00 -0700
category: python
color: royalblue
---

*Here I do bar analysis to find potential buy spots.  This analysis is simply counting instances of minutely bars closing on highs.*

*This is an analysis from a Python [Jupyter notebook][jn], [exported directly][ex].  The tables below each code block are the API responses.*

*I am using the [BarChart.com OnDemand API][bc] to call getHistory() and receive 3 months of minute data for a basket of stocks.*  

*To use the code yourself, you will need to setup a python environment, jupyter notebook or otherwise.  Then [request a free BarChart.com OnDemand API key][bc], and plug it in.*

*Last, set the file path for your project directory, and in that folder create a folder 'Stock_Price_Data' to export data to, and a folder 'assets' for your list.  In 'assets' create an Excel file 'Watchlist'.  With a header have names in the first column and tickers in the second column.*

[jn]: https://jupyter.org/
[ex]: https://github.com/jupyter/nbconvert
[bc]: https://www.barchart.com/ondemand/free-market-data-api

# Fetch the data from BarChart

Here we call the barchart getHistory API.  This is an adaptation of BlackArb's Python [tutorial][tut].

#### Steps:
- import libraries
- set directories and API key
- build URL to call API
- get_minute_data() function
- call the function

[tut]: http://www.blackarbs.com/blog/how-to-get-free-intraday-stock-data-with-python-and-barcharts-ondemand-api/9/22/2015



```python
# -*- coding: utf-8 -*-

#----------IMPORT LIBRARIES----------#
import time
t0 = time.clock()

import pandas as pd
from pandas.tseries.offsets import BDay

import numpy as np
import datetime as dt

from copy import copy
import warnings
warnings.filterwarnings('ignore',category=pd.io.pytables.PerformanceWarning)
 

    
#----------SET DIRECTORIES----------#
    
project_dir = r'C:\Users/drale/Desktop/python/' 
price_path = project_dir + r'Stock_Price_Data\\'

# header=3 to skip metadata   
components = pd.read_excel(project_dir +\
                             'assets/Watchlist.xls', header=0)
syms = components.Identifier.dropna()
syms = syms.drop(syms.index[-1]).sort_values()


apikey = 'x'



#----------BUILD URL----------#

def construct_barChart_url(sym, start_date, freq, api_key=apikey):
    '''Function to construct barchart api url'''
    
    url = 'http://marketdata.websol.barchart.com/getHistory.csv?' +\
            'key={}&symbol={}&type={}&startDate={}'.format(api_key, sym, freq, start_date)
    return url

#outputs: symbol, timestamp, tradingDay, open, high, low, close, volume, openInterest

#----------F(X) DEFINITION----------#

def get_minute_data():
    '''Function to Retrieve <= 3 months of minute data'''
    
    # YYYY MM DD HH MM SS
    start = '20171001000000'
    #end = d
    freq = 'minutes'    
    prices = {}
    symbol_count = len(syms)
    
    try:
        for i, sym in enumerate(syms, start=1):
            api_url = construct_barChart_url(sym, start, freq, api_key=apikey)
            try:
                csvfile = pd.read_csv(api_url, parse_dates=['timestamp'])
                csvfile.set_index('timestamp', inplace=True)
                prices[sym] = csvfile
            except:
                continue

            print('{}..[fetched] | {} of {} tickers |'.format(sym, i, symbol_count)) 
    except Exception as e: 
        print(e)
    finally:
        pass
    
    px = pd.Panel.from_dict(prices)
    px.major_axis = px.major_axis.tz_localize('utc').tz_convert('US/Pacific')
    return px



#----------CALL FUNCTION----------#

pxx = get_minute_data()
pxx

# timer
secs      = np.round( ( time.clock()  - t0 ), 4 )
time_secs = "{timeSecs} seconds to run".format(timeSecs = secs)
print( time_secs )
```

    AAPL..[fetched] | 1 of 9 tickers |
    AMZN..[fetched] | 2 of 9 tickers |
    BIDU..[fetched] | 3 of 9 tickers |
    FB..[fetched] | 4 of 9 tickers |
    GOOGL..[fetched] | 5 of 9 tickers |
    GS..[fetched] | 6 of 9 tickers |
    IBB..[fetched] | 7 of 9 tickers |
    NFLX..[fetched] | 8 of 9 tickers |
    TSLA..[fetched] | 9 of 9 tickers |
    47.5803 seconds to run
    

# Select stock
Choose a ticker to analyze, and test the output.


```python
stock = 'GOOGL'

ohlc = pxx[stock]
ohlc.tail(11)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>symbol</th>
      <th>tradingDay</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>timestamp</th>
      <th></th>
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
      <th>2017-11-09 12:50:00-08:00</th>
      <td>GOOGL</td>
      <td>2017-11-09</td>
      <td>1046.950</td>
      <td>1049.33</td>
      <td>1046.95</td>
      <td>1048.000</td>
      <td>9359</td>
    </tr>
    <tr>
      <th>2017-11-09 12:51:00-08:00</th>
      <td>GOOGL</td>
      <td>2017-11-09</td>
      <td>1048.105</td>
      <td>1048.24</td>
      <td>1047.72</td>
      <td>1047.740</td>
      <td>4044</td>
    </tr>
    <tr>
      <th>2017-11-09 12:52:00-08:00</th>
      <td>GOOGL</td>
      <td>2017-11-09</td>
      <td>1047.680</td>
      <td>1048.19</td>
      <td>1047.53</td>
      <td>1047.530</td>
      <td>2797</td>
    </tr>
    <tr>
      <th>2017-11-09 12:53:00-08:00</th>
      <td>GOOGL</td>
      <td>2017-11-09</td>
      <td>1047.700</td>
      <td>1048.00</td>
      <td>1047.44</td>
      <td>1047.690</td>
      <td>7585</td>
    </tr>
    <tr>
      <th>2017-11-09 12:54:00-08:00</th>
      <td>GOOGL</td>
      <td>2017-11-09</td>
      <td>1047.830</td>
      <td>1047.95</td>
      <td>1047.59</td>
      <td>1047.940</td>
      <td>1741</td>
    </tr>
    <tr>
      <th>2017-11-09 12:55:00-08:00</th>
      <td>GOOGL</td>
      <td>2017-11-09</td>
      <td>1047.775</td>
      <td>1048.05</td>
      <td>1047.72</td>
      <td>1047.921</td>
      <td>10171</td>
    </tr>
    <tr>
      <th>2017-11-09 12:56:00-08:00</th>
      <td>GOOGL</td>
      <td>2017-11-09</td>
      <td>1047.700</td>
      <td>1048.00</td>
      <td>1047.55</td>
      <td>1047.887</td>
      <td>6478</td>
    </tr>
    <tr>
      <th>2017-11-09 12:57:00-08:00</th>
      <td>GOOGL</td>
      <td>2017-11-09</td>
      <td>1047.863</td>
      <td>1048.00</td>
      <td>1047.76</td>
      <td>1047.820</td>
      <td>7859</td>
    </tr>
    <tr>
      <th>2017-11-09 12:58:00-08:00</th>
      <td>GOOGL</td>
      <td>2017-11-09</td>
      <td>1047.911</td>
      <td>1048.07</td>
      <td>1047.41</td>
      <td>1047.950</td>
      <td>15405</td>
    </tr>
    <tr>
      <th>2017-11-09 12:59:00-08:00</th>
      <td>GOOGL</td>
      <td>2017-11-09</td>
      <td>1048.030</td>
      <td>1048.03</td>
      <td>1046.89</td>
      <td>1047.540</td>
      <td>23058</td>
    </tr>
    <tr>
      <th>2017-11-09 13:00:00-08:00</th>
      <td>GOOGL</td>
      <td>2017-11-09</td>
      <td>1047.720</td>
      <td>1047.72</td>
      <td>1047.72</td>
      <td>1047.720</td>
      <td>68623</td>
    </tr>
  </tbody>
</table>
</div>



# Accumulation
Where 1 min candlestick closes on highs, flag as accumulated.


```python
#create accum column: for closing on highs, assign 1
ohlc["accum"] = np.where(ohlc["high"] == ohlc["close"], 1, 0)

#list matches
accumulation_bars = ohlc[(ohlc.accum == 1)]
accumulation_bars[["high", "close", "accum"]].tail(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>high</th>
      <th>close</th>
      <th>accum</th>
    </tr>
    <tr>
      <th>timestamp</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-11-09 12:37:00-08:00</th>
      <td>1047.76</td>
      <td>1047.76</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2017-11-09 12:45:00-08:00</th>
      <td>1046.83</td>
      <td>1046.83</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2017-11-09 13:00:00-08:00</th>
      <td>1047.72</td>
      <td>1047.72</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



## Two-in-a-row
*Add the previous accumulated (or not) to current row*

Measures when two 1-min candlesticks in a row close at highs.


```python
#create conf column adding prev column
ohlc["conf"] = ohlc.accum + ohlc.accum.shift(1)

#where conf is 2, make a table
confirmation = ohlc[(ohlc.conf >= 2)]
confirmation[["high", "close", "conf"]].tail(3)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>high</th>
      <th>close</th>
      <th>conf</th>
    </tr>
    <tr>
      <th>timestamp</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-11-09 12:05:00-08:00</th>
      <td>1043.610</td>
      <td>1043.610</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2017-11-09 12:08:00-08:00</th>
      <td>1043.929</td>
      <td>1043.929</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2017-11-09 12:11:00-08:00</th>
      <td>1044.530</td>
      <td>1044.530</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



## Accumulation daily signal

*sum the consecutive accumulation by day*

**Return the 3 biggest daily signals**


```python
#combine minutes into days
signal = confirmation.resample('D',how='sum')

#sort based on sum(conf)
signal.nlargest(3,'conf')
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>accum</th>
      <th>conf</th>
    </tr>
    <tr>
      <th>timestamp</th>
      <th></th>
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
      <th>2017-10-09 00:00:00-07:00</th>
      <td>42877.0643</td>
      <td>42883.2938</td>
      <td>42874.1932</td>
      <td>42883.2938</td>
      <td>59941</td>
      <td>43</td>
      <td>86</td>
    </tr>
    <tr>
      <th>2017-11-02 00:00:00-07:00</th>
      <td>43662.1550</td>
      <td>43673.1240</td>
      <td>43657.7140</td>
      <td>43673.1240</td>
      <td>40449</td>
      <td>42</td>
      <td>84</td>
    </tr>
    <tr>
      <th>2017-10-17 00:00:00-07:00</th>
      <td>41388.0520</td>
      <td>41395.7110</td>
      <td>41385.9700</td>
      <td>41395.7110</td>
      <td>35038</td>
      <td>41</td>
      <td>82</td>
    </tr>
  </tbody>
</table>
</div>