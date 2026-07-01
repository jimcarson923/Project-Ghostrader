"""
=========================================================
GHO$TRADER Historical Data Service

Purpose:
    Downloads and provides historical market data for
    technical indicator calculations.

Build:
    1.19.0 - Historical Data Service
=========================================================
"""

from dataclasses import dataclass
from datetime import datetime, timedelta

import pandas as pd
import yfinance as yf


@dataclass
class HistoricalDataResult:
    symbol: str
    dataframe: pd.DataFrame
    start_date: str
    end_date: str
    trading_days: int


class HistoricalDataService:
    """
    Retrieves historical OHLCV market data.

    Future engines (RSI, MACD, EMA, SMA, ATR,
    Bollinger Bands, etc.) will all use this service.
    """

    def get_history(
        self,
        symbol: str,
        months: int = 12,
    ) -> HistoricalDataResult:

        clean_symbol = symbol.strip().upper()

        if not clean_symbol:
            raise ValueError("Stock symbol cannot be empty.")

        end_date = datetime.today()
        start_date = end_date - timedelta(days=months * 30)

        df = yf.download(
            clean_symbol,
            start=start_date.strftime("%Y-%m-%d"),
            end=end_date.strftime("%Y-%m-%d"),
            progress=False,
            auto_adjust=True,
        )

        if df.empty:
            raise ValueError(
                f"No historical market data found for {clean_symbol}."
            )

        df = df.dropna()

        return HistoricalDataResult(
            symbol=clean_symbol,
            dataframe=df,
            start_date=start_date.strftime("%Y-%m-%d"),
            end_date=end_date.strftime("%Y-%m-%d"),
            trading_days=len(df),
        )

    def get_closing_prices(
        self,
        symbol: str,
        months: int = 12,
    ) -> pd.Series:
        """
        Convenience method for indicator engines.
        """

        result = self.get_history(symbol, months)
        return result.dataframe["Close"]

    def get_volume(
        self,
        symbol: str,
        months: int = 12,
    ) -> pd.Series:
        """
        Returns historical trading volume.
        """

        result = self.get_history(symbol, months)
        return result.dataframe["Volume"]