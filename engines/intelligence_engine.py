from dataclasses import dataclass
from typing import List

from engines.scoring_engine import ScoreResult


@dataclass
class IntelligenceReport:
    symbol: str
    current_price: float
    ghost_score: int
    confidence: int
    recommendation: str

    strengths: List[str]
    warnings: List[str]


class IntelligenceEngine:

    def build_report(
        self,
        symbol: str,
        current_price: float,
        score: ScoreResult,
        strengths: List[str],
        warnings: List[str],
    ) -> IntelligenceReport:

        return IntelligenceReport(
            symbol=symbol,
            current_price=current_price,
            ghost_score=score.score,
            confidence=score.confidence,
            recommendation=score.recommendation,
            strengths=strengths,
            warnings=warnings,
        )

    def print_report(self, report: IntelligenceReport):

        print("\n")
        print("=" * 60)
        print("           GHOSTRADER INTELLIGENCE REPORT")
        print("=" * 60)

        print(f"Symbol           : {report.symbol}")
        print(f"Current Price    : ${report.current_price:.2f}")

        print("-" * 60)

        print(f"Ghost Score      : {report.ghost_score}/100")
        print(f"Confidence       : {report.confidence}%")
        print(f"Recommendation   : {report.recommendation}")

        print("\nStrengths")

        if report.strengths:
            for item in report.strengths:
                print(f"  ✓ {item}")
        else:
            print("  None")

        print("\nWarnings")

        if report.warnings:
            for item in report.warnings:
                print(f"  • {item}")
        else:
            print("  None")

        print("=" * 60)
