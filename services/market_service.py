"""
=========================================================
GHO$TRADER Market Service

Purpose:
    Provides market snapshot data for the Ghostrader analysis
    workflow.

Build:
    1.6.0 - Market Service Foundation
=========================================================
"""

from dataclasses import dataclass


@dataclass
class MarketSnapshot:
    symbol: str
    current_price: float
    daily_change: float
    daily_change_percent: float
    volume: int


class MarketService:
    """
    Temporary market service.

    This build creates the official service layer that the
    Analyze button will use in the next milestone.

    Live market data will be added later.
    """

    def get_market_snapshot(self, symbol: str) -> MarketSnapshot:
        clean_symbol = symbol.strip().upper()

        if not clean_symbol:
            raise ValueError("Stock symbol cannot be empty.")

        base_value = sum(ord(char) for char in clean_symbol)

        current_price = 100 + (base_value % 250)
        daily_change = round(((base_value % 21) - 10) * 0.37, 2)
        daily_change_percent = round((daily_change / current_price) * 100, 2)
        volume = 1_000_000 + (base_value * 12_345)

        return MarketSnapshot(
            symbol=clean_symbol,
            current_price=float(current_price),
            daily_change=daily_change,
            daily_change_percent=daily_change_percent,
            volume=volume,
        )