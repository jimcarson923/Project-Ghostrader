"""
=========================================================
GHO$TRADER Intelligence Engine

Purpose:
    Builds a beginner-friendly intelligence report from
    market, score, and signal results.

Build:
    1.13.0 - Intelligence Report Engine
=========================================================
"""

from dataclasses import dataclass


@dataclass
class IntelligenceReport:
    symbol: str
    title: str
    summary: str
    market_context: str
    score_explanation: str
    signal_explanation: str
    risk_summary: str
    beginner_takeaway: str


class IntelligenceEngine:
    """
    Official intelligence engine for Ghostrader.

    This engine converts raw market, score, and signal outputs
    into a plain-English report for beginner traders.
    """

    def build_report(self, market_snapshot, score_result, signal_result) -> IntelligenceReport:
        symbol = market_snapshot.symbol

        title = f"GHO$TRADER Intelligence Report — {symbol}"

        summary = (
            f"{symbol} currently has a Ghost Score of "
            f"{score_result.ghost_score}/100 with {score_result.confidence}% confidence. "
            f"The active signal is {signal_result.signal}."
        )

        market_context = (
            f"{symbol} is trading at ${market_snapshot.current_price:,.2f}. "
            f"The daily move is ${market_snapshot.daily_change:,.2f}, "
            f"or {market_snapshot.daily_change_percent:.2f}%. "
            f"Current volume is {market_snapshot.volume:,} shares."
        )

        score_explanation = (
            "The Ghost Score is based on the current market snapshot, "
            "including daily price movement and trading volume. "
            "Higher scores indicate stronger market behavior, while lower "
            "scores indicate weaker or riskier conditions."
        )

        signal_explanation = (
            f"The Signal Engine classified this setup as {signal_result.signal} "
            f"with {signal_result.signal_strength.lower()} signal strength. "
            f"The current risk level is {signal_result.risk_level}."
        )

        risk_summary = (
            "This report is not financial advice. Beginner traders should use "
            "Ghostrader as a decision-support tool, not as an automatic trading system. "
            "Always review risk, position size, news, earnings dates, and broader market conditions."
        )

        beginner_takeaway = signal_result.action_message

        return IntelligenceReport(
            symbol=symbol,
            title=title,
            summary=summary,
            market_context=market_context,
            score_explanation=score_explanation,
            signal_explanation=signal_explanation,
            risk_summary=risk_summary,
            beginner_takeaway=beginner_takeaway,
        )