"""
=========================================================
GHO$TRADER Ghost Score Engine

Purpose:
    Calculates the official Ghost Score from market snapshot
    data supplied by the Market Service.

Build:
    1.9.0 - Real Ghost Score Engine Integration
=========================================================
"""

from dataclasses import dataclass


@dataclass
class ScoreResult:
    symbol: str
    ghost_score: int
    confidence: int
    recommendation: str
    strengths: list[str]
    warnings: list[str]


class GhostScoreEngine:
    """
    Converts market snapshot data into a Ghost Score.

    This engine is now the official scoring source.
    The UI should display scoring results, not calculate them.
    """

    def calculate(self, market_snapshot) -> ScoreResult:
        score = 70
        strengths = []
        warnings = []

        symbol = market_snapshot.symbol
        daily_change_percent = market_snapshot.daily_change_percent
        volume = market_snapshot.volume

        if daily_change_percent >= 2:
            score += 12
            strengths.append("Strong positive daily price movement")
        elif daily_change_percent >= 1:
            score += 8
            strengths.append("Positive daily price movement")
        elif daily_change_percent > 0:
            score += 4
            strengths.append("Slight positive price movement")
        elif daily_change_percent <= -2:
            score -= 12
            warnings.append("Strong negative daily price movement")
        elif daily_change_percent <= -1:
            score -= 8
            warnings.append("Negative daily price movement")
        elif daily_change_percent < 0:
            score -= 4
            warnings.append("Slight negative price movement")
        else:
            warnings.append("Price is currently flat")

        if volume >= 10_000_000:
            score += 10
            strengths.append("Very strong trading volume")
        elif volume >= 5_000_000:
            score += 7
            strengths.append("Strong trading volume")
        elif volume >= 1_000_000:
            score += 4
            strengths.append("Healthy trading volume")
        else:
            score -= 5
            warnings.append("Low trading volume")

        ghost_score = max(0, min(score, 100))
        confidence = self._calculate_confidence(ghost_score, volume)

        recommendation = self._get_recommendation(ghost_score)

        if not strengths:
            strengths.append("Market snapshot loaded successfully")

        if not warnings:
            warnings.append("No major market snapshot warnings detected")

        return ScoreResult(
            symbol=symbol,
            ghost_score=ghost_score,
            confidence=confidence,
            recommendation=recommendation,
            strengths=strengths,
            warnings=warnings,
        )

    def _calculate_confidence(self, ghost_score: int, volume: int) -> int:
        confidence = 65

        if ghost_score >= 85:
            confidence += 15
        elif ghost_score >= 70:
            confidence += 10
        elif ghost_score < 50:
            confidence -= 10

        if volume >= 5_000_000:
            confidence += 10
        elif volume >= 1_000_000:
            confidence += 5
        else:
            confidence -= 5

        return max(0, min(confidence, 95))

    def _get_recommendation(self, ghost_score: int) -> str:
        if ghost_score >= 85:
            return "BUY"

        if ghost_score >= 70:
            return "WATCH"

        return "AVOID"