#!/usr/bin/python3
import os, datetime
now = datetime.datetime.now().strftime('%Y-%m-%d')
from alpaca_trade_api.rest import REST, TimeFrame
ticker = []
api = REST(key_id='PKDQVXIQ0PBGUBFFV9VR', secret_key='W0JAsqtasEfmbHo4CZWXaM8qH83qlSZUU17Zasc1',base_url='https://paper-api.alpaca.markets')
with open('/Users/Nathan/Documents/Scripts/Stocks_for_{}'.format(now)) as file:
    for line in file:
       ticker.append(line.split(':')[1].split('|')[0].replace(' ', ''))

def buy_amount():
    account = api.get_account().__dict__
    cash = account['_raw']['cash']
    return cash

def buy_stocks(ticker, amount):
    for stock in ticker:
        print(api.submit_order(symbol=stock,notional=amount))
        print('ordered {}, {}'.format(stock, amount))

def get_postion(symbol):
    position = api.get_position(symbol=symbol).__dict__
    print(position['_raw'])


get_postion(ticker[0])
#buy_stocks(ticker=ticker, amount=(float(buy_amount())/len(ticker)))
