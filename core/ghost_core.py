"""
=========================================================
GHO$TRADER Ghost Core

Purpose:
    Central orchestration layer for Ghostrader analysis.

Build:
    1.31.0 - Strategy Lab Integration
=========================================================
"""

from dataclasses import dataclass

from services.market_service import MarketService
from engines.ghost_score_engine import GhostScoreEngine, ScoreResult
from engines.signal_engine import SignalEngine, SignalResult
from engines.intelligence_engine import IntelligenceEngine, IntelligenceReport
from engines.technical_indicator_engine import (
    TechnicalIndicatorEngine,
    TechnicalIndicatorResult,
)
from engines.strategy_lab_engine import StrategyLabEngine, StrategyResult


@dataclass
class GhostAnalysisResult:
    market_snapshot: object
    technical_result: TechnicalIndicatorResult
    score_result: ScoreResult
    signal_result: SignalResult
    intelligence_report: IntelligenceReport
    strategy_result: StrategyResult


class GhostCore:
    """
    Coordinates the complete Ghostrader analysis workflow.
    """

    def __init__(self):
        self.market_service = MarketService()
        self.technical_engine = TechnicalIndicatorEngine()
        self.score_engine = GhostScoreEngine()
        self.signal_engine = SignalEngine()
        self.intelligence_engine = IntelligenceEngine()
        self.strategy_lab_engine = StrategyLabEngine()

    def analyze(self, symbol: str) -> GhostAnalysisResult:
        clean_symbol = symbol.strip().upper()

        if not clean_symbol:
            raise ValueError("Stock symbol cannot be empty.")

        market_snapshot = self.market_service.get_market_snapshot(clean_symbol)

        technical_result = self.technical_engine.analyze(market_snapshot)

        score_result = self.score_engine.calculate(market_snapshot)

        signal_result = self.signal_engine.generate_signal(score_result)

        intelligence_report = self.intelligence_engine.build_report(
            market_snapshot,
            score_result,
            signal_result,
        )

        strategy_data = {
            "ghost_score": score_result.ghost_score,
            "confidence": score_result.confidence,
            "recommendation": score_result.recommendation,
            "signal": signal_result.signal,
            "signal_strength": signal_result.signal_strength,
            "risk_level": signal_result.risk_level,
            "daily_change_percent": market_snapshot.daily_change_percent,
            "volume": market_snapshot.volume,
            "trend_direction": technical_result.trend_direction,
            "momentum_status": technical_result.momentum_status,
            "volume_status": technical_result.volume_status,
        }

        beginner_bullish_rules = (
            self.strategy_lab_engine.build_beginner_bullish_strategy()
        )

        strategy_result = self.strategy_lab_engine.evaluate_strategy(
            strategy_name="Beginner Bullish Strategy",
            symbol=clean_symbol,
            data=strategy_data,
            rules=beginner_bullish_rules,
        )

        return GhostAnalysisResult(
            market_snapshot=market_snapshot,
            technical_result=technical_result,
            score_result=score_result,
            signal_result=signal_result,
            intelligence_report=intelligence_report,
            strategy_result=strategy_result,
        )