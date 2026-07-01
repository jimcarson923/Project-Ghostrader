"""
Ghostrader Analysis Result

Purpose:
    This is the standard object returned by GhostCore.

Every module inside Ghostrader should use this object.

Version:
    1.0.0
"""

from dataclasses import dataclass
from typing import Dict


@dataclass
class AnalysisResult:
    """
    Standard analysis object used throughout Ghostrader.
    """

    # Stock Symbol
    symbol: str

    # Ghost Score Results
    score: Dict

    # Market Intelligence Results
    intelligence: Dict

    # Trading Signal
    signal: str
    