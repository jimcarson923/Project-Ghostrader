"""
=========================================================
Project Ghostrader

Main Application Entry Point

Purpose:
    Starts the Ghostrader Desktop application.

Version:
    1.5.1
=========================================================
"""

from frontend.main_window import main as launch_frontend


def main():
    """
    Start Ghostrader Desktop.
    """

    launch_frontend()


if __name__ == "__main__":
    main()