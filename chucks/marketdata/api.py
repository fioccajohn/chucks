from utils.api_client import ApiClient


class MarketData:
    def __init__(self, oauth):
        self.api_client = ApiClient(oauth, api="marketdata")
        self.instruments = Instruments(self.api_client)
        self.market_hours = MarketHours(self.api_client)
        self.movers = Movers(self.api_client)
        self.option_chains = OptionChains(self.api_client)
        self.price_history = PriceHistory(self.api_client)
        self.quotes = Quotes(self.api_client)


class Instruments:
    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_instruments(self, symbol, projection, **kwargs):
        """
        Get Instruments details by using different projections.

        :param symbols: List of symbols (strings) to query.
        :param projection: The projection type for the query.
        :param kwargs: Additional parameters to pass to the API client.
        :return: JSON response from the API.
        """
        # Join the symbols list into a comma-separated string
        symbol_str = ",".join(symbols)

        endpoint = f"/instruments"
        params = {"symbol": symbol_str, "projection": projection}

        # Pass the params and any additional kwargs to the API client
        return self.api_client.get(endpoint, params=params, **kwargs)

    def get_instruments_by_cusip(self, cusip_id, **kwargs):
        endpoint = f"/instruments/{cusip_id}"
        return self.api_client.get(endpoint, **kwargs)


class MarketHours:
    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_all_market_hours(self, markets, date=None, **kwargs):
        endpoint = f"/markets"
        params = {"markets": markets, "date": date}
        return self.api_client.get(endpoint, params=params, **kwargs)

    def get_market_hours(self, market_id, date=None, **kwargs):
        endpoint = f"/markets/{market_id}"
        params = {"date": date}
        return self.api_client.get(endpoint, params=params, **kwargs)


class Movers:
    VALID_SYMBOL_IDS = [
        "$DJI",
        "$COMPX",
        "$SPX",
        "NYSE",
        "NASDAQ",
        "OTCBB",
        "INDEX_ALL",
        "EQUITY_ALL",
        "OPTION_ALL",
        "OPTION_PUT",
        "OPTION_CALL",
    ]
    VALID_SORT_VALUES = ["VOLUME", "TRADES", "PERCENT_CHANGE_UP", "PERCENT_CHANGE_DOWN"]
    VALID_FREQUENCY_VALUES = [0, 1, 5, 10, 30, 60]

    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_movers(self, symbol_id, sort, frequency=0, **kwargs):
        """
        Get Movers for a specific index.

        :param symbol_id: Index Symbol (one of $DJI, $COMPX, $SPX, NYSE, NASDAQ, OTCBB, INDEX_ALL, EQUITY_ALL, OPTION_ALL, OPTION_PUT, OPTION_CALL)
        :param sort: Sort by a particular attribute (one of VOLUME, TRADES, PERCENT_CHANGE_UP, PERCENT_CHANGE_DOWN)
        :param frequency: Frequency (one of 0, 1, 5, 10, 30, 60)
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If any of the input parameters are invalid
        """
        if symbol_id not in self.VALID_SYMBOL_IDS:
            raise ValueError(
                f"Invalid symbol_id: {symbol_id}. Must be one of {self.VALID_SYMBOL_IDS}"
            )

        if sort not in self.VALID_SORT_VALUES:
            raise ValueError(
                f"Invalid sort value: {sort}. Must be one of {self.VALID_SORT_VALUES}"
            )

        if frequency not in self.VALID_FREQUENCY_VALUES:
            raise ValueError(
                f"Invalid frequency value: {frequency}. Must be one of {self.VALID_FREQUENCY_VALUES}"
            )

        endpoint = f"/movers/{symbol_id}"
        params = {"sort": sort, "frequency": frequency}
        return self.api_client.get(endpoint, params=params, **kwargs)


class OptionChains(object):
    VALID_CONTRACT_TYPES = ["CALL", "PUT", "ALL"]
    VALID_STRATEGIES = [
        "SINGLE",
        "ANALYTICAL",
        "COVERED",
        "VERTICAL",
        "CALENDAR",
        "STRANGLE",
        "STRADDLE",
        "BUTTERFLY",
        "CONDOR",
        "DIAGONAL",
        "COLLAR",
        "ROLL",
    ]
    VALID_EXP_MONTHS = [
        "JAN",
        "FEB",
        "MAR",
        "APR",
        "MAY",
        "JUN",
        "JUL",
        "AUG",
        "SEP",
        "OCT",
        "NOV",
        "DEC",
        "ALL",
    ]
    VALID_ENTITLEMENTS = ["PN", "NP", "PP"]

    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_chain(self, symbol, **kwargs):
        """
        Get option chain for an optionable symbol.

        :param symbol: Symbol to query (e.g., AAPL) (required)
        :param contractType: Contract type (one of CALL, PUT, ALL)
        :param strikeCount: The number of strikes to return above or below the at-the-money price
        :param includeUnderlyingQuote: Whether to include underlying quotes
        :param strategy: Option chain strategy (one of SINGLE, ANALYTICAL, COVERED, VERTICAL, CALENDAR, STRANGLE, STRADDLE, BUTTERFLY, CONDOR, DIAGONAL, COLLAR, ROLL)
        :param interval: Strike interval for spread strategy chains
        :param strike: Strike price
        :param range: Range (e.g., ITM, NTM, OTM)
        :param fromDate: From date (format: yyyy-MM-dd)
        :param toDate: To date (format: yyyy-MM-dd)
        :param volatility: Volatility to use in calculations (for ANALYTICAL strategy)
        :param underlyingPrice: Underlying price to use in calculations (for ANALYTICAL strategy)
        :param interestRate: Interest rate to use in calculations (for ANALYTICAL strategy)
        :param daysToExpiration: Days to expiration to use in calculations (for ANALYTICAL strategy)
        :param expMonth: Expiration month (one of JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC, ALL)
        :param optionType: Option type
        :param entitlement: Entitlement (one of PN, NP, PP)
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If any of the input parameters are invalid

        For more details, see the official documentation: [link to documentation]
        """

        if not symbol:
            raise ValueError("Symbol is required")

        contract_type = kwargs.get("contractType")
        if contract_type and contract_type not in self.VALID_CONTRACT_TYPES:
            raise ValueError(
                f"Invalid contractType: {contract_type}. Must be one of {self.VALID_CONTRACT_TYPES}"
            )

        strategy = kwargs.get("strategy")
        if strategy and strategy not in self.VALID_STRATEGIES:
            raise ValueError(
                f"Invalid strategy: {strategy}. Must be one of {self.VALID_STRATEGIES}"
            )

        exp_month = kwargs.get("expMonth")
        if exp_month and exp_month not in self.VALID_EXP_MONTHS:
            raise ValueError(
                f"Invalid expMonth: {exp_month}. Must be one of {self.VALID_EXP_MONTHS}"
            )

        entitlement = kwargs.get("entitlement")
        if entitlement and entitlement not in self.VALID_ENTITLEMENTS:
            raise ValueError(
                f"Invalid entitlement: {entitlement}. Must be one of {self.VALID_ENTITLEMENTS}"
            )

        endpoint = f"/chains"
        params = {"symbol": symbol}
        params.update(kwargs)

        return self.api_client.get(endpoint, params=params)


class OptionExpirationChain:
    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_expiration_chain(self, symbol, **kwargs):
        endpoint = f"/expirationchain"
        params = {"symbol": symbol}
        return self.api_client.get(endpoint, params=params, **kwargs)


class PriceHistory:
    VALID_PERIOD_TYPES = ["day", "month", "year", "ytd"]
    VALID_FREQUENCY_TYPES = {
        "day": ["minute"],
        "month": ["daily", "weekly"],
        "year": ["daily", "weekly", "monthly"],
        "ytd": ["daily", "weekly"],
    }
    VALID_PERIOD_VALUES = {
        "day": [1, 2, 3, 4, 5, 10],
        "month": [1, 2, 3, 6],
        "year": [1, 2, 3, 5, 10, 15, 20],
        "ytd": [1],
    }
    VALID_FREQUENCIES = {
        "minute": [1, 5, 10, 15, 30],
        "daily": [1],
        "weekly": [1],
        "monthly": [1],
    }

    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_price_history(self, symbol, periodType, frequencyType, **kwargs):
        """
        Get historical Open, High, Low, Close, and Volume for a given frequency.

        :param symbol: The Equity symbol used to look up price history (e.g., AAPL) (required)
        :param periodType: The chart period being requested (one of day, month, year, ytd) (required)
        :param period: The number of chart period types (depends on periodType)
        :param frequencyType: The time frequency type (depends on periodType) (required)
        :param frequency: The time frequency duration (depends on frequencyType)
        :param startDate: The start date in milliseconds since UNIX epoch
        :param endDate: The end date in milliseconds since UNIX epoch
        :param needExtendedHoursData: Whether to include extended hours data
        :param needPreviousClose: Whether to include the previous close price/date
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If any of the input parameters are invalid

        For more details, see the official documentation: [link to documentation]
        """
        if not symbol:
            raise ValueError("Symbol is required")

        if periodType not in self.VALID_PERIOD_TYPES:
            raise ValueError(
                f"Invalid periodType: {periodType}. Must be one of {self.VALID_PERIOD_TYPES}"
            )

        period = kwargs.get("period")
        if period is not None and period not in self.VALID_PERIOD_VALUES.get(
            periodType, []
        ):
            raise ValueError(
                f"Invalid period value: {period} for periodType {periodType}. Must be one of {self.VALID_PERIOD_VALUES.get(periodType, [])}"
            )

        if frequencyType not in self.VALID_FREQUENCY_TYPES.get(periodType, []):
            raise ValueError(
                f"Invalid frequencyType: {frequencyType} for periodType {periodType}. Must be one of {self.VALID_FREQUENCY_TYPES.get(periodType, [])}"
            )

        frequency = kwargs.get("frequency")
        if frequency is not None and frequency not in self.VALID_FREQUENCIES.get(
            frequencyType, []
        ):
            raise ValueError(
                f"Invalid frequency value: {frequency} for frequencyType {frequencyType}. Must be one of {self.VALID_FREQUENCIES.get(frequencyType, [])}"
            )

        endpoint = f"/pricehistory"
        params = {
            "symbol": symbol,
            "periodType": periodType,
            "frequencyType": frequencyType,
        }
        params.update(kwargs)

        return self.api_client.get(endpoint, params=params)


class Quotes:
    VALID_FIELDS = ["quote", "fundamental", "extended", "reference", "regular"]

    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_quotes(self, symbols, **kwargs):
        """
        Get quotes by list of symbols.

        :param symbols: List of symbols to look up a quote (e.g., "['AAPL', 'BAC', 'MSFT']") (required)
        :param fields: Request for subset of data by passing a comma separated list of root nodes
                       (possible values: quote, fundamental, extended, reference, regular)
        :param indicative: Include indicative symbol quotes for all ETF symbols in request (true or false)
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If any of the input parameters are invalid

        For more details, see the official documentation: [link to documentation]
        """
        if not symbols:
            raise ValueError("Symbols are required")

        symbol_str = ",".join(symbols)

        fields = kwargs.get("fields")
        if fields:
            invalid_fields = [
                field for field in fields.split(",") if field not in self.VALID_FIELDS
            ]
            if invalid_fields:
                raise ValueError(
                    f"Invalid fields: {invalid_fields}. Must be a comma separated list of {self.VALID_FIELDS}"
                )

        indicative = kwargs.get("indicative")
        if indicative is not None and not isinstance(indicative, bool):
            raise ValueError(
                f"Invalid indicative value: {indicative}. Must be a boolean (true or false)"
            )

        endpoint = f"/quotes"
        params = {"symbols": symbol_str}
        params.update(kwargs)

        return self.api_client.get(endpoint, params=params)

    def get_quote(self, symbol_id, **kwargs):
        """
        Get quote by a specific symbol.

        :param symbol_id: Symbol of the instrument (e.g., TSLA) (required)
        :param fields: Request for subset of data by passing a comma separated list of root nodes
                       (possible values: quote, fundamental, extended, reference, regular)
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If any of the input parameters are invalid

        For more details, see the official documentation: [link to documentation]
        """
        if not symbol_id:
            raise ValueError("Symbol ID is required")

        fields = kwargs.get("fields")
        if fields:
            invalid_fields = [
                field for field in fields.split(",") if field not in self.VALID_FIELDS
            ]
            if invalid_fields:
                raise ValueError(
                    f"Invalid fields: {invalid_fields}. Must be a comma separated list of {self.VALID_FIELDS}"
                )

        endpoint = f"/instruments/{symbol_id}"
        params = {}
        if fields:
            params["fields"] = fields
        params.update(kwargs)

        return self.api_client.get(endpoint, params=params)
