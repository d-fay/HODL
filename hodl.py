""" BagHodler MAIN """
import sys
from sys import argv

from hodl.ConfRetriever import ConfRetriever
from hodl.exchanges.Polo import (print_poloniex_ascii,
                                 print_poloniex_balances,
                                 get_poloniex_account_value,
                                 get_poloniex_available_btc,
                                 print_open_poloniex_orders)
from hodl.exchanges.Trex import (print_bittrex_ascii,
                                 print_bittrex_balances,
                                 get_bittrex_account_value,
                                 get_bittrex_available_btc,
                                 print_open_bittrex_orders)

settings = ConfRetriever()

"""
BEFORE USE: 

 - Poloniex and/or Bittrex api keys must be provided in the file `conf/credentials.ini` 
 - Customizable parameters for the bot are contained in the file `conf/settings.ini`
        - Turn on/off support for desired exchanges
        - Ensure that only exchanges with provided API keys are set to `on`.
"""


def main():

    def start():
        """
        ASCII art generated at http://patorjk.com/software/taag/#p=display&f=Big%20Money-nw&t=hodl
        """
        print('\n\n'
              '$$\                       $$\ $$\     \n'
              '$$ |                      $$ |$$ |    \n'
              '$$$$$$$\   $$$$$$\   $$$$$$$ |$$ |    \n'
              '$$  __$$\ $$  __$$\ $$  __$$ |$$ |    \n'
              '$$ |  $$ |$$ /  $$ |$$ /  $$ |$$ |    \n'
              '$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |    \n'
              '$$ |  $$ |\$$$$$$  |\$$$$$$$ |$$ |    \n'
              '\__|  \__| \______/  \_______|\__|    \n'
              '                                      \n'
              '   $$$$$$$\ $$\   $$\ $$$$$$\$$$$\  $$$$$$\$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ \n'
              '  $$  _____|$$ |  $$ |$$  _$$  _$$\ $$  _$$  _$$\  \____$$\ $$  __$$\ $$ |  $$ |\n'
              '  \$$$$$$\  $$ |  $$ |$$ / $$ / $$ |$$ / $$ / $$ | $$$$$$$ |$$ |  \__|$$ |  $$ |\n'
              '   \____$$\ $$ |  $$ |$$ | $$ | $$ |$$ | $$ | $$ |$$  __$$ |$$ |      $$ |  $$ |\n'
              '  $$$$$$$  |\$$$$$$  |$$ | $$ | $$ |$$ | $$ | $$ |\$$$$$$$ |$$ |      \$$$$$$$ |\n'
              '  \_______/  \______/ \__| \__| \__|\__| \__| \__| \_______|\__|       \____$$ |\n'
              '                                                                      $$\   $$ |\n'
              '                                                                      \$$$$$$  |\n'
              '                                                                       \______/ ')

    def info():
        """
        Prints usage instructions
        :return: None
        """
        print('hodl requires the using one of the following flags:\n')
        print('     --overview: Print total and available btc balances')
        print('     --detailed: Print verbose account balances')
        print('\nPlease pass in required argument (ie: python3 hodl.py --overview)\n')

    def print_summary_ascii():
        print('   _____                                           \n'
              '  / ___/__  ______ ___  ____ ___  ____ ________  __\n'
              '  \__ \/ / / / __ `__ \/ __ `__ \/ __ `/ ___/ / / /\n'
              ' ___/ / /_/ / / / / / / / / / / / /_/ / /  / /_/ / \n'
              '/____/\__,_/_/ /_/ /_/_/ /_/ /_/\__,_/_/   \__, /  \n'
              '                                          /____/   ')

    def print_available_btc_balances():
        """
        Prints an overview of each exchanges account value and available BTC
        :return: None
        """
        print('===================================================================')
        print('Balances By Account (BTC)')
        print('-------------------------------------------------------------------')
        value_of_all_accounts = 0
        value_of_all_available_btc = 0

        if settings.poloniex == 'on':
            value_at_poloniex = float(get_poloniex_account_value())
            btc_avail_at_polo = float(get_poloniex_available_btc())

            value_of_all_accounts += value_at_poloniex
            value_of_all_available_btc += btc_avail_at_polo

            polo_str = '{0: >10} '.format('Poloniex')
            polo_str += ' --- Available: {0: >10.8f}'.format(btc_avail_at_polo)
            polo_str += ' --- Account Value: {0: >10.8f}'.format(value_at_poloniex)
            print(polo_str)

        if settings.bittrex == 'on':
            value_at_bittrex = float(get_bittrex_account_value())
            btc_avail_at_trex = float(get_bittrex_available_btc())

            value_of_all_accounts += value_at_bittrex
            value_of_all_available_btc += btc_avail_at_trex

            trex_str = '{0: >10} '.format('Bittrex')
            trex_str += ' --- Available: {0: >10.8f}'.format(btc_avail_at_trex)
            trex_str += ' --- Account Value: {0: >10.8f}'.format(value_at_bittrex)
            print(trex_str)

        print_total_value_accounts_summary(value_of_all_available_btc, value_of_all_accounts)

    def print_total_value_accounts_summary(combined_available_btc, combined_value_of_accounts):
        """
        Prints info about available BTC and combined BTC value across all exchanges
        :param combined_available_btc:
        :type combined_available_btc: float
        :param combined_value_of_accounts: pre-calculated total value of all active account connections
        :type combined_value_of_accounts: float
        :return: None
        """
        percent_btc = float(combined_available_btc / combined_value_of_accounts * 100)
        print('-------------------------------------------------------------------')
        print('Percentage of account in BTC: % {0: >3.2f}'.format(percent_btc))
        print('===================================================================')
        print('Total estimated value of all accounts: {0:.8f} BTC'.format(combined_value_of_accounts))
        print('===================================================================\n')

    def print_poloniex_detail_balances():
        """
        Print detailed balances of Poloniex account
        :return: None
        """
        if settings.poloniex == 'on':
            print_poloniex_ascii()
            print_poloniex_balances()
            print_open_poloniex_orders()

    def print_bittrex_detail_balances():
        """
        Print detailed balances of Bittrex account
        :return: None
        """
        if settings.bittrex == 'on':
            print_bittrex_ascii()
            print_bittrex_balances()
            print_open_bittrex_orders()

    def execute_printing_of_all_balances():
        """
        Used to execute printing of balances across all exchanges and
        then print a total combined value of all active exchanges.
        :return: None
        """
        print_poloniex_detail_balances()
        print_bittrex_detail_balances()

        print_summary_ascii()
        print_available_btc_balances()

    # parse command line args
    if len(argv) > 1:
        for arg in argv:
            if arg == '--overview' or arg == 'overview':
                start()
                print_available_btc_balances()              # --overview: Print total and available btc balances
                sys.exit(0)
            elif arg == '--detailed' or arg == 'detailed':
                start()
                execute_printing_of_all_balances()          # --detailed: Print verbose account balances
                sys.exit(0)
            elif arg == '--poloniex' or arg == 'poloniex':
                start()
                print_poloniex_balances()                   # --poloniex: Print only Poloniex balances
                sys.exit(0)
            elif arg == '--bittrex' or arg == 'bittrex':
                start()
                print_bittrex_balances()                    # --balances: Print only Bittrex balances
                sys.exit(0)

    start()   # ascii art
    info()    # if no parameter is passed in, print help screen
    sys.exit(0)


if __name__ == '__main__':
    main()
