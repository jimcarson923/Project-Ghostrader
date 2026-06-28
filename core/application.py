"""
Ghostrader Application

Creates the application object.

Author: Ghostrader Architecture
Version: 0.5.0
"""

from core.constants import APP_NAME
from core.constants import VERSION


class Application:

    def __init__(self):

        self.name = APP_NAME

        self.version = VERSION

    def startup(self):

        print(f"{self.name} v{self.version}")