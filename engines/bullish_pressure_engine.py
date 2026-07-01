"""
=========================================================
GHO$TRADER Bullish Pressure Engine

Purpose:
    Detects whether a stock is showing early signs of
    bullish pressure based on Ghostrader analysis results.

Build:
    1.33.0 - Bullish Pressure Engine Foundation
=========================================================
"""

from dataclasses import dataclass


@dataclass
class BullishPressureResult:
    symbol: str
    pressure_score: int
    pressure_level: str
    bullish_factors: list[str]
    caution_factors: list[str]
    summary: str


class BullishPressureEngine:
    """
    Foundation engine for detecting bullish pressure.

    Future builds will expand this with:
    - RSI confirmation
    - Moving average alignment
    - MACD confirmation
    - Relative volume
    - Breakout detection
    - Institutional accumulation signals
    """

    def analyze(self, market_snapshot, technical_result, score_result, signal_result) -> BullishPressureResult:
        score = 0
        bullish_factors = []
        caution_factors = []

        symbol = market_snapshot.symbol

        if market_snapshot.daily_change_percent > 2:
            score += 25
            bullish_factors.append("Strong positive daily price movement")
        elif market_snapshot.daily_change_percent > 0:
            score += 15
            bullish_factors.append("Positive daily price movement")
        else:
            caution_factors.append("Price is not currently moving higher")

        if market_snapshot.volume >= 10_000_000:
            score += 25
            bullish_factors.append("Very high trading volume")
        elif market_snapshot.volume >= 5_000_000:
            score += 18
            bullish_factors.append("High trading volume")
        elif market_snapshot.volume >= 1_000_000:
            score += 10
            bullish_factors.append("Normal trading volume")
        else:
            caution_factors.append("Low trading volume")

        if technical_result.trend_direction in ["Bullish", "Slightly Bullish"]:
            score += 20
            bullish_factors.append(f"Trend direction is {technical_result.trend_direction}")
        else:
            caution_factors.append(f"Trend direction is {technical_result.trend_direction}")

        if technical_result.momentum_status in ["Strong Positive", "Positive"]:
            score += 15
            bullish_factors.append(f"Momentum status is {technical_result.momentum_status}")
        else:
            caution_factors.append(f"Momentum status is {technical_result.momentum_status}")

        if score_result.ghost_score >= 80:
            score += 10
            bullish_factors.append("Ghost Score supports bullish pressure")
        else:
            caution_factors.append("Ghost Score does not strongly confirm bullish pressure")

        if signal_result.signal == "BUY":
            score += 5
            bullish_factors.append("Signal Engine generated a BUY signal")
        else:
            caution_factors.append(f"Signal Engine generated {signal_result.signal}")

        pressure_score = max(0, min(score, 100))
        pressure_level = self._get_pressure_level(pressure_score)

        if not bullish_factors:
            bullish_factors.append("No major bullish pressure factors detected")

        if not caution_factors:
            caution_factors.append("No major caution factors detected")

        summary = (
            f"{symbol} has a bullish pressure score of {pressure_score}/100, "
            f"classified as {pressure_level}."
        )

        return BullishPressureResult(
            symbol=symbol,
            pressure_score=pressure_score,
            pressure_level=pressure_level,
            bullish_factors=bullish_factors,
            caution_factors=caution_factors,
            summary=summary,
        )

    def _get_pressure_level(self, pressure_score: int) -> str:
        if pressure_score >= 85:
            return "Very High"

        if pressure_score >= 70:
            return "High"

        if pressure_score >= 50:
            return "Moderate"

        if pressure_score >= 30:
            return "Low"

        return "Very Low"