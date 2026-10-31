"""Shared state for the Atlas research cycle.

The research cycle is:

    plan -> delegate -> investigate -> report -> review -> synthesize -> commit -> reassess

Each phase reads and updates this state.  The state is intentionally small and
serializable so it can be persisted between cycles if needed.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class ResearchState:
    """Mutable state carried through one research cycle."""

    objective: str = ""
    domains: List[str] = field(default_factory=list)
    worktrees: Dict[str, str] = field(default_factory=dict)
    reports: Dict[str, str] = field(default_factory=dict)
    synthesis: str = ""
    review_status: str = "pending"  # pending | approved | revision_required | rejected
    current_phase: str = "plan"
    messages: List[str] = field(default_factory=list)

    def log(self, message: str) -> None:
        self.messages.append(message)

    def summary(self) -> str:
        return (
            f"Atlas cycle state:\n"
            f"  objective: {self.objective!r}\n"
            f"  domains: {self.domains}\n"
            f"  worktrees: {self.worktrees}\n"
            f"  reports: {list(self.reports.keys())}\n"
            f"  review_status: {self.review_status}\n"
            f"  current_phase: {self.current_phase}"
        )
