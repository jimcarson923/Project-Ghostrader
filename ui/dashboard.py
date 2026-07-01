"""
=========================================================
Project Ghostrader

Dashboard

Purpose:
    Main dashboard layout for Ghostrader Desktop.

Version:
    1.3.0
=========================================================
"""

from types import SimpleNamespace

from PySide6.QtWidgets import (
    QGridLayout,
    QWidget,
)

from ui.score_card import ScoreCard
from ui.ai_summary_card import AISummaryCard
from ui.brain_briefing_card import BrainBriefingCard


class Dashboard(QWidget):
    """
    Main Ghostrader dashboard.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()
        self.load_demo_analysis()

    def build_ui(self):
        """
        Build dashboard layout.
        """

        layout = QGridLayout()

        layout.setContentsMargins(20, 20, 20, 20)
        layout.setHorizontalSpacing(20)
        layout.setVerticalSpacing(20)

        self.score_card = ScoreCard()
        self.ai_summary_card = AISummaryCard()
        self.brain_briefing_card = BrainBriefingCard()

        layout.addWidget(self.score_card, 0, 0)
        layout.addWidget(self.ai_summary_card, 0, 1)
        layout.addWidget(self.brain_briefing_card, 1, 0, 1, 2)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
        layout.setRowStretch(0, 1)
        layout.setRowStretch(1, 1)

        self.setLayout(layout)

    def load_demo_analysis(self):
        """
        Load a sample analysis so the dashboard shows real intelligence
        immediately when the app opens.
        """

        analysis = SimpleNamespace(
            symbol="NVDA",
            score={
                "score": 84,
            },
            signal="BUY",
            intelligence={
                "trend": "Bullish",
                "momentum": "Strong",
                "risk": "Medium",
                "confidence": 82,
                "assistant_summary": (
                    "NVDA currently has a Ghost Score of 84 out of 100. "
                    "The current trading signal is BUY. The trend is bullish, "
                    "momentum is strong, and risk is medium. Ghostrader confidence "
                    "is 82%. This setup shows favorable technical strength, but "
                    "risk management is still required."
                ),
                "brain_briefing": (
                    "Ghost Brain classifies NVDA as a Positive Setup. "
                    "The current signal is BUY, with a Ghost Score of 84 out of 100."
                ),
                "next_action": (
                    "Review for possible entry after confirming risk, position size, "
                    "and broader market conditions."
                ),
            },
        )

        self.update_dashboard(analysis)

    def update_dashboard(self, analysis):
        """
        Update dashboard cards from an AnalysisResult.
        """

        self.score_card.update_score(
            analysis.score["score"],
            analysis.signal,
        )

        self.ai_summary_card.update_summary(
            analysis.intelligence.get(
                "assistant_summary",
                "No AI summary available.",
            )
        )

        self.brain_briefing_card.update_briefing(
            analysis.intelligence.get(
                "brain_briefing",
                "No Ghost Brain briefing available.",
            ),
            analysis.intelligence.get(
                "next_action",
                "No next action available.",
            ),
        )