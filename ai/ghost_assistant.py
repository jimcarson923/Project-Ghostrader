"""
=========================================================
Project Ghostrader

Ghost Assistant

Purpose:
    Provides the first permanent AI assistant layer for
    Ghostrader.

Version:
    1.2.0
=========================================================
"""


class GhostAssistant:
    """
    GhostAssistant converts Ghostrader analysis results into
    plain-English answers.

    This is the first foundation for the future Jarvis-style
    Ghostrader AI assistant.
    """

    def __init__(self):
        self.name = "Ghost Assistant"
        self.version = "1.2.0"
        self.status = "ONLINE"

    def get_status(self):
        """
        Return the assistant's current status.
        """

        return {
            "name": self.name,
            "version": self.version,
            "status": self.status,
        }

    def explain_analysis(self, analysis):
        """
        Explain a market analysis in simple language.
        """

        score = analysis.score
        intelligence = analysis.intelligence
        signal = analysis.signal

        symbol = analysis.symbol
        ghost_score = score["score"]
        trend = intelligence["trend"]
        momentum = intelligence["momentum"]
        risk = intelligence["risk"]
        confidence = intelligence["confidence"]
        summary = intelligence["summary"]

        explanation = (
            f"{symbol} currently has a Ghost Score of "
            f"{ghost_score} out of 100. "
            f"The current trading signal is {signal}. "
            f"The trend is {trend.lower()}, momentum is "
            f"{momentum.lower()}, and risk is {risk.lower()}. "
            f"Ghostrader confidence is {confidence}%. "
            f"{summary}"
        )

        return explanation

    def explain_signal(self, analysis):
        """
        Explain the trading signal.
        """

        signal = analysis.signal
        score = analysis.score["score"]
        symbol = analysis.symbol

        if score >= 90:
            reason = "the setup is very strong across the current scoring rules."
        elif score >= 70:
            reason = "the setup is favorable, but still requires risk management."
        elif score >= 40:
            reason = "the setup is mixed and does not show a clear advantage."
        elif score >= 20:
            reason = "the setup is weak and caution is recommended."
        else:
            reason = "the setup is very weak and risk appears elevated."

        return (
            f"{symbol} is currently rated {signal} because "
            f"{reason}"
        )

    def answer_question(self, question, analysis):
        """
        Answer a simple question about the current analysis.
        """

        question = question.lower().strip()

        if "score" in question:
            return (
                f"The Ghost Score for {analysis.symbol} is "
                f"{analysis.score['score']} out of 100."
            )

        if "signal" in question or "buy" in question or "sell" in question:
            return self.explain_signal(analysis)

        if "risk" in question:
            return (
                f"The current risk level for {analysis.symbol} is "
                f"{analysis.intelligence['risk']}."
            )

        if "trend" in question:
            return (
                f"The current trend for {analysis.symbol} is "
                f"{analysis.intelligence['trend']}."
            )

        if "momentum" in question:
            return (
                f"The current momentum for {analysis.symbol} is "
                f"{analysis.intelligence['momentum']}."
            )

        if "summary" in question or "explain" in question:
            return self.explain_analysis(analysis)

        return (
            "I can answer questions about the Ghost Score, signal, "
            "trend, momentum, risk, and summary."
        )