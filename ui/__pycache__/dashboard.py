"""
Project Ghostrader
Dashboard

Permanent dashboard widget for Ghostrader Desktop.
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QLabel,
    QVBoxLayout,
    QWidget,
)


CARD_STYLE = """
QFrame {
    background-color: #151515;
    border: 1px solid #2E2E2E;
    border-radius: 10px;
}
"""


class Dashboard(QWidget):
    """
    Main Ghostrader dashboard.
    """

    def __init__(self):
        super().__init__()

        self.build_ui()

    def create_card(self, title: str) -> QFrame:
        card = QFrame()
        card.setStyleSheet(CARD_STYLE)

        layout = QVBoxLayout(card)

        heading = QLabel(title)
        heading.setFont(QFont("Segoe UI", 14, QFont.Bold))
        heading.setStyleSheet("color:#00FF88;")

        body = QLabel("Waiting for GhostCore...")
        body.setAlignment(Qt.AlignCenter)
        body.setStyleSheet("color:white;font-size:16px;")

        layout.addWidget(heading)
        layout.addStretch()
        layout.addWidget(body)
        layout.addStretch()

        return card

    def build_ui(self):

        layout = QGridLayout(self)
        layout.setSpacing(20)

        layout.addWidget(self.create_card("GHOST SCORE"), 0, 0)
        layout.addWidget(self.create_card("SIGNAL"), 0, 1)
        layout.addWidget(self.create_card("MARKET INTELLIGENCE"), 1, 0)
        layout.addWidget(self.create_card("AI SUMMARY"), 1, 1)

        layout.setColumnStretch(0, 1)
        layout.setColumnStretch(1, 1)
