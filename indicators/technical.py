import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator


def calculate_indicators(data: pd.DataFrame):
    """
    Calculates technical indicators for a stock.
    """

    close = data["Close"]

    # RSI (Relative Strength Index)
    rsi = RSIIndicator(close=close, window=14).rsi()

    # EMA 20
    ema20 = EMAIndicator(close=close, window=20).ema_indicator()

    # EMA 50
    ema50 = EMAIndicator(close=close, window=50).ema_indicator()

    return {
        "RSI": round(rsi.iloc[-1], 2),
        "EMA20": round(ema20.iloc[-1], 2),
        "EMA50": round(ema50.iloc[-1], 2),
    }
