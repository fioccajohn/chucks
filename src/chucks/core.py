# coding: utf-8
import json
from pathlib import Path
import pandas as pd

CONFIG_FILE = Path('/Users/johnfiocca/.config/chucks/config.json')

with open(CONFIG_FILE) as f:
            j = json.load(f)

@pd.api.extensions.register_dataframe_accessor("chucks")
class ChucksAccessor:
    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj
        self.some_other_namespace = NamespaceClassForLikePriceHistory
        self.another_namespace = NamespaceClassForLikeQuote

    @staticmethod
    def _validate(obj):
        pass

    @staticmethod
    def from_candles(obj):
        return pd.json_normalize(obj, record_path='candles')

    @property
    def price_history_dataframe(self):
        pass

    def plot(self):
        pass

if __name__ == "__main__":
    c = easy_client(j.get('client_id'), j.get('client_secret'), j.get('redirect_uri'), Path('/Users/johnfiocca/.config/chucks/access_token.json'))
    r = c.get_price_history('SPY')
    df = pd.json_normalize(r.json())

