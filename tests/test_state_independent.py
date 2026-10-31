"""Tests for ResearchState defaults and summary output."""

from __future__ import annotations

from atlas.state import ResearchState


def test_research_state_defaults() -> None:
    state = ResearchState()
    assert state.objective == ""
    assert state.domains == []
    assert state.review_status == "pending"
    assert state.current_phase == "plan"


def test_research_state_summary_contains_objective() -> None:
    state = ResearchState(objective="investigate quantum algorithms")
    summary = state.summary()
    assert "investigate quantum algorithms" in summary


def test_research_state_custom_values() -> None:
    state = ResearchState(
        objective="map the search space",
        domains=["physics", "math"],
        review_status="approved",
        current_phase="delegate",
    )
    assert state.objective == "map the search space"
    assert state.domains == ["physics", "math"]
    assert state.review_status == "approved"
    assert state.current_phase == "delegate"
