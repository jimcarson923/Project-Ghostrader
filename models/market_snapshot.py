from dataclasses import dataclass
from datetime import datetime


@dataclass
class MarketSnapshot:
    symbol: str
    company: str
    price: float
    change: float
    change_pct: float
    volume: int
    market_cap: int
    timestamp: datetime
