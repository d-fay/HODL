"""
THIS CLASS HANDLES ALL POLONIEX API

Parameter configuration files are located in ../conf/settings.ini
"""
import sys
import time
import datetime

from poloniex import Poloniex

from hodl.ConfRetriever import ConfRetriever
"""
Open a connection to the Poloniex API

    REQUIREMENT: Install s4w3d0ff's python-poloniex library:

        $ pip3 install -r requirements.txt
        
        OR

        $ pip3 install https://github.com/s4w3d0ff/python-poloniex/archive/v0.4.6.zip
        
    DOCUMENTATION for Poloniex(): 
        - https://poloniex.com/support/api/
        - https://pastebin.com/8fBVpjaj
        - https://github.com/s4w3d0ff/python-poloniex/wiki/The-Poloniex-Class
    
"""

conf = ConfRetriever()
NEAR_ZERO_BALANCE = float(conf.near_zero_balance)  # arbitrarily small value used to remove near-zero account balances

try:
    connection = Poloniex(key=conf.polo_key, secret=conf.polo_secret)
except:
    print('Unexpected error:', sys.exc_info()[0])


def print_poloniex_ascii():
    # ASCII art generated at http://patorjk.com/software/taag/#p=display&f=Doom&t=Poloniex
    print('\n'
          '______     _             _           \n'
          '| ___ \   | |           (_)          \n'
          '| |_/ /__ | | ___  _ __  _  _____  __\n'
          '|  __/ _ \| |/ _ \| \'_ \\| |/ _ \\ \\/ /\n'
          '| | | (_) | | (_) | | | | |  __/>  < \n'
          '\_|  \___/|_|\___/|_| |_|_|\___/_/\_\\')

def print_poloniex_trade_history():
    start_date = datetime.date(2015, 1, 1)
    end_date = datetime.date.today()

    unix_start_dt = int(time.mktime(start_date.timetuple()))
    unix_end_dt = int(time.mktime(end_date.timetuple()))

    trade_history = connection.returnTradeHistory(start=unix_start_dt, end=unix_end_dt)

    for market_ticker, market_trade_hist in trade_history.items():
        print (market_ticker)
        for trade_data in market_trade_hist:
            print(trade_data)

def print_poloniex_balances():
    balances = connection.returnBalances()
    print('-----------------------------------------------------'
          '-----------------------------------------------------')
    print('Available BTC Balance: ' + balances['BTC'])
    print('-----------------------------------------------------'
          '-----------------------------------------------------')
    time.sleep(2)
    account_value = 0.0
    complete_balances = connection.returnCompleteBalances()

    for market, balances in complete_balances.items():
        if float(balances['btcValue']) > NEAR_ZERO_BALANCE:
            account_value += float(balances['btcValue'])

        if float(balances['btcValue']) > NEAR_ZERO_BALANCE or float(balances['onOrders']) > 0:
            mkt_str = ' --- {0: <6} ---  '.format(market)
            mkt_str += 'available: {0: >15} ---  '.format(balances['available'])
            mkt_str += 'onOrders: {0: >15} ---  '.format(balances['onOrders'])
            mkt_str += 'btcValue: {0: >11.8f} ---  '.format(float(balances['btcValue']))

            print(mkt_str)

    print('-----------------------------------------------------'
          '-----------------------------------------------------')
    print('Account Value: {:.8f} BTC'.format(account_value))
    print('-----------------------------------------------------'
          '-----------------------------------------------------')


def print_open_poloniex_orders():
    complete_balances = connection.returnOpenOrders('all')
    print('Open orders: ')
    for market, orders in complete_balances.items():
        if orders:
            for order in orders:
                temp_str = '   Market: {0: <9}'.format(market)
                temp_str += ' --- Order Type: {0: <4}'.format(order['type'])
                temp_str += ' --- Qty: {0: >15}'.format(order['startingAmount'])
                temp_str += ' --- Qty Remaining {0: >15}'.format(order['amount'])
                print(temp_str)
    print('\n')


def get_poloniex_available_btc():
    balance_btc = connection.returnAvailableAccountBalances()
    return balance_btc['exchange']['BTC']


def get_poloniex_account_value():
    account_value = 0.0
    complete_balances = connection.returnCompleteBalances()
    for market, balances in complete_balances.items():
        if float(balances['btcValue']) > NEAR_ZERO_BALANCE:
            account_value += float(balances['btcValue'])

    return account_value
