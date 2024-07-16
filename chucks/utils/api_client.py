import requests

TRADER_BASE_URL = "https://api.schwabapi.com/trader/v1"
MARKET_DATA_BASE_URL = "https://api.schwabapi.com/marketdata/v1"


class ApiClient:

    def __init__(self, oauth_session, api):
        self.oauth = oauth_session

        if api == "trader":
            self.base_url = TRADER_BASE_URL
        elif api == "marketdata":
            self.base_url = MARKET_DATA_BASE_URL
        else:
            raise ValueError(f"api for {api} not found.")

    def get(self, endpoint, params=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.oauth.get(url, params=params, **kwargs)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.oauth.post(url, json=data, **kwargs)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.oauth.put(url, json=data, **kwargs)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint, data=None, **kwargs):
        url = f"{self.base_url}{endpoint}"
        response = self.oauth.delete(url, **kwargs)
        response.raise_for_status()
        return response.json()
