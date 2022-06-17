#!/usr/bin/python3
import sys, datetime, os
sys.path.append('Users/Nathan/Scripting/finviz/lib/python3.8/site-packages/finviz')
from finviz.screener import Screener
now = datetime.datetime.now().strftime('%Y-%m-%d')
filters = ['an_recom_buybetter','cap_midover','geo_usa','sh_avgvol_o1000','sh_opt_option','ta_highlow52w_a0to10h','ta_rsi_os40','ta_sma50_sa200','targetprice_above']
stock_list_filter1 = Screener(filters=filters,table='Performance', order='Price')
file_path='/Users/Nathan/Documents/Scripts/Stocks_for_{}'.format(now)

#filters2 = ['an_recom_buybetter','sh_avgvol_o2000','ta_averagetruerange_o1.5','ta_highlow52w_b15h','ta_rsi_nob60',
           # 'ta_sma20_pa','ta_sma200_pa','ta_sma50_pa']
#stock_list_filter2 = Screener(filters=filters2,table='Performance', order='Price')

stonks = ([i for i in stock_list_filter1]) #+ [i for i in stock_list_filter2])

with open(file_path,'a') as file:
    for stock in stonks:
        if float(stock['Recom']) > 2.0:
            file.write(str('Ticker: {} | Price: ${} | Reccomendation: {}'.format(stock['Ticker'], stock['Price'], stock['Recom']) + '\n'))
os.popen('cat /Users/Nathan/Documents/Scripts/Stocks_for_{} | mail -s “Stocks_for_{}” nathcarr55@gmail.com'.format(now,now))

