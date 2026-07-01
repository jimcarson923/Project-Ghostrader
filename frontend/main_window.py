import sys

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

from core.ghost_core import GhostCore


class GhostraderMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ghost_core = GhostCore()

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

            QPushButton:disabled {
                background-color: #333333;
                color: #777777;
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
            "Build 1.18.0 displays technical indicator output:\n"
            "- Trend direction\n"
            "- Momentum status\n"
            "- Volume status\n"
            "- Technical summary\n"
            "- Ghost Core integration"
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

        self.status_label.setText(f"Status: Ghost Core analyzing {symbol}...")
        self.analyze_button.setEnabled(False)

        try:
            result = self.ghost_core.analyze(symbol)
            self.display_analysis(result)
            self.status_label.setText(f"Status: Analysis complete for {symbol}")
        except Exception as error:
            self.result_box.setText(
                "Ghostrader could not complete the analysis.\n\n"
                f"Error:\n{error}"
            )
            self.status_label.setText("Status: Analysis failed.")
        finally:
            self.analyze_button.setEnabled(True)

    def display_analysis(self, result):
        market = result.market_snapshot
        technical = result.technical_result
        score = result.score_result
        signal = result.signal_result
        report = result.intelligence_report

        strengths_text = "\n".join(f"- {item}" for item in score.strengths)
        warnings_text = "\n".join(f"- {item}" for item in score.warnings)

        result_text = f"""
{report.title}

Summary:
{report.summary}

Market Snapshot:
Current Price: ${market.current_price:,.2f}
Daily Change: ${market.daily_change:,.2f}
Daily Change Percent: {market.daily_change_percent:.2f}%
Volume: {market.volume:,}

Technical Indicators:
Trend Direction: {technical.trend_direction}
Momentum Status: {technical.momentum_status}
Volume Status: {technical.volume_status}

Technical Summary:
{technical.technical_summary}

Ghost Score:
{score.ghost_score} / 100

Confidence:
{score.confidence}%

Recommendation:
{score.recommendation}

Signal:
{signal.signal}

Signal Strength:
{signal.signal_strength}

Risk Level:
{signal.risk_level}

Market Context:
{report.market_context}

Score Explanation:
{report.score_explanation}

Signal Explanation:
{report.signal_explanation}

Beginner Takeaway:
{report.beginner_takeaway}

Risk Summary:
{report.risk_summary}

Strengths:
{strengths_text}

Warnings:
{warnings_text}

Analysis Status:
Complete

Build:
Ghostrader Build 1.18.0 — Display Technical Indicators on Dashboard
"""

        self.result_box.setText(result_text.strip())


def main():
    app = QApplication(sys.argv)
    window = GhostraderMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()