"""
=========================================================
GHO$TRADER Analysis Pipeline

Purpose:
    Runs the complete stock analysis workflow through a
    dedicated pipeline layer.

Build:
    1.34.0 - Analysis Pipeline Foundation
=========================================================
"""

from dataclasses import dataclass

from services.market_service import MarketService
from engines.technical_indicator_engine import (
    TechnicalIndicatorEngine,
    TechnicalIndicatorResult,
)
from engines.ghost_score_engine import GhostScoreEngine, ScoreResult
from engines.signal_engine import SignalEngine, SignalResult
from engines.intelligence_engine import IntelligenceEngine, IntelligenceReport
from engines.strategy_lab_engine import StrategyLabEngine, StrategyResult
from engines.bullish_pressure_engine import (
    BullishPressureEngine,
    BullishPressureResult,
)


@dataclass
class PipelineAnalysisResult:
    market_snapshot: object
    technical_result: TechnicalIndicatorResult
    score_result: ScoreResult
    signal_result: SignalResult
    intelligence_report: IntelligenceReport
    strategy_result: StrategyResult
    bullish_pressure_result: BullishPressureResult


class AnalysisPipeline:
    """
    Executes the official Ghostrader stock analysis pipeline.
    """

    def __init__(self):
        self.market_service = MarketService()
        self.technical_engine = TechnicalIndicatorEngine()
        self.score_engine = GhostScoreEngine()
        self.signal_engine = SignalEngine()
        self.intelligence_engine = IntelligenceEngine()
        self.strategy_lab_engine = StrategyLabEngine()
        self.bullish_pressure_engine = BullishPressureEngine()

    def analyze_stock(self, symbol: str) -> PipelineAnalysisResult:
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

        strategy_result = self._run_beginner_bullish_strategy(
            clean_symbol,
            market_snapshot,
            technical_result,
            score_result,
            signal_result,
        )

        bullish_pressure_result = self.bullish_pressure_engine.analyze(
            market_snapshot,
            technical_result,
            score_result,
            signal_result,
        )

        return PipelineAnalysisResult(
            market_snapshot=market_snapshot,
            technical_result=technical_result,
            score_result=score_result,
            signal_result=signal_result,
            intelligence_report=intelligence_report,
            strategy_result=strategy_result,
            bullish_pressure_result=bullish_pressure_result,
        )

    def _run_beginner_bullish_strategy(
        self,
        symbol,
        market_snapshot,
        technical_result,
        score_result,
        signal_result,
    ) -> StrategyResult:
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

        return self.strategy_lab_engine.evaluate_strategy(
            strategy_name="Beginner Bullish Strategy",
            symbol=symbol,
            data=strategy_data,
            rules=beginner_bullish_rules,
        )