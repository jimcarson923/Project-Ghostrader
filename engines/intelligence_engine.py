"""
Ghostrader Intelligence Engine

Converts market data into a human-readable market assessment.
"""


class IntelligenceEngine:

    @staticmethod
    def analyze(result: dict) -> dict:
        """
        Analyze Ghost Score results and generate
        market intelligence.
        """

        score = result["score"]
        rsi = result["rsi"]
        price = result["close"]
        sma20 = result["sma20"]
        sma50 = result["sma50"]

        # -------------------------
        # Trend
        # -------------------------

        if price > sma20 and price > sma50:
            trend = "Bullish"
        elif price < sma20 and price < sma50:
            trend = "Bearish"
        else:
            trend = "Neutral"

        # -------------------------
        # Momentum
        # -------------------------

        if rsi >= 60:
            momentum = "Strong"

        elif rsi >= 45:
            momentum = "Neutral"

        else:
            momentum = "Weak"

        # -------------------------
        # Risk
        # -------------------------

        if score >= 80:
            risk = "Low"

        elif score >= 50:
            risk = "Medium"

        else:
            risk = "High"

        confidence = max(0, min(score + 20, 100))

        summary = (
            f"{trend} trend detected. "
            f"Momentum is {momentum.lower()}. "
            f"Current trading risk is {risk.lower()}."
        )

        return {
            "trend": trend,
            "momentum": momentum,
            "risk": risk,
            "confidence": confidence,
            "summary": summary,
        }