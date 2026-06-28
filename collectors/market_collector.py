"""
Simple market collector entrypoint for testing.
"""

import time
import yfinance as yf


class MarketCollector:
    """Minimal market collector stub."""

    def __init__(self, interval: float = 1.0):
        self.interval = interval
        self.running = False

    def run_once(self):
        """Perform a single collection step."""

        try:
            ticker = yf.Ticker("AAPL")
            price = ticker.fast_info["lastPrice"]

            print(f"AAPL Current Price: ${price:.2f}")

        except Exception as e:
            print(f"Error collecting market data: {e}")

    def run(self, cycles: int = 5):
        """Run the collector for a number of cycles."""

        self.running = True

        for _ in range(cycles):
            if not self.running:
                break

            self.run_once()
            time.sleep(self.interval)

        self.running = False


def main():
    collector = MarketCollector(interval=0.5)

    try:
        collector.run(cycles=3)

    except KeyboardInterrupt:
        print("Stopped")


if __name__ == "__main__":
    main()
