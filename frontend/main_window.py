import sys
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

        analyze_button = QPushButton("Analyze")
        analyze_button.clicked.connect(self.run_analysis)

        input_layout.addWidget(self.symbol_input)
        input_layout.addWidget(analyze_button)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        self.result_box.setText(
            "Enter a stock symbol and click Analyze.\n\n"
            "Ghostrader will display:\n"
            "- Current Price\n"
            "- Ghost Score\n"
            "- Confidence\n"
            "- Recommendation\n"
            "- Strengths\n"
            "- Warnings"
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
            return

        self.status_label.setText(f"Status: Analyzing {symbol}...")

        # Temporary analysis output for Build 1.4.0.
        # In the next build, this will connect directly to the Ghostrader engines.
        current_price = "$214.38"
        ghost_score = "87 / 100"
        confidence = "82%"
        recommendation = "BUY"

        strengths = [
            "Strong recent price momentum",
            "Positive trend structure",
            "Healthy trading activity",
        ]

        warnings = [
            "Market volatility remains elevated",
            "Resistance may be nearby",
        ]

        result_text = f"""
GHO$TRADER INTELLIGENCE REPORT

Symbol:
{symbol}

Current Price:
{current_price}

Ghost Score:
{ghost_score}

Confidence:
{confidence}

Recommendation:
{recommendation}

Strengths:
- {strengths[0]}
- {strengths[1]}
- {strengths[2]}

Warnings:
- {warnings[0]}
- {warnings[1]}

Analysis Status:
Complete
"""

        self.result_box.setText(result_text.strip())
        self.status_label.setText(f"Status: Analysis complete for {symbol}")


def main():
    app = QApplication(sys.argv)
    window = GhostraderMainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()