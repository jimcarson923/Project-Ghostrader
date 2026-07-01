"""
=========================================================
Project Ghostrader

AI Summary Card

Purpose:
    Displays Ghost Assistant summary output on the dashboard.

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


class AISummaryCard(QFrame):
    """
    Dashboard card for Ghost Assistant summary.
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

        title = QLabel("🤖 AI SUMMARY")

        title.setFont(QFont("Segoe UI", 14, QFont.Bold))

        title.setStyleSheet("""
            color:#00FF88;
        """)

        layout.addWidget(title)

        self.summary_label = QLabel(
            "Ghost Assistant is online and ready to explain market analysis."
        )

        self.summary_label.setWordWrap(True)

        self.summary_label.setFont(QFont("Segoe UI", 12))

        self.summary_label.setStyleSheet("""
            color:white;
            line-height:140%;
        """)

        layout.addWidget(self.summary_label)

        layout.addStretch()

    def update_summary(self, text: str):
        """
        Update the AI summary text.
        """

        self.summary_label.setText(text)