"""
=========================================================
Project Ghostrader

Ghost Brain Briefing Card

Purpose:
    Displays Ghost Brain interpretation and next action.

Version:
    1.2.0
=========================================================
"""

from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class BrainBriefingCard(QFrame):
    """
    Dashboard card for Ghost Brain briefing and next action.
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

        layout.setContentsMargins(20, 20, 20, 20)

        title = QLabel("🧠 GHOST BRAIN")

        title.setFont(QFont("Segoe UI", 14, QFont.Bold))

        title.setStyleSheet("""
            color:#00FF88;
        """)

        layout.addWidget(title)

        self.briefing_label = QLabel(
            "Ghost Brain is online and ready to interpret analysis."
        )

        self.briefing_label.setWordWrap(True)

        self.briefing_label.setFont(QFont("Segoe UI", 12))

        self.briefing_label.setStyleSheet("""
            color:white;
        """)

        layout.addWidget(self.briefing_label)

        self.next_action_label = QLabel(
            "Next Action: Waiting for analysis."
        )

        self.next_action_label.setWordWrap(True)

        self.next_action_label.setFont(QFont("Segoe UI", 12, QFont.Bold))

        self.next_action_label.setStyleSheet("""
            color:#00FF88;
            padding-top:12px;
        """)

        layout.addWidget(self.next_action_label)

        layout.addStretch()

    def update_briefing(self, briefing: str, next_action: str):
        """
        Update the Ghost Brain briefing and next action.
        """

        self.briefing_label.setText(briefing)

        self.next_action_label.setText(f"Next Action: {next_action}")