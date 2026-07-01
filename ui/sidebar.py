"""
=========================================================
Project Ghostrader

Sidebar

Purpose:
    Main navigation sidebar for the Ghostrader desktop.

Version:
    1.1.0
=========================================================
"""

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class Sidebar(QFrame):
    """
    Ghostrader navigation sidebar.
    """

    def __init__(self):
        super().__init__()

        self.setFixedWidth(240)

        self.setStyleSheet("""
            QFrame{
                background:#151515;
                border-right:1px solid #2A2A2A;
            }
        """)

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        layout.setContentsMargins(15, 20, 15, 20)

        layout.setSpacing(12)

        # ==================================================
        # Logo
        # ==================================================

        logo = QLabel()

        logo_path = (
            Path(__file__).resolve().parent.parent
            / "assets"
            / "images"
            / "ghost_logo.png"
        )

        if logo_path.exists():

            pixmap = QPixmap(str(logo_path))

            logo.setPixmap(
                pixmap.scaled(
                    150,
                    150,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation,
                )
            )

        else:

            logo.setText("GHO$TRADER")

            logo.setAlignment(Qt.AlignCenter)

            logo.setFont(QFont("Segoe UI", 18, QFont.Bold))

            logo.setStyleSheet("color:#00FF88;")

        logo.setAlignment(Qt.AlignCenter)

        layout.addWidget(logo)

        # ==================================================
        # Product Name
        # ==================================================

        title = QLabel("GHO$TRADER")

        title.setAlignment(Qt.AlignCenter)

        title.setFont(QFont("Segoe UI", 18, QFont.Bold))

        title.setStyleSheet("""
            color:#00FF88;
        """)

        layout.addWidget(title)

        subtitle = QLabel("AI MARKET OPERATING SYSTEM")

        subtitle.setAlignment(Qt.AlignCenter)

        subtitle.setStyleSheet("""
            color:#808080;
            font-size:10px;
        """)

        layout.addWidget(subtitle)

        layout.addSpacing(20)

        # ==================================================
        # Navigation Buttons
        # ==================================================

        buttons = [
            "🏠 Dashboard",
            "📈 Watchlist",
            "🔎 Scanner",
            "💼 Portfolio",
            "🤖 AI Chat",
            "📄 Reports",
            "⚙ Settings",
        ]

        button_style = """
            QPushButton{
                background:#202020;
                color:white;
                border:none;
                border-radius:8px;
                padding:14px;
                text-align:left;
                font-size:13px;
            }

            QPushButton:hover{
                background:#2B2B2B;
            }

            QPushButton:pressed{
                background:#00AA66;
            }
        """

        for text in buttons:

            button = QPushButton(text)

            button.setStyleSheet(button_style)

            button.setMinimumHeight(46)

            layout.addWidget(button)

        layout.addStretch()

        # ==================================================
        # Version
        # ==================================================

        version = QLabel("Ghostrader v1.1.0")

        version.setAlignment(Qt.AlignCenter)

        version.setStyleSheet("""
            color:#666666;
            font-size:10px;
        """)

        layout.addWidget(version)