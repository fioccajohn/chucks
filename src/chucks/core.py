import logging
from functools import wraps

import pandas as pd

logger = logging.getLogger(__name__)


def _client_required(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self._client is None:
            error_message = "API client is not set. Use `set_client` to initialize it before using this method."
            raise ValueError(error_message)
        return func(self, *args, **kwargs)

    return wrapper

@pd.api.extensions.register_dataframe_accessor("chucks")
class ChucksAccessor:
    """Extension to provide more finance dataframe methods."""

    _client = None

    @classmethod
    def set_client(cls, client):
        cls._client = client

    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    @staticmethod
    def _validate(response_obj):
        pass

    @staticmethod
    def _convert_datetime_to_ms(df: pd.DataFrame) -> pd.DataFrame:
        return df.astype({"datetime": "datetime64[ms]"})

    @staticmethod
    def _set_index_datetime_symbol(df: pd.DataFrame) -> pd.DataFrame:
        return df.set_index(["datetime", "symbol"])

    @staticmethod
    def from_candles(price_history_responses):
        """Returns a dataframe of the candles responses.

        Can take multiple responses and output one df.

        Args:
            price_history_responses (iterable): An iterable of price history responses.

        """
        return (
            pd.concat(
                pd.json_normalize(c.json(), record_path="candles", meta=["symbol", "empty"])
                for c in price_history_responses
            )
            .pipe(ChucksAccessor._convert_datetime_to_ms)
            .pipe(ChucksAccessor._set_index_datetime_symbol)
        )

    @staticmethod
    def from_accounts(accounts_response):
        return pd.json_normalize(accounts_response.json(), sep="_")

    @staticmethod
    def from_instruments(instruments_response):
        return pd.json_normalize(instruments_response.json(), record_path="instruments").set_index('symbol')

    @staticmethod
    def static_method(response_obj):
        pass

    @_client_required
    def get_quotes_for_symbols(self):
        symbols = self._get_unique_symbols_from_index()
        response = self._client.get_quotes(symbols)
        response_dict = response.json()

        # TODO: How to return certain "fields"? filter after creating all? only request subset if set using the client values? Column multiindex?
        return pd.concat([pd.DataFrame.from_dict(response_dict.get(k) for k in response_dict)]).set_index('symbol')
        # .filter(regex='fundamental')


    def _get_unique_symbols_from_index(self):
        return self._obj.index.get_level_values('symbol').unique()


    def some_method(self):
        pass

    def convenience_method_like_send_all_instruments_to_price_history(self):
        pass

    def what_about_adding_field_like_response_type_to_df(self):
        pass
