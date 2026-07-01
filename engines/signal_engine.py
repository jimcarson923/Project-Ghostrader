"""
Ghostrader Signal Engine

Purpose:
    Convert a Ghost Score into a professional trading signal.

Version:
    1.0.0
"""


class SignalEngine:
    """
    Determines the trading signal based on the Ghost Score.
    """

    @staticmethod
    def calculate(score: int) -> str:
        """
        Returns a trading signal based on the Ghost Score.

        Parameters
        ----------
        score : int
            Ghost Score (0 - 100)

        Returns
        -------
        str
            Trading signal.
        """

        if score >= 90:
            return "🟢 STRONG BUY"

        elif score >= 70:
            return "🟢 BUY"

        elif score >= 40:
            return "🟡 HOLD"

        elif score >= 20:
            return "🟠 SELL"

        else:
            return "🔴 STRONG SELL"