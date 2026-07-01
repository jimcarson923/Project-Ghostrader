"""
=========================================================
GHO$TRADER Technical Indicator Engine

Purpose:
    Provides the foundation for technical indicator analysis.

Build:
    1.16.0 - Technical Indicator Foundation
=========================================================
"""

from dataclasses import dataclass


@dataclass
class TechnicalIndicatorResult:
    symbol: str
    trend_direction: str
    momentum_status: str
    volume_status: str
    technical_summary: str


class TechnicalIndicatorEngine:
    """
    Foundation engine for technical indicators.

    Future builds will add:
    - RSI
    - MACD
    - EMA 20 / 50 / 200
    - Bollinger Bands
    - ATR
    - Relative volume
    """

    def analyze(self, market_snapshot) -> TechnicalIndicatorResult:
        symbol = market_snapshot.symbol
        daily_change_percent = market_snapshot.daily_change_percent
        volume = market_snapshot.volume

        trend_direction = self._get_trend_direction(daily_change_percent)
        momentum_status = self._get_momentum_status(daily_change_percent)
        volume_status = self._get_volume_status(volume)

        technical_summary = (
            f"{symbol} is currently showing a {trend_direction.lower()} short-term trend. "
            f"Momentum is classified as {momentum_status.lower()}, and volume is "
            f"classified as {volume_status.lower()}."
        )

        return TechnicalIndicatorResult(
            symbol=symbol,
            trend_direction=trend_direction,
            momentum_status=momentum_status,
            volume_status=volume_status,
            technical_summary=technical_summary,
        )

    def _get_trend_direction(self, daily_change_percent: float) -> str:
        if daily_change_percent >= 1.5:
            return "Bullish"

        if daily_change_percent > 0:
            return "Slightly Bullish"

        if daily_change_percent <= -1.5:
            return "Bearish"

        if daily_change_percent < 0:
            return "Slightly Bearish"

        return "Neutral"

    def _get_momentum_status(self, daily_change_percent: float) -> str:
        if daily_change_percent >= 2:
            return "Strong Positive"

        if daily_change_percent > 0:
            return "Positive"

        if daily_change_percent <= -2:
            return "Strong Negative"

        if daily_change_percent < 0:
            return "Negative"

        return "Flat"

    def _get_volume_status(self, volume: int) -> str:
        if volume >= 10_000_000:
            return "Very High"

        if volume >= 5_000_000:
            return "High"

        if volume >= 1_000_000:
            return "Normal"

        return "Low"