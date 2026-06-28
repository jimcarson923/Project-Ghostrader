"""
Ghostrader Application Controller

Coordinates the application's workflow.

Author: Ghostrader Architecture
Version: 0.5.0
"""

from core.application import Application
from services.market_service import MarketService
from services.technical_service import TechnicalService
from engines.ghost_score_engine import GhostScoreEngine
from core.constants import (
    DEFAULT_SYMBOL,
    DEFAULT_PERIOD,
    DEFAULT_INTERVAL,
    LINE,
)


class AppController:

    def __init__(self):

        self.application = Application()

        self.market_service = MarketService()

    def start(self):

        self.application.startup()

        print(LINE)
        print("      GHOSTRADER MARKET INTELLIGENCE")
        print(LINE)

        symbol = DEFAULT_SYMBOL

        print(f"\nDownloading historical data for {symbol}...")

        historical_data = self.market_service.get_historical_data(
            symbol,
            DEFAULT_PERIOD,
            DEFAULT_INTERVAL,
        )

        print("Calculating technical indicators...")

        historical_data = TechnicalService.add_indicators(historical_data)

        print("Calculating Ghost Score...")

        result = GhostScoreEngine.calculate(historical_data)

        print("\n" + LINE)
        print("          GHOSTRADER ANALYSIS")
        print(LINE)

        print(f"\nSymbol            : {symbol}")
        print(f"Current Price     : ${result['close']:.2f}")
        print(f"SMA20             : ${result['sma20']:.2f}")
        print(f"SMA50             : ${result['sma50']:.2f}")
        print(f"RSI               : {result['rsi']:.2f}")

        print("\n" + "-" * 65)

        print(f"Ghost Score       : {result['score']} / 100")
        print(f"Recommendation    : {result['recommendation']}")

        print("\nReasons:")

        for reason in result["reasons"]:
            print(f"  ✓ {reason}")

        print("\n" + LINE)
        print("Analysis Complete.")
        print(LINE)