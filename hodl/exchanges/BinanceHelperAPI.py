"""
THIS CLASS HANDLES ALL BINANCE TRADE EXECUTION

    Resources:
        - https://github.com/binance-exchange/binance-official-api-docs
        - http://python-binance.readthedocs.io/en/latest/index.html

    Trading Rule:
        - https://support.binance.com/hc/en-us/articles/115000594711-Trading-Rule

Parameter configuration files are located in ../conf/settings.ini
"""
import datetime as dt
import logging
import sys
import time

from hodl.ConfRetriever import ConfRetriever

from binance.client import Client


conf = ConfRetriever()
NEAR_ZERO_BALANCE = float(conf.near_zero_balance)  # arbitrarily small value used to remove near-zero account balances

try:
    client = Client(conf.binance_key, conf.binance_secret)

except:
    print('Unexpected error:', sys.exc_info()[0])


def print_binance_ascii():
    # ASCII art generated at http://patorjk.com/software/taag/#p=display&f=Doom&t=Bittrex
    print('\n\n'
          '______ _                            \n'
          '| ___ (_)                           \n'
          '| |_/ /_ _ __   __ _ _ __   ___ ___ \n'
          '| ___ \\ | \'_ \\ / _` | \'_ \\ / __/ _ \\\n'
          '| |_/ / | | | | (_| | | | | (_|  __/\n'
          '\____/|_|_| |_|\__,_|_| |_|\___\___|')


def print_binance_balances():
    print(' - - - GET BINANCE BALANCES - - - ')
    # TODO: Beautify
    info = client.get_account()
    for asset in info['balances']:
        if float(asset['free']) > NEAR_ZERO_BALANCE or float(asset['locked']) > NEAR_ZERO_BALANCE:
            print(asset)


def get_binance_account_value():
    print(' - - - GET BINANCE ACCOUNT VAL - - - ')
    # TODO: Beautify
    print('print: info = client.get_account() ')
    info = client.get_account()
    for asset in info['balances']:
        if float(asset['free']) > NEAR_ZERO_BALANCE or float(asset['locked']) > NEAR_ZERO_BALANCE:
            print(' {} ---- locked: {} ---- free {}'.format(asset['asset'], asset['free'], asset['locked']))
    return 0


def get_binance_available_btc():
    print(' - - - GET BINANCE AVAILABLE BTC - - - ')
    # TODO: Beautify
    btc_balance_info = client.get_asset_balance(asset='BTC')
    print(btc_balance_info)
    return 0


def print_open_binance_orders():
    print(' - - - PRINT OPEN BINANCE ORDERS - - - ')
    # TODO: Beautify
    print('print:     orders = client.get_open_orders()')
    orders = client.get_open_orders()
    print(orders)

