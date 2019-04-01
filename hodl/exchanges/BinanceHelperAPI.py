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


def calc_price_of_market(mrkt_ticker, aggressiveness=0.5):
    """
    Calculates the price of a market using the spread
        aggressiveness = 1.0 : uses the highest bid (best when selling)
        aggressiveness = 0.0 : uses the lowest ask (best when buying)
        aggressiveness = 0.5 : middle of spread

    :param aggressiveness: Ratio used to control how aggressive
    :type aggressiveness: float (zero to one)
    :return: calculated price for asset
    :rtype: float
    """
    depth = client.get_order_book(symbol=mrkt_ticker)
    highest_bid = float(depth['bids'][0][0])
    lowest_ask = float(depth['asks'][0][0])
    spread = highest_bid - lowest_ask
    btc_price = float((spread * aggressiveness) + lowest_ask)
    return round(btc_price, 8)


def print_formatted_balance(asset_ticker, asset_balance, asset_free_bal, mkt_btc_value):

    mkt_str = ' --- {0: <6} ---  '.format(asset_ticker)
    mkt_str += 'balance: {0: >15.8f} --- '.format(asset_balance)
    mkt_str += 'available/free: {0: >15.8f} --- '.format(asset_free_bal)
    # mkt_str += 'onOrders/locked: {0: >15.8f} --- '.format(asset_locked_bal)
    mkt_str += 'btcValue: {0: >11.8f} --- '.format(mkt_btc_value)
    print(mkt_str)


def print_binance_balances():
    account_value_btc = 0
    btc_balance_available = get_binance_available_btc()
    print('------------------------------------------------------'
          '------------------------------------------------------')
    print('Available BTC Balance: {:.8f}'.format(float(btc_balance_available)))
    print('------------------------------------------------------'
          '------------------------------------------------------')
    info = client.get_account()

    for asset in info['balances']:
        asset_free_bal = float(asset['free'])
        asset_locked_bal = float(asset['locked'])
        asset_balance = asset_free_bal + asset_locked_bal
        asset_ticker = asset['asset']
        # If coin is not BTC we need market price (in btc)
        mkt_btc_value = 0

        if 'BTC' not in asset_ticker:

            if asset_balance > NEAR_ZERO_BALANCE:
                mkt_ticker = '{}BTC'.format(asset_ticker)

                # There has to be a better way to handle this. Can we obtain a
                # list of market tickers for each coin we hold and conditionally
                # query them? Right now a handfull of coins that show up in this
                # list do not have {}BTC markets. So the below query throws an
                # error when we provide an invalid market ticker.
                try:
                    mkt_price = calc_price_of_market(mkt_ticker)
                    mkt_btc_value = mkt_price * asset_balance
                except:
                    # print('Market: {} does not exist? '.format(mkt_ticker))
                    # print('Unexpected error:', sys.exc_info()[0])
                    pass

                if mkt_btc_value > NEAR_ZERO_BALANCE:
                    account_value_btc += mkt_btc_value
                    print_formatted_balance(asset_ticker, asset_balance, asset_free_bal, mkt_btc_value)

        elif asset_ticker == 'BTC':

            if asset_balance > NEAR_ZERO_BALANCE:
                account_value_btc += mkt_btc_value
                print_formatted_balance(asset_ticker, asset_balance, asset_free_bal, asset_balance)

    account_value_btc += btc_balance_available
    account_value_btc += get_binance_open_buy_orders_value()
    print('------------------------------------------------------'
          '------------------------------------------------------')
    print('Account Value: {:.8f} BTC'
          .format(account_value_btc))
    print('------------------------------------------------------'
          '------------------------------------------------------')


def get_binance_account_value():
    account_value_btc = 0
    info = client.get_account()

    for asset in info['balances']:
        asset_free_bal = float(asset['free'])
        asset_locked_bal = float(asset['locked'])
        asset_balance = asset_free_bal + asset_locked_bal
        asset_ticker = asset['asset']
        mkt_btc_value = 0

        if 'BTC' not in asset_ticker:

            if asset_balance > NEAR_ZERO_BALANCE:
                mkt_ticker = '{}BTC'.format(asset_ticker)

                try:
                    mkt_price = calc_price_of_market(mkt_ticker)
                    mkt_btc_value = mkt_price * asset_balance
                except:
                    # print('Market: {} does not exist? '.format(mkt_ticker))
                    # print('Unexpected error:', sys.exc_info()[0])
                    pass

                if mkt_btc_value > NEAR_ZERO_BALANCE:
                    account_value_btc += mkt_btc_value

        elif asset_ticker == 'BTC':

            if asset_balance > NEAR_ZERO_BALANCE:
                account_value_btc += mkt_btc_value

    account_value_btc += get_binance_available_btc()
    account_value_btc += get_binance_open_buy_orders_value()

    return float(account_value_btc)


def get_binance_available_btc():
    btc_balance_info = client.get_asset_balance(asset='BTC')
    btc_available = float(btc_balance_info['free'])
    return btc_available


def print_binance_open_orders():
    print('Open orders: ')
    orders = client.get_open_orders()
    for order in orders:
        mkt_str = ' {0: <6} --- '.format(order['symbol'])
        mkt_str += 'orderType: {}   ---  side: {}  \n\t'.format(order['type'], order['side'])
        mkt_str += '--- price: {0: >11.8f} ---  '.format(float(order['price']))
        mkt_str += 'origQty: {0: >15} ---  '.format(order['origQty'])
        mkt_str += 'executedQty: {0: >15} ---  \n'.format(order['executedQty'])
        print(mkt_str)
    print('\n')


def get_binance_open_buy_orders_value():
    orders = client.get_open_orders()
    open_orders_val = 0.0
    for order in orders:
        if order['side'] == 'BUY':
            order_value = float(order['origQty']) * float(order['price'])
            open_orders_val += order_value
    return open_orders_val
