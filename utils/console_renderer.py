"""
Ghostrader Console Renderer

Purpose:
    Display the Ghostrader analysis in a clean,
    professional console layout.

Version:
    1.0.0
"""

from datetime import datetime

from utils.colors import Colors


class ConsoleRenderer:

    WIDTH = 70
    BOXES = 20

    @staticmethod
    def divider():
        print(Colors.INFO + ("═" * ConsoleRenderer.WIDTH) + Colors.RESET)

    @staticmethod
    def center(text):
        return text.center(ConsoleRenderer.WIDTH)

    @staticmethod
    def build_score_scale(score):

        boxes = []
        pointer = []

        pointer_position = min(
            int((score / 100) * (ConsoleRenderer.BOXES - 1)),
            ConsoleRenderer.BOXES - 1,
        )

        for i in range(ConsoleRenderer.BOXES):

            percent = ((i + 1) / ConsoleRenderer.BOXES) * 100

            if percent <= 40:
                color = Colors.DANGER
            elif percent <= 70:
                color = Colors.WARNING
            else:
                color = Colors.SUCCESS

            boxes.append(color + "■" + Colors.RESET)

            if i == pointer_position:
                pointer.append("▲")
            else:
                pointer.append(" ")

        return " ".join(boxes), " ".join(pointer)

    @staticmethod
    def render(analysis):

        score = analysis.score
        intelligence = analysis.intelligence

        now = datetime.now().strftime("%I:%M:%S %p")

        ConsoleRenderer.divider()

        print(
            Colors.SUCCESS
            + ConsoleRenderer.center("GHOSTRADER")
            + Colors.RESET
        )

        print(
            Colors.INFO
            + ConsoleRenderer.center("AI MARKET OPERATING SYSTEM")
            + Colors.RESET
        )

        print(ConsoleRenderer.center("Version 1.0.0"))

        ConsoleRenderer.divider()

        print(f" AI STATUS : {Colors.SUCCESS}ONLINE{Colors.RESET}")
        print(f" TIME      : {now}")
        print(f" SYMBOL    : {analysis.symbol}")
        print(f" PRICE     : ${score['close']:.2f}")

        ConsoleRenderer.divider()

        print(
            Colors.INFO
            + "GHOST SCORE"
            + Colors.RESET
        )

        print()

        scale, pointer = ConsoleRenderer.build_score_scale(
            score["score"]
        )

        print(" 0%" + (" " * 54) + "100%")
        print(" " + scale)
        print(" " + pointer)

        print()

        print(f" Current Score : {score['score']} / 100")
        print(f" Signal        : {analysis.signal}")

        ConsoleRenderer.divider()

        print(
            Colors.INFO
            + "MARKET INTELLIGENCE"
            + Colors.RESET
        )

        print()

        print(f" Trend       : {intelligence['trend']}")
        print(f" Momentum    : {intelligence['momentum']}")
        print(f" Risk        : {intelligence['risk']}")
        print(f" Confidence  : {intelligence['confidence']}%")

        ConsoleRenderer.divider()

        print(
            Colors.INFO
            + "AI SUMMARY"
            + Colors.RESET
        )

        print()

        print(" " + intelligence["summary"])

        ConsoleRenderer.divider()

        print(
            Colors.INFO
            + "REASONS"
            + Colors.RESET
        )

        print()

        for reason in score["reasons"]:
            print(f" • {reason}")

        ConsoleRenderer.divider()

        print(
            Colors.SUCCESS
            + ConsoleRenderer.center("Analysis Complete")
            + Colors.RESET
        )

        ConsoleRenderer.divider()