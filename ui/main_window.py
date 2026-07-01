"""
=========================================================
Project Ghostrader

Main Desktop Window

Purpose:
    Main application window for Ghostrader Desktop.

Version:
    1.2.1
=========================================================
"""

from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

from ui.sidebar import Sidebar
from ui.dashboard import Dashboard


class MainWindow(QMainWindow):
    """
    Main Ghostrader desktop window.
    """

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ghostrader AI Market Operating System")
        self.resize(1500, 900)

        self.build_ui()

    def build_ui(self):
        """
        Build the main application layout.
        """

        root = QWidget()
        root_layout = QHBoxLayout(root)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        self.sidebar = Sidebar()
        root_layout.addWidget(self.sidebar)

        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(30, 25, 30, 25)
        content_layout.setSpacing(20)

        title = QLabel("Ghostrader Dashboard")
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        title.setStyleSheet("color:#00FF88;")
        title.setAlignment(Qt.AlignLeft)

        content_layout.addWidget(title)

        self.dashboard = Dashboard()
        content_layout.addWidget(self.dashboard)

        root_layout.addWidget(content)

        self.setCentralWidget(root)

        status = QStatusBar()
        status.showMessage("Ghostrader AI Brain : ONLINE")
        self.setStatusBar(status)

        self.setStyleSheet("""
            QMainWindow{
                background:#101010;
            }

            QWidget{
                background:#101010;
                color:white;
            }

            QStatusBar{
                background:#050505;
                color:white;
                border-top:1px solid #222222;
            }
        """)


def launch():
    """
    Launch Ghostrader Desktop.
    """

    app = QApplication.instance() or QApplication([])

    window = MainWindow()
    window.show()

    app.exec()