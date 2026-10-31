"""Tests for the Atlas orchestrator."""

from __future__ import annotations

from pathlib import Path
import tempfile

from atlas.state import ResearchState
from atlas.worktree_manager import WorktreeManager


def test_state_summary_contains_objective() -> None:
    state = ResearchState(objective="test objective", domains=["a", "b"])
    summary = state.summary()
    assert "test objective" in summary
    assert "a" in summary
    assert "b" in summary


def test_worktree_manager_uses_provided_paths() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "repo"
        wt_parent = Path(tmp) / "worktrees"
        repo.mkdir()
        wt_parent.mkdir()
        mgr = WorktreeManager(repo, wt_parent)
        assert mgr.repo_root == repo
        assert mgr.worktree_parent == wt_parent


def test_state_defaults() -> None:
    state = ResearchState()
    assert state.objective == ""
    assert state.domains == []
    assert state.worktrees == {}
    assert state.reports == {}
    assert state.review_status == "pending"
    assert state.current_phase == "plan"
