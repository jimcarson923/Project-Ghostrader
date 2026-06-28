"""
Project Ghostrader
Main Application Entry Point

Workflow

1. Download historical market data
2. Calculate technical indicators
3. Calculate Ghost Score
4. Display market analysis
"""

from services.market_service import MarketService
from services.technical_service import TechnicalService
from engines.ghost_score_engine import GhostScoreEngine


def main():

    print("=" * 65)
    print("              GHOSTRADER MARKET INTELLIGENCE")
    print("=" * 65)

    symbol = "AAPL"

    market_service = MarketService()

    print(f"\nDownloading historical market data for {symbol}...")

    historical_data = market_service.get_historical_data(symbol)

    print("Calculating technical indicators...")

    historical_data = TechnicalService.add_indicators(historical_data)

    print("Calculating Ghost Score...")

    result = GhostScoreEngine.calculate(historical_data)

    print("\n" + "=" * 65)
    print("                 GHOSTRADER ANALYSIS")
    print("=" * 65)

    print(f"\nSymbol          : {symbol}")
    print(f"Current Price   : ${result['close']:.2f}")
    print(f"SMA20           : ${result['sma20']:.2f}")
    print(f"SMA50           : ${result['sma50']:.2f}")
    print(f"RSI             : {result['rsi']:.2f}")

    print("\n" + "-" * 65)

    print(f"Ghost Score     : {result['score']} / 100")
    print(f"Recommendation  : {result['recommendation']}")

    print("\nReasons:")

    for reason in result["reasons"]:
        print(f"  ✓ {reason}")

    print("\n" + "=" * 65)
    print("Analysis Complete.")
    print("=" * 65)


if __name__ == "__main__":
    main()
    