"""
=========================================================
GHO$TRADER Strategy Lab Engine

Purpose:
    Allows Ghostrader to evaluate custom trading strategy
    rules against analysis results.

Build:
    1.30.0 - Strategy Lab Foundation
=========================================================
"""

from dataclasses import dataclass
from typing import Any


@dataclass
class StrategyRule:
    name: str
    field: str
    operator: str
    value: Any


@dataclass
class StrategyResult:
    strategy_name: str
    symbol: str
    passed: bool
    passed_rules: list[str]
    failed_rules: list[str]
    summary: str


class StrategyLabEngine:
    """
    Foundation engine for user-defined strategy testing.

    Future builds will connect this to:
    - RSI
    - Moving averages
    - MACD
    - Bullish Pressure Scanner
    - Institutional Activity Detector
    - Backtesting
    """

    def evaluate_strategy(
        self,
        strategy_name: str,
        symbol: str,
        data: dict,
        rules: list[StrategyRule],
    ) -> StrategyResult:
        passed_rules = []
        failed_rules = []

        for rule in rules:
            actual_value = data.get(rule.field)

            if self._evaluate_rule(actual_value, rule.operator, rule.value):
                passed_rules.append(rule.name)
            else:
                failed_rules.append(rule.name)

        passed = len(failed_rules) == 0

        if passed:
            summary = f"{symbol} passed all rules for strategy '{strategy_name}'."
        else:
            summary = (
                f"{symbol} failed {len(failed_rules)} rule(s) for "
                f"strategy '{strategy_name}'."
            )

        return StrategyResult(
            strategy_name=strategy_name,
            symbol=symbol,
            passed=passed,
            passed_rules=passed_rules,
            failed_rules=failed_rules,
            summary=summary,
        )

    def build_beginner_bullish_strategy(self) -> list[StrategyRule]:
        """
        Default beginner-friendly bullish strategy template.
        """

        return [
            StrategyRule(
                name="Ghost Score above 80",
                field="ghost_score",
                operator=">=",
                value=80,
            ),
            StrategyRule(
                name="Confidence above 70",
                field="confidence",
                operator=">=",
                value=70,
            ),
            StrategyRule(
                name="Signal is BUY",
                field="signal",
                operator="==",
                value="BUY",
            ),
            StrategyRule(
                name="Risk is not Very High",
                field="risk_level",
                operator="!=",
                value="Very High",
            ),
        ]

    def _evaluate_rule(self, actual_value: Any, operator: str, expected_value: Any) -> bool:
        if actual_value is None:
            return False

        if operator == "==":
            return actual_value == expected_value

        if operator == "!=":
            return actual_value != expected_value

        if operator == ">":
            return actual_value > expected_value

        if operator == ">=":
            return actual_value >= expected_value

        if operator == "<":
            return actual_value < expected_value

        if operator == "<=":
            return actual_value <= expected_value

        raise ValueError(f"Unsupported strategy operator: {operator}")