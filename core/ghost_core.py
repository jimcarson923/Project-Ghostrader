"""
=========================================================
GHO$TRADER Ghost Core

Purpose:
    Central orchestration layer for Ghostrader analysis.

Build:
    1.14.0 - Ghost Core Orchestrator
=========================================================
"""

from dataclasses import dataclass

from services.market_service import MarketService
from engines.ghost_score_engine import GhostScoreEngine, ScoreResult
from engines.signal_engine import SignalEngine, SignalResult
from engines.intelligence_engine import IntelligenceEngine, IntelligenceReport


@dataclass
class GhostAnalysisResult:
    market_snapshot: object
    score_result: ScoreResult
    signal_result: SignalResult
    intelligence_report: IntelligenceReport


class GhostCore:
    """
    Coordinates the complete Ghostrader analysis workflow.
    """

    def __init__(self):
        self.market_service = MarketService()
        self.score_engine = GhostScoreEngine()
        self.signal_engine = SignalEngine()
        self.intelligence_engine = IntelligenceEngine()

    def analyze(self, symbol: str) -> GhostAnalysisResult:
        clean_symbol = symbol.strip().upper()

        if not clean_symbol:
            raise ValueError("Stock symbol cannot be empty.")

        market_snapshot = self.market_service.get_market_snapshot(clean_symbol)
        score_result = self.score_engine.calculate(market_snapshot)
        signal_result = self.signal_engine.generate_signal(score_result)
        intelligence_report = self.intelligence_engine.build_report(
            market_snapshot,
            score_result,
            signal_result,
        )

        return GhostAnalysisResult(
            market_snapshot=market_snapshot,
            score_result=score_result,
            signal_result=signal_result,
            intelligence_report=intelligence_report,
        )