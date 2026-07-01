"""
Ghostrader

Application Controller

Purpose:
    Controls the application workflow.

Version: 0.8.1
"""

from core.ghost_core import GhostCore
from core.constants import DEFAULT_SYMBOL
from utils.console_renderer import ConsoleRenderer


class AppController:
    """
    Controls the application.

    The controller should not perform calculations or
    display results. It coordinates the workflow only.
    """

    def __init__(self):

        self.brain = GhostCore()

    def start(self):

        # --------------------------------------------------
        # Start GhostCore
        # --------------------------------------------------

        self.brain.start()

        # --------------------------------------------------
        # Run Analysis
        # --------------------------------------------------

        analysis = self.brain.run(DEFAULT_SYMBOL)

        # --------------------------------------------------
        # Display Results
        # --------------------------------------------------

        ConsoleRenderer.render(analysis)