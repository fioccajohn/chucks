# coding: utf-8
import json
from pathlib import Path

import pandas as pd
from schwab.auth import easy_client

# TODO: Could this work as a massive wrapper around the schwab-py package?


@pd.api.extensions.register_dataframe_accessor("chucks")
class ChucksAccessor:


    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj
        self.some_other_namespace = NamespaceClassForLikePriceHistory
        self.another_namespace = NamespaceClassForLikeQuote

    @staticmethod
    def _validate(response_obj):
        # TODO: what's the input here?
        # TODO
        pass

    @staticmethod
    def from_price_history(response_obj):
        # TODO
        return pd.json_normalize(response_obj, record_path="candles")

    @staticmethod
    def from_XXX(response_obj):
        # TODO
        pass

    @property
    def something(self):
        # TODO
        pass

    def plot(self):
        # TODO
        pass


if __name__ == "__main__":

    CONFIG_FILE = Path("/Users/johnfiocca/.config/chucks/config.json")

    with open(CONFIG_FILE) as f:
        j = json.load(f)

    c = easy_client(
        j.get("client_id"),
        j.get("client_secret"),
        j.get("redirect_uri"),
        Path("/Users/johnfiocca/.config/chucks/access_token.json"),
    )
    r = c.get_price_history("SPY")
    df = pd.DataFrame.chucks.from_price_history(r)
