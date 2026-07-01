"""
=========================================================
GHO$TRADER Signal Engine

Purpose:
    Converts Ghost Score results into official trading
    signal language for the dashboard and intelligence layer.

Build:
    1.11.0 - Signal Engine Integration
=========================================================
"""

from dataclasses import dataclass


@dataclass
class SignalResult:
    symbol: str
    signal: str
    signal_strength: str
    risk_level: str
    action_message: str


class SignalEngine:
    """
    Official signal engine for Ghostrader.

    This engine converts a Ghost Score into simple,
    beginner-friendly trading signal language.
    """

    def generate_signal(self, score_result) -> SignalResult:
        symbol = score_result.symbol
        ghost_score = score_result.ghost_score
        confidence = score_result.confidence

        signal = self._get_signal(ghost_score)
        signal_strength = self._get_signal_strength(ghost_score, confidence)
        risk_level = self._get_risk_level(ghost_score, confidence)
        action_message = self._get_action_message(signal, risk_level)

        return SignalResult(
            symbol=symbol,
            signal=signal,
            signal_strength=signal_strength,
            risk_level=risk_level,
            action_message=action_message,
        )

    def _get_signal(self, ghost_score: int) -> str:
        if ghost_score >= 85:
            return "BUY"

        if ghost_score >= 70:
            return "WATCH"

        if ghost_score >= 50:
            return "CAUTION"

        return "AVOID"

    def _get_signal_strength(self, ghost_score: int, confidence: int) -> str:
        if ghost_score >= 85 and confidence >= 80:
            return "Strong"

        if ghost_score >= 70 and confidence >= 70:
            return "Moderate"

        if ghost_score >= 50:
            return "Weak"

        return "Negative"

    def _get_risk_level(self, ghost_score: int, confidence: int) -> str:
        if ghost_score >= 85 and confidence >= 80:
            return "Medium"

        if ghost_score >= 70:
            return "Medium-High"

        if ghost_score >= 50:
            return "High"

        return "Very High"

    def _get_action_message(self, signal: str, risk_level: str) -> str:
        if signal == "BUY":
            return (
                "Possible bullish setup. Review entry timing, risk level, "
                "position size, and broader market conditions before taking action."
            )

        if signal == "WATCH":
            return (
                "Promising setup, but not strong enough for automatic action. "
                "Continue monitoring price action and confirmation signals."
            )

        if signal == "CAUTION":
            return (
                "Mixed setup. Avoid rushing into a trade until stronger confirmation appears."
            )

        return (
            "Unfavorable setup. Ghostrader does not currently support a bullish action."
        )