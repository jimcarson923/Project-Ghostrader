import sys
from dataclasses import dataclass
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QTextEdit,
    QFrame,
)
from PyQt6.QtCore import Qt


@dataclass
class DashboardAnalysis:
    symbol: str
    current_price: str
    ghost_score: int
    confidence: int
    recommendation: str
    strengths: list[str]
    warnings: list[str]


class GhostraderMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("GHO$TRADER — Market Intelligence Dashboard")
        self.setMinimumSize(1200, 750)

        self.setStyleSheet("""
            QMainWindow {
                background-color: #050505;
            }

            QLabel {
                color: #EAEAEA;
                font-size: 16px;
            }

            QLineEdit {
                background-color: #111111;
                color: #00FF88;
                border: 1px solid #00FF88;
                padding: 10px;
                font-size: 18px;
            }

            QPushButton {
                background-color: #00FF88;
                color: #000000;
                border: none;
                padding: 12px;
                font-size: 18px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #00CC6A;
            }

            QTextEdit {
                background-color: #111111;
                color: #EAEAEA;
                border: 1px solid #222222;
                font-size: 15px;
                padding: 10px;
            }

            QFrame {
                background-color: #0D0D0D;
                border: 1px solid #1F1F1F;
            }
        """)

        self.setup_ui()

    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()

        sidebar = QFrame()
        sidebar.setFixedWidth(260)
        sidebar_layout = QVBoxLayout()

        logo_label = QLabel("GHO$TRADER")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setStyleSheet("""
            color: #00FF88;
            font-size: 28px;
            font-weight: bold;
            padding: 25px;
        """)

        sidebar_layout.addWidget(logo_label)
        sidebar_layout.addStretch()
        sidebar.setLayout(sidebar_layout)

        dashboard = QWidget()
        dashboard_layout = QVBoxLayout()

        title = QLabel("Live Intelligence Dashboard")
        title.setStyleSheet("""
            color: #00FF88;
            font-size: 30px;
            font-weight: bold;
            padding-bottom: 15px;
        """)

        input_layout = QHBoxLayout()

        self.symbol_input = QLineEdit()
        self.symbol_input.setPlaceholderText("Enter stock symbol, example: AAPL")
        self.symbol_input.returnPressed.connect(self.run_analysis)

        self.analyze_button = QPushButton("Analyze")
        self.analyze_button.clicked.connect(self.run_analysis)

        input_layout.addWidget(self.symbol_input)
        input_layout.addWidget(self.analyze_button)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        self.result_box.setText(
            "Enter a stock symbol and click Analyze.\n\n"
            "Build 1.5.0 adds a working Analyze button workflow:\n"
            "- Symbol validation\n"
            "- Analysis execution\n"
            "- Ghost Score calculation\n"
            "- Recommendation display\n"
            "- Strength and warning output\n"
            "- Status updates"
        )

        self.status_label = QLabel("Status: Ready")
        self.status_label.setStyleSheet("color: #888888; font-size: 14px;")

        dashboard_layout.addWidget(title)
        dashboard_layout.addLayout(input_layout)
        dashboard_layout.addWidget(self.result_box)
        dashboard_layout.addWidget(self.status_label)

        dashboard.setLayout(dashboard_layout)

        main_layout.addWidget(sidebar)
        main_layout.addWidget(dashboard)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def run_analysis(self):
        symbol = self.symbol_input.text().strip().upper()

        if not symbol:
            self.status_label.setText("Status: Please enter a stock symbol.")
            self.result_box.setText("No symbol entered. Example: AAPL, MSFT, NVDA, TSLA")
            return

        if not symbol.isalpha() or len(symbol) > 5:
            self.status_label.setText("Status: Invalid stock symbol.")
            self.result_box.setText("Please enter a valid stock symbol using letters only. Example: AAPL")
            return

        self.status_label.setText(f"Status: Analyzing {symbol}...")
        self.analyze_button.setEnabled(False)

        analysis = self.build_dashboard_analysis(symbol)
        self.display_analysis(analysis)

        self.analyze_button.setEnabled(True)
        self.status_label.setText(f"Status: Analysis complete for {symbol}")

    def build_dashboard_analysis(self, symbol: str) -> DashboardAnalysis:
        base_score = 70 + (sum(ord(char) for char in symbol) % 25)
        confidence = min(base_score - 3, 95)

        if base_score >= 85:
            recommendation = "BUY"
        elif base_score >= 70:
            recommendation = "WATCH"
        else:
            recommendation = "AVOID"

        estimated_price = 100 + (sum(ord(char) for char in symbol) % 250)

        strengths = [
            "Technical structure is currently favorable",
            "Momentum profile is showing positive behavior",
            "Setup quality supports continued monitoring",
        ]

        warnings = [
            "This is not yet connected to live market data",
            "Risk management and position sizing are still required",
        ]

        return DashboardAnalysis(
            symbol=symbol,
            current_price=f"${estimated_price:.2f}",
            ghost_score=base_score,
            confidence=confidence,
            recommendation=recommendation,
            strengths=strengths,
            warnings=warnings,
        )

    def display_analysis(self, analysis: DashboardAnalysis):
        result_text = f"""
GHO$TRADER INTELLIGENCE REPORT

Symbol:
{analysis.symbol}

Current Price:
{analysis.current_price}

Ghost Score:
{analysis.ghost_score} / 100

Confidence:
{analysis.confidence}%

Recommendation:
{analysis.recommendation}

Strengths:
- {analysis.strengths[0]}
- {analysis.strengths[1]}
- {analysis.strengths[2]}

Warnings:
- {analysis.warnings[0]}
- {analysis.warnings[1]}

Analysis Status:
Complete

Build:
Ghostrader Build 1.5.0 — Analyze Button Integration
"""

        self.result_box.setText(result_text.strip())


def main():
    app = QApplication(sys.argv)
    window = GhostraderMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()