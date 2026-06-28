
"""
Ghostrader Market Collector

Collects market information by using the Market Service.
"""

from services.market_service import MarketService


service = MarketService()


def get_stock_data(symbol: str):

    return service.get_stock_data(symbol)
