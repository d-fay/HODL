from configparser import ConfigParser


class ConfRetriever(object):

    def __init__(self):

        config = ConfigParser()
        config.read('conf/credentials.ini')
        self.binance_key = config.get('api_keys_binance', 'key')
        self.binance_secret = config.get('api_keys_binance', 'secret')
        self.polo_key = config.get('api_keys_poloniex', 'key')
        self.polo_secret = config.get('api_keys_poloniex', 'secret')
        self.trex_key = config.get('api_keys_bittrex', 'key')
        self.trex_secret = config.get('api_keys_bittrex', 'secret')

        settings = ConfigParser()
        settings.read('conf/settings.ini')
        self.binance = settings.get('params', 'binance')
        self.bittrex = settings.get('params', 'bittrex')
        self.poloniex = settings.get('params', 'poloniex')
        self.near_zero_balance = settings.get('params', 'near_zero_balance')
