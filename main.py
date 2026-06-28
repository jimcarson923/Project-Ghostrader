"""
Project Ghostrader

Main Application Entry Point

Version: 0.5.0
"""

from controllers.app_controller import AppController


def main():

    controller = AppController()

    controller.start()


if __name__ == "__main__":
    main()