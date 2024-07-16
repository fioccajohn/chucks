from utils.api_client import ApiClient
from trader.models import Order


class Trader:
    def __init__(self, oauth):

        self.api_client = ApiClient(oauth, api="trader")
        self.accounts = Accounts(self.api_client)
        self.orders = Orders(self.api_client)
        self.transactions = Transactions(self.api_client)
        self.user_preference = UserPreference(self.api_client)

        # TODO (all with internal functions)
        # Fetch and store user information
        # Fetch and store user preferences
        # Fetch and store account information
        # Initialize other services as needed


class Accounts:
    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_account_numbers(self, **kwargs):
        endpoint = f"/accounts/accountNumbers"
        return self.api_client.get(endpoint, **kwargs)

    def get_all_accounts(self, fields="positions", **kwargs):
        endpoint = f"/accounts"
        params = {"fields": fields}
        return self.api_client.get(endpoint, params=params, **kwargs)

    # TODO what's this for?
    def get_account(self, account_number, fields="positions", **kwargs):
        endpoint = f"/accounts/{account_number}"
        params = {"fields": fields}
        return self.api_client.get(endpoint, params=params, **kwargs)


class Orders:
    VALID_STATUSES = [
        "AWAITING_PARENT_ORDER",
        "AWAITING_CONDITION",
        "AWAITING_STOP_CONDITION",
        "AWAITING_MANUAL_REVIEW",
        "ACCEPTED",
        "AWAITING_UR_OUT",
        "PENDING_ACTIVATION",
        "QUEUED",
        "WORKING",
        "REJECTED",
        "PENDING_CANCEL",
        "CANCELED",
        "PENDING_REPLACE",
        "REPLACED",
        "FILLED",
        "EXPIRED",
        "NEW",
        "AWAITING_RELEASE_TIME",
        "PENDING_ACKNOWLEDGEMENT",
        "PENDING_RECALL",
        "UNKNOWN",
    ]

    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_account_orders(
        self, account_number, from_entered_time, to_entered_time, **kwargs
    ):
        """
        Get all orders for a specific account.

        :param account_number: The encrypted ID of the account (required)
        :param from_entered_time: Specifies that no orders entered before this time should be returned (required)
        :param to_entered_time: Specifies that no orders entered after this time should be returned (required)
        :param maxResults: The max number of orders to retrieve (optional, default is 3000)
        :param status: Specifies that only orders of this status should be returned (optional)
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If any of the input parameters are invalid

        For more details, see the official documentation: [link to documentation]
        """
        if not account_number:
            raise ValueError("Account number is required")
        if not from_entered_time:
            raise ValueError("fromEnteredTime is required")
        if not to_entered_time:
            raise ValueError("toEnteredTime is required")

        status = kwargs.get("status")
        if status and status not in self.VALID_STATUSES:
            raise ValueError(
                f"Invalid status: {status}. Must be one of {self.VALID_STATUSES}"
            )

        endpoint = f"/accounts/{account_number}/orders"
        params = {
            "fromEnteredTime": from_entered_time,
            "toEnteredTime": to_entered_time,
            "maxResults": kwargs.get("maxResults", 3000),
        }
        if status:
            params["status"] = status

        params.update(kwargs)

        return self.api_client.get(endpoint, params=params)

    def place_order(self, account_number, order: Order, **kwargs):
        """
        Place an order for a specific account.

        :param account_number: The encrypted ID of the account (required)
        :param order: The Order object to place (required)
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If the account number or order is invalid

        For more details, see the official documentation: [link to documentation]
        """
        if not account_number:
            raise ValueError("Account number is required")

        if not order:
            raise ValueError("Order object is required")

        endpoint = f"/accounts/{account_number}/orders"

        # TODO what is this doing? does it jsonify for the dataclass?
        order_data = order.__dict__
        return self.api_client.post(endpoint, data=order_data, **kwargs)

    def get_order(self, account_number, order_id, **kwargs):
        endpoint = f"/accounts/{account_number}/orders/{order_id}"
        return self.api_client.get(endpoint, **kwargs)

    def delete_order(self, account_number, order_id, **kwargs):
        endpoint = f"/accounts/{account_number}/orders/{order_id}"
        return self.api_client.delete(endpoint, **kwargs)

    def replace_order(self, account_number, order_id, order: Order, **kwargs):
        """
        Replace an order for a specific account.

        :param account_number: The encrypted ID of the account (required)
        :param order_id: The Order ID of the order to replace (required)
        :param order: The Order object to place (required)
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If the account number or order is invalid

        For more details, see the official documentation: [link to documentation]
        """
        if not account_number:
            raise ValueError("Account number is required")

        if not order_id:
            raise ValueError("Order ID number is required")

        if not order:
            raise ValueError("Order object is required")

        endpoint = f"/accounts/{account_number}/orders/{order_id}"
        order_data = order.__dict__
        return self.api_client.post(endpoint, data=order_data, **kwargs)

    def get_all_orders(self, from_entered_time, to_entered_time, **kwargs):
        """
        Get all orders for all accounts.

        :param from_entered_time: Specifies that no orders entered before this time should be returned (required)
        :param to_entered_time: Specifies that no orders entered after this time should be returned (required)
        :param maxResults: The max number of orders to retrieve (optional, default is 3000)
        :param status: Specifies that only orders of this status should be returned (optional)
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If any of the input parameters are invalid

        For more details, see the official documentation: [link to documentation]
        """
        if not from_entered_time:
            raise ValueError("fromEnteredTime is required")

        if not to_entered_time:
            raise ValueError("toEnteredTime is required")

        status = kwargs.get("status")
        if status and status not in self.VALID_STATUSES:
            raise ValueError(
                f"Invalid status: {status}. Must be one of {self.VALID_STATUSES}"
            )

        endpoint = "/orders"
        params = {
            "fromEnteredTime": from_entered_time,
            "toEnteredTime": to_entered_time,
            "maxResults": kwargs.get("maxResults", 3000),
        }
        if status:
            params["status"] = status

        params.update(kwargs)

        return self.api_client.get(endpoint, params=params)

    def preview_order(self, account_number, order: Order, **kwargs):
        """
        Preview an order for a specific account.

        :param account_number: The encrypted ID of the account (required)
        :param order: The Order object to place (required)
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If the account number or order is invalid

        For more details, see the official documentation: [link to documentation]
        """
        if not account_number:
            raise ValueError("Account number is required")

        if not order:
            raise ValueError("Order object is required")

        endpoint = f"/accounts/{account_number}/previewOrder"

        # TODO what is this doing? does it jsonify for the dataclass?
        order_data = order.__dict__
        return self.api_client.post(endpoint, data=order_data, **kwargs)


class Transactions:
    VALID_TRANSACTION_TYPES = [
        "TRADE",
        "RECEIVE_AND_DELIVER",
        "DIVIDEND_OR_INTEREST",
        "ACH_RECEIPT",
        "ACH_DISBURSEMENT",
        "CASH_RECEIPT",
        "CASH_DISBURSEMENT",
        "ELECTRONIC_FUND",
        "WIRE_OUT",
        "WIRE_IN",
        "JOURNAL",
        "MEMORANDUM",
        "MARGIN_CALL",
        "MONEY_MARKET",
        "SMA_ADJUSTMENT",
    ]

    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_all_transactions(self, account_number, start_date, end_date, **kwargs):
        """
        Get all transactions information for a specific account.

        :param account_number: The encrypted ID of the account (required)
        :param start_date: Specifies that no transactions entered before this time should be returned (required)
        :param end_date: Specifies that no transactions entered after this time should be returned (required)
        :param symbol: Filters all the transaction activities based on the symbol specified (optional)
        :param types: Specifies that only transactions of this status should be returned (optional)
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If any of the input parameters are invalid

        For more details, see the official documentation: [link to documentation]
        """
        if not account_number:
            raise ValueError("Account number is required")
        if not start_date:
            raise ValueError("Start date is required")
        if not end_date:
            raise ValueError("End date is required")

        types = kwargs.get("types")
        if types and types not in self.VALID_TRANSACTION_TYPES:
            raise ValueError(
                f"Invalid transaction type: {types}. Must be one of {self.VALID_TRANSACTION_TYPES}"
            )

        endpoint = f"/accounts/{account_number}/transactions"
        params = {"startDate": start_date, "endDate": end_date}
        if "symbol" in kwargs:
            params["symbol"] = kwargs["symbol"]
        if types:
            params["types"] = types

        params.update(kwargs)

        return self.api_client.get(endpoint, params=params)

    def get_transaction(self, account_number, transaction_id, **kwargs):
        """
        Get specific transaction information for a specific account.

        :param account_number: The encrypted ID of the account (required)
        :param transaction_id: The ID of the transaction being retrieved (required)
        :param kwargs: Additional parameters to pass to the API client
        :return: JSON response from the API
        :raises ValueError: If any of the input parameters are invalid

        For more details, see the official documentation: [link to documentation]
        """
        if not account_number:
            raise ValueError("Account number is required")
        if not transaction_id:
            raise ValueError("Transaction ID is required")

        endpoint = f"/accounts/{account_number}/transactions/{transaction_id}"
        return self.api_client.get(endpoint, **kwargs)


class UserPreference:
    def __init__(self, api_client=None):
        self.api_client = api_client

    def get_user_preference(self, **kwargs):
        endpoint = f"/userPreference"
        return self.api_client.get(endpoint, **kwargs)
