import sys
from dataclasses import dataclass

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QLabel,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from services.market_service import MarketService


@dataclass
class DashboardAnalysis:
    symbol: str
    current_price: float
    daily_change: float
    daily_change_percent: float
    volume: int
    ghost_score: int
    confidence: int
    recommendation: str
    strengths: list[str]
    warnings: list[str]


class GhostraderMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.market_service = MarketService()

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
            "Build 1.7.0 connects the dashboard to the Market Service:\n"
            "- Symbol validation\n"
            "- Market snapshot retrieval\n"
            "- Price display\n"
            "- Daily change display\n"
            "- Volume display\n"
            "- Ghost Score calculation\n"
            "- Recommendation output"
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

        self.status_label.setText(f"Status: Pulling market snapshot for {symbol}...")
        self.analyze_button.setEnabled(False)

        try:
            analysis = self.build_dashboard_analysis(symbol)
            self.display_analysis(analysis)
            self.status_label.setText(f"Status: Analysis complete for {symbol}")
        except Exception as error:
            self.result_box.setText(f"Ghostrader could not complete the analysis.\n\nError:\n{error}")
            self.status_label.setText("Status: Analysis failed.")
        finally:
            self.analyze_button.setEnabled(True)

    def build_dashboard_analysis(self, symbol: str) -> DashboardAnalysis:
        snapshot = self.market_service.get_market_snapshot(symbol)

        ghost_score = self.calculate_ghost_score(snapshot.daily_change_percent, snapshot.volume)
        confidence = min(ghost_score - 2, 95)

        if ghost_score >= 85:
            recommendation = "BUY"
        elif ghost_score >= 70:
            recommendation = "WATCH"
        else:
            recommendation = "AVOID"

        strengths = [
            "Market snapshot successfully loaded",
            "Price and volume data are available to the dashboard",
            "Analyze button is now connected to the service layer",
        ]

        warnings = [
            "Market Service is still using simulated data",
            "Live market data connection is scheduled for a future build",
        ]

        return DashboardAnalysis(
            symbol=snapshot.symbol,
            current_price=snapshot.current_price,
            daily_change=snapshot.daily_change,
            daily_change_percent=snapshot.daily_change_percent,
            volume=snapshot.volume,
            ghost_score=ghost_score,
            confidence=confidence,
            recommendation=recommendation,
            strengths=strengths,
            warnings=warnings,
        )

    def calculate_ghost_score(self, daily_change_percent: float, volume: int) -> int:
        score = 70

        if daily_change_percent > 1:
            score += 10
        elif daily_change_percent > 0:
            score += 5
        elif daily_change_percent < -1:
            score -= 10
        elif daily_change_percent < 0:
            score -= 5

        if volume >= 3_000_000:
            score += 8
        elif volume >= 1_500_000:
            score += 4

        return max(0, min(score, 100))

    def display_analysis(self, analysis: DashboardAnalysis):
        result_text = f"""
GHO$TRADER INTELLIGENCE REPORT

Symbol:
{analysis.symbol}

Market Snapshot:
Current Price: ${analysis.current_price:,.2f}
Daily Change: ${analysis.daily_change:,.2f}
Daily Change Percent: {analysis.daily_change_percent:.2f}%
Volume: {analysis.volume:,}

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
Ghostrader Build 1.7.0 — Connect Analyze Button to Market Service
"""

        self.result_box.setText(result_text.strip())


def main():
    app = QApplication(sys.argv)
    window = GhostraderMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()