
from dataclasses import dataclass


@dataclass
class ScoreResult:
    score: int
    confidence: int
    recommendation: str


class ScoringEngine:

    def calculate(
        self,
        rsi: float,
        ema20: float,
        ema50: float
    ) -> ScoreResult:

        score = 50

        # RSI

        if rsi < 30:
            score += 20

        elif rsi > 70:
            score -= 20

        # Trend

        if ema20 > ema50:
            score += 20
        else:
            score -= 20

        # Clamp score

        score = max(0, min(score, 100))

        # Recommendation

        if score >= 80:
            recommendation = "Strong Buy"

        elif score >= 65:
            recommendation = "Buy"

        elif score >= 45:
            recommendation = "Watch"

        elif score >= 25:
            recommendation = "Sell"

        else:
            recommendation = "Strong Sell"

        confidence = score

        return ScoreResult(
            score=score,
            confidence=confidence,
            recommendation=recommendation,
        )