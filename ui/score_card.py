"""
=========================================================
Project Ghostrader

Ghost Score Card

Purpose:
    Displays the current Ghost Score and trading signal.

Version:
    1.1.0
=========================================================
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class ScoreCard(QFrame):
    """
    Ghost Score dashboard card.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        self.setMinimumHeight(250)

        self.setStyleSheet("""
            QFrame{
                background:#151515;
                border:1px solid #2A2A2A;
                border-radius:12px;
            }
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(20,20,20,20)

        # ==================================================
        # Title
        # ==================================================

        title = QLabel("👻 GHOST SCORE")

        title.setFont(QFont("Segoe UI", 14, QFont.Bold))

        title.setStyleSheet("""
            color:#00FF88;
        """)

        layout.addWidget(title)

        layout.addStretch()

        # ==================================================
        # Score
        # ==================================================

        self.score_label = QLabel("20 / 100")

        self.score_label.setAlignment(Qt.AlignCenter)

        self.score_label.setFont(QFont("Segoe UI", 34, QFont.Bold))

        self.score_label.setStyleSheet("""
            color:white;
        """)

        layout.addWidget(self.score_label)

        # ==================================================
        # Signal
        # ==================================================

        self.signal_label = QLabel("🔴 SELL")

        self.signal_label.setAlignment(Qt.AlignCenter)

        self.signal_label.setFont(QFont("Segoe UI", 16, QFont.Bold))

        self.signal_label.setStyleSheet("""
            color:#FF5555;
        """)

        layout.addWidget(self.signal_label)

        layout.addStretch()

    # ======================================================
    # Public Method
    # ======================================================

    def update_score(self, score: int, signal: str):
        """
        Update the Ghost Score card.
        """

        self.score_label.setText(f"{score} / 100")

        self.signal_label.setText(signal)