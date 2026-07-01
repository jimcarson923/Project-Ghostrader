"""
=========================================================
Project Ghostrader

Ghost Brain

Purpose:
    Provides the central AI decision layer for Ghostrader.

Version:
    1.2.0
=========================================================
"""


class GhostBrain:
    """
    GhostBrain is the beginning of Ghostrader's higher-level
    AI reasoning layer.

    It does not replace GhostCore.

    GhostCore runs the platform workflow.
    GhostBrain interprets the meaning of the analysis.
    """

    def __init__(self):
        self.name = "Ghost Brain"
        self.version = "1.2.0"
        self.status = "ONLINE"

    def get_status(self):
        """
        Return the current Ghost Brain status.
        """

        return {
            "name": self.name,
            "version": self.version,
            "status": self.status,
        }

    def classify_market_condition(self, analysis):
        """
        Classify the current market condition for a stock.
        """

        score = analysis.score["score"]
        risk = analysis.intelligence["risk"]
        trend = analysis.intelligence["trend"]
        momentum = analysis.intelligence["momentum"]

        if score >= 80 and risk.lower() == "low":
            return "Strong Opportunity"

        if score >= 60 and trend.lower() == "bullish":
            return "Positive Setup"

        if score >= 40:
            return "Mixed Setup"

        if risk.lower() == "high":
            return "High Risk Setup"

        if trend.lower() == "bearish" or momentum.lower() == "weak":
            return "Weak Setup"

        return "Unclear Setup"

    def create_briefing(self, analysis):
        """
        Create a short AI briefing for the user.
        """

        market_condition = self.classify_market_condition(analysis)

        briefing = (
            f"Ghost Brain classifies {analysis.symbol} as a "
            f"{market_condition}. "
            f"The current signal is {analysis.signal}, with a Ghost Score "
            f"of {analysis.score['score']} out of 100."
        )

        return briefing

    def recommend_next_action(self, analysis):
        """
        Recommend the next action in plain English.
        """

        score = analysis.score["score"]
        risk = analysis.intelligence["risk"]

        if score >= 80:
            return "Review for possible entry after confirming risk and position size."

        if score >= 60:
            return "Monitor closely and wait for stronger confirmation."

        if score >= 40:
            return "Hold off until the setup becomes clearer."

        if risk.lower() == "high":
            return "Avoid for now. Risk is elevated."

        return "Do not act yet. More confirmation is needed."