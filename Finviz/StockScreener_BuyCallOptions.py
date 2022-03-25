#!/usr/bin/python3
import sys, datetime, os
sys.path.append('Users/Nathan/Scripting/finviz/lib/python3.8/site-packages/finviz')
from finviz.screener import Screener
now = datetime.datetime.now().strftime('%Y-%m-%d')
filters = ['an_recom_buybetter','cap_midover','geo_usa','sh_avgvol_o1000','sh_opt_option','ta_highlow52w_a0to10h','ta_rsi_os40','ta_sma50_sa200','targetprice_above']
stock_list = Screener(filters=filters,table='Performance', order='Price')
file_path='/Users/Nathan/Documents/Scripts/Stocks_for_{}'.format(now)
with open(file_path,'a') as file:
    for stock in stock_list:
        file.write(str('Ticker: {} | Price: ${} | Reccomendation: {}'.format(stock['Ticker'], stock['Price'], stock['Recom']) + '\n'))
os.popen('cat /Users/Nathan/Documents/Scripts/Stocks_for_{} | mail -s “Stocks_for_{}” nathcarr55@gmail.com'.format(now,now))

