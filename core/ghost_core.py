"""
=========================================================
Project Ghostrader

GhostCore

Purpose:
    Central orchestration layer for Ghostrader.

Version:
    1.2.0
=========================================================
"""

from services.market_service import MarketService
from services.technical_service import TechnicalService

from engines.ghost_score_engine import GhostScoreEngine
from engines.intelligence_engine import IntelligenceEngine
from engines.signal_engine import SignalEngine

from ai.ghost_assistant import GhostAssistant
from ai.ghost_brain import GhostBrain

from core.constants import DEFAULT_PERIOD
from core.constants import DEFAULT_INTERVAL

from models.analysis_result import AnalysisResult


class GhostCore:
    """
    GhostCore is the central AI brain for Ghostrader.

    It coordinates:
    - Market data
    - Technical indicators
    - Ghost Score
    - Market intelligence
    - Trading signal
    - Ghost Assistant explanation layer
    - Ghost Brain interpretation layer
    """

    def __init__(self):

        self.version = "1.2.0"
        self.status = "ONLINE"

        self.market_service = MarketService()
        self.assistant = GhostAssistant()
        self.brain = GhostBrain()

    def start(self):
        """
        Start GhostCore.
        """

        print()
        print("=" * 65)
        print("                 GHOSTRADER AI BRAIN")
        print("=" * 65)
        print(f"Status        : {self.status}")
        print(f"Version       : {self.version}")
        print(f"Assistant     : {self.assistant.status}")
        print(f"Ghost Brain   : {self.brain.status}")
        print("=" * 65)

    def run(self, symbol):
        """
        Run a complete Ghostrader analysis.
        """

        print(f"\nDownloading historical data for {symbol}...")

        historical_data = self.market_service.get_historical_data(
            symbol,
            DEFAULT_PERIOD,
            DEFAULT_INTERVAL,
        )

        print("Calculating technical indicators...")

        historical_data = TechnicalService.add_indicators(historical_data)

        print("Calculating Ghost Score...")

        score = GhostScoreEngine.calculate(historical_data)

        print("Generating market intelligence...")

        intelligence = IntelligenceEngine.analyze(score)

        print("Generating trading signal...")

        signal = SignalEngine.calculate(score["score"])

        analysis = AnalysisResult(
            symbol=symbol,
            score=score,
            intelligence=intelligence,
            signal=signal,
        )

        print("Generating AI assistant explanation...")

        assistant_summary = self.assistant.explain_analysis(analysis)

        analysis.intelligence["assistant_summary"] = assistant_summary

        print("Generating Ghost Brain interpretation...")

        brain_briefing = self.brain.create_briefing(analysis)
        next_action = self.brain.recommend_next_action(analysis)

        analysis.intelligence["brain_briefing"] = brain_briefing
        analysis.intelligence["next_action"] = next_action

        return analysis

    def ask(self, question, analysis):
        """
        Ask Ghost Assistant a question about the current analysis.
        """

        return self.assistant.answer_question(question, analysis)