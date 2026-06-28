"""
Ghostrader Market Service

Responsible for communicating with external market data providers.

Current Provider:
    - Yahoo Finance

Future Providers:
    - Polygon
    - Finnhub
    - Alpha Vantage
    - Interactive Brokers
"""

import yfinance as yf


class MarketService:
    """
    Handles all communication with market data providers.
    """

    def get_stock_data(self, symbol: str):
        """
        Returns a snapshot of the current market data.
        """

        ticker = yf.Ticker(symbol)
        info = ticker.info

        return {
            "symbol": symbol,
            "company": info.get("longName"),
            "price": info.get("currentPrice"),
            "market_cap": info.get("marketCap"),
            "volume": info.get("volume"),
            "previous_close": info.get("previousClose"),
            "open": info.get("open"),
            "day_high": info.get("dayHigh"),
            "day_low": info.get("dayLow"),
        }

    def get_historical_data(
        self,
        symbol: str,
        period: str = "6mo",
        interval: str = "1d",
    ):
        """
        Returns historical OHLCV data as a Pandas DataFrame.
        """

        ticker = yf.Ticker(symbol)

        history = ticker.history(
            period=period,
            interval=interval,
        )

        return history
    
