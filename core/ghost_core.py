"""
=========================================================
GHO$TRADER Ghost Core

Purpose:
    Central application-facing coordinator for Ghostrader
    analysis.

Build:
    1.35.0 - Connect Ghost Core to Analysis Pipeline
=========================================================
"""

from core.analysis_pipeline import AnalysisPipeline, PipelineAnalysisResult


class GhostCore:
    """
    Application-facing Ghostrader coordinator.

    GhostCore now delegates the detailed analysis workflow
    to the AnalysisPipeline. This keeps GhostCore clean while
    allowing the pipeline to grow with new engines.
    """

    def __init__(self):
        self.analysis_pipeline = AnalysisPipeline()

    def analyze(self, symbol: str) -> PipelineAnalysisResult:
        clean_symbol = symbol.strip().upper()

        if not clean_symbol:
            raise ValueError("Stock symbol cannot be empty.")

        return self.analysis_pipeline.analyze_stock(clean_symbol)