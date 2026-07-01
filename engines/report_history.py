from typing import List

from engines.intelligence_engine import IntelligenceReport


class ReportHistory:
    """
    Stores every Intelligence Report created during a session.
    """

    def __init__(self):
        self._reports: List[IntelligenceReport] = []

    def add_report(self, report: IntelligenceReport):
        """Add a report to history."""
        self._reports.append(report)

    def get_reports(self) -> List[IntelligenceReport]:
        """Return all saved reports."""
        return self._reports

    def report_count(self) -> int:
        """Return the number of saved reports."""
        return len(self._reports)

    def clear(self):
        """Delete all saved reports."""
        self._reports.clear()