import logging
import pandas as pd

logger = logging.getLogger(__name__)

@pd.api.extensions.register_dataframe_accessor("chucks")
class ChucksAccessor:
    """Extension to provide more finance dataframe methods."""

    def __init__(self, pandas_obj):
        self._validate(pandas_obj)
        self._obj = pandas_obj

    @staticmethod
    def _validate(response_obj):
        pass

    @staticmethod
    def from_candles(price_history_responses):
        """Returns a dataframe of the candles responses.

        Can take multiple responses and output one df.

        Args:
            price_history_responses (iterable): An iterable of price history responses.

        """
        df =  pd.concat(pd.json_normalize(c.json(), record_path="candles", meta=['symbol', 'empty']) for c in price_history_responses)

        return df

    @staticmethod
    def from_accounts(accounts_response):
        df =  pd.json_normalize(accounts_response.json(), sep='_')
        return df

    @staticmethod
    def from_instruments(instruments_response):
        df =  pd.json_normalize(instruments_response.json(), record_path="instruments")
        return df

    @staticmethod
    def static_method(response_obj):
        pass

    def some_method(self):
        pass

    def convenience_method_like_send_all_instruments_to_price_history(self):
        pass

    def what_about_adding_field_like_response_type_to_df(self):
        pass
