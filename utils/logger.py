"""
Ghostrader Logger

Simple centralized console logger.

Author: Ghostrader Architecture
Version: 0.5.0
"""

from datetime import datetime


class Logger:

    @staticmethod
    def info(message: str):

        timestamp = datetime.now().strftime("%H:%M:%S")

        print(f"[INFO {timestamp}] {message}")

    @staticmethod
    def warning(message: str):

        timestamp = datetime.now().strftime("%H:%M:%S")

        print(f"[WARNING {timestamp}] {message}")

    @staticmethod
    def error(message: str):

        timestamp = datetime.now().strftime("%H:%M:%S")

        print(f"[ERROR {timestamp}] {message}")