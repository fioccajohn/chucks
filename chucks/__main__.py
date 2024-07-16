from utils.token_manager import TokenManager
from trader.api import Trader
from marketdata.api import MarketData
from dataclasses import asdict

if __name__ == "__main__":
    token_manager = TokenManager()
    oauth_session = token_manager.get_oauth_session()

    trader = Trader(oauth_session)
    market_data = MarketData(oauth_session)
