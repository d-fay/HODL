"""
THIS CLASS HANDLES ALL BITTREX API

Parameter configuration files are located in ../conf/settings.ini

    DOCUMENTATION for Bittrex():
        - https://bittrex.com/Home/Api
        - https://github.com/ericsomdahl/python-bittrex

"""
import sys

from hodl.ConfRetriever import ConfRetriever
from hodl.exchanges.Bittrex import Bittrex, API_V1_1, API_V2_0


conf = ConfRetriever()
NEAR_ZERO_BALANCE = float(conf.near_zero_balance)  # arbitrarily small value used to remove near-zero account balances

try:
    bittrex_v1 = Bittrex(conf.trex_key,
                         conf.trex_secret,
                         api_version=API_V1_1)

    bittrex_v2 = Bittrex(conf.trex_key,
                         conf.trex_secret,
                         api_version=API_V2_0)
except:
    print('Unexpected error:', sys.exc_info()[0])


def print_bittrex_ascii():
    # ASCII art generated at http://patorjk.com/software/taag/#p=display&f=Doom&t=Bittrex
    print('\n'
          '______ _ _   _                 \n'
          '| ___ (_) | | |                \n'
          '| |_/ /_| |_| |_ _ __ _____  __\n'
          '| ___ \ | __| __| \'__/ _ \\ \\/ /\n'
          '| |_/ / | |_| |_| | |  __/>  < \n'
          '\____/|_|\__|\__|_|  \___/_/\_\\')


def print_bittrex_trade_history():
    trade_history_data = []
    trade_history_response = bittrex_v2.get_order_history()
    if trade_history_response['success'] and trade_history_response['result'] is not None:
        trade_history_data = trade_history_response['result']
        print('Trade History for all currencies {}' .format(trade_history_data))
    if trade_history_data is None:
        print('Error: No trade history data returned from Bittrex')

def print_bittrex_api_error(response):
    print('Error with Bittrex API ::: {}: {}'.format(response['success'], response['result']))


def print_bittrex_balances():
    # TODO: CONVERT TO bittrex_v1 usage ?

    balances_data = []
    balances_response = bittrex_v2.get_balances()
    if balances_response['success'] and balances_response['result'] is not None:
        balances_data = balances_response['result']
    if balances_data is None:
        print('Error: No account balance data returned from Bittrex')
    else:

        btc_balance_response = bittrex_v2.get_balance('BTC')
        if btc_balance_response['success'] and btc_balance_response['result'] is not None:
            account_value_btc = 0
            btc_balance_data = btc_balance_response['result']
            btc_balance = btc_balance_data['Balance']
            btc_balance_available = btc_balance_data['Available']

            print('----------------------------------------------------'
                  '-----------------------------------------------------')
            print('Available BTC Balance: {:.8f}'.format(float(btc_balance_available)))
            print('----------------------------------------------------'
                  '-----------------------------------------------------')
            for market in balances_data:

                    mkt_balance = '{0:.8f}'.format(float(market['Balance']['Balance']))

                    mkt_ticker = market['Currency']['Currency']
                    mkt_price = 0
                    try:
                        mkt_price = market['BitcoinMarket']['Last']
                    except TypeError:
                        pass

                    mkt_value_btc = float(mkt_price) * float(mkt_balance)

                    # arbitrary number to remove near-zero balances
                    if float(mkt_value_btc) > NEAR_ZERO_BALANCE:

                        account_value_btc += mkt_value_btc
                        mkt_avail_bal = '{0:.8f}'.format(float(market['Balance']['Available']))

                        mkt_str = ' --- {0: <6} ---  '.format(mkt_ticker)
                        mkt_str += 'balance: {0: >15} ---  '.format(mkt_balance)
                        mkt_str += 'available: {0: >15} ---  '.format(mkt_avail_bal)
                        mkt_str += 'btcValue: {0: >11.8f} ---  '.format(mkt_value_btc)
                        print(mkt_str)

            account_value_btc += btc_balance

            print('----------------------------------------------------'
                  '-----------------------------------------------------')
            print('Account Value: {:.8f} BTC'
                  .format(account_value_btc))
            print('----------------------------------------------------'
                  '-----------------------------------------------------')
        else:
            print_bittrex_api_error(btc_balance_response)


def print_open_bittrex_orders():
    open_orders_response = bittrex_v1.get_open_orders()
    if open_orders_response['success'] and open_orders_response['result'] is not None:
        open_orders = open_orders_response['result']
        print("Open orders: ")
        for order in open_orders:
            if order:
                temp_str = '   Market: {0: <9}'.format(order['Exchange'])
                temp_str += ' --- Order Type: {0: <4}'.format(order['OrderType'])
                temp_str += ' --- Qty: {0: >15}'.format(order['Quantity'])
                temp_str += ' --- Qty Remaining {0: >15}'.format(order['QuantityRemaining'])
                print(temp_str)
        print('\n')
    else:
        print_bittrex_api_error(open_orders_response)


def get_bittrex_available_btc():
    btc_balance_response = bittrex_v2.get_balance('BTC')
    if btc_balance_response['success'] and btc_balance_response['result'] is not None:
        btc_balance_data = btc_balance_response['result']
        btc_balance_available = btc_balance_data['Available']
        return btc_balance_available
    else:
        print_bittrex_api_error(btc_balance_response)
        return None


def get_bittrex_account_value():
    # TODO: CONVERT TO bittrex_v1 usage ?
    balances_data = []
    account_value_btc = 0
    balances_response = bittrex_v2.get_balances()
    if balances_response['success'] and balances_response['result'] is not None:
        balances_data = balances_response['result']
    if balances_data is None:
        print('Error: No account balance data returned from Bittrex')
    else:
        btc_balance_response = bittrex_v2.get_balance('BTC')
        if btc_balance_response['success'] and btc_balance_response['result'] is not None:
            btc_balance_data = btc_balance_response['result']
            btc_balance = btc_balance_data['Balance']
            # btc_balance_available = btc_balance_data['Available']  # I think this value is included in btc_balance

            for market in balances_data:
                mkt_balance = '{0:.4f}'.format(float(market['Balance']['Balance']))
                mkt_price = 0
                try:
                    mkt_price = market['BitcoinMarket']['Last']
                except TypeError:
                    pass

                mkt_value_btc = float(mkt_price) * float(mkt_balance)

                # arbitrary number to remove near-zero balances
                if float(mkt_value_btc) > NEAR_ZERO_BALANCE:
                    account_value_btc += mkt_value_btc

            account_value_btc += btc_balance
        else:
            print_bittrex_api_error(btc_balance_response)
            return None

    return account_value_btc

