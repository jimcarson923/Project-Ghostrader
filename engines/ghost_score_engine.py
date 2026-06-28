"""
Ghostrader Ghost Score Engine

Version: 1.0

Purpose:
    Converts technical indicators into a single Ghost Score.

Author:
    Project Ghostrader
"""


class GhostScoreEngine:
    """
    Calculates the Ghost Score from technical indicators.
    """

    @staticmethod
    def calculate(data):

        latest = data.iloc[-1]

        score = 0

        reasons = []

        close = latest["Close"]
        sma20 = latest["SMA20"]
        sma50 = latest["SMA50"]
        rsi = latest["RSI"]

        # -------------------------------------------------
        # Trend
        # -------------------------------------------------

        if close > sma20:
            score += 20
            reasons.append("Price above SMA20")
        else:
            reasons.append("Price below SMA20")

        if close > sma50:
            score += 20
            reasons.append("Price above SMA50")
        else:
            reasons.append("Price below SMA50")

        if sma20 > sma50:
            score += 20
            reasons.append("SMA20 above SMA50")
        else:
            reasons.append("SMA20 below SMA50")

        # -------------------------------------------------
        # RSI
        # -------------------------------------------------

        if 40 <= rsi <= 60:
            score += 20
            reasons.append("RSI Neutral")

        elif rsi < 30:
            score += 10
            reasons.append("RSI Oversold")

        else:
            reasons.append("RSI Outside Neutral Range")

        # -------------------------------------------------
        # Trend Bonus
        # -------------------------------------------------

        if close > sma20 and close > sma50:
            score += 20
            reasons.append("Strong Bullish Trend")

        # -------------------------------------------------
        # Recommendation
        # -------------------------------------------------

        if score >= 80:
            recommendation = "STRONG BUY"

        elif score >= 60:
            recommendation = "BUY"

        elif score >= 40:
            recommendation = "WATCH"

        elif score >= 20:
            recommendation = "WEAK"

        else:
            recommendation = "AVOID"

        return {
            "score": score,
            "recommendation": recommendation,
            "close": close,
            "sma20": sma20,
            "sma50": sma50,
            "rsi": rsi,
            "reasons": reasons,
        }