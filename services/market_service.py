"""
=========================================================
GHO$TRADER Market Service

Purpose:
    Provides live market snapshot data for the Ghostrader
    analysis workflow using yfinance.

Build:
    1.8.1 - Reliable Live Price Fix
=========================================================
"""

from dataclasses import dataclass

import yfinance as yf


@dataclass
class MarketSnapshot:
    symbol: str
    current_price: float
    daily_change: float
    daily_change_percent: float
    volume: int


class MarketService:
    """
    Market service for retrieving live stock market data.
    """

    def get_market_snapshot(self, symbol: str) -> MarketSnapshot:
        clean_symbol = symbol.strip().upper()

        if not clean_symbol:
            raise ValueError("Stock symbol cannot be empty.")

        ticker = yf.Ticker(clean_symbol)

        history = ticker.history(period="5d", interval="1d")

        if history.empty:
            raise ValueError(f"Could not retrieve market data for {clean_symbol}.")

        latest_row = history.iloc[-1]
        previous_row = history.iloc[-2] if len(history) > 1 else latest_row

        current_price = float(latest_row["Close"])
        previous_close = float(previous_row["Close"])
        volume = int(latest_row["Volume"])

        daily_change = current_price - previous_close

        if previous_close != 0:
            daily_change_percent = (daily_change / previous_close) * 100
        else:
            daily_change_percent = 0.0

        return MarketSnapshot(
            symbol=clean_symbol,
            current_price=round(current_price, 2),
            daily_change=round(daily_change, 2),
            daily_change_percent=round(daily_change_percent, 2),
            volume=volume,
        )
    