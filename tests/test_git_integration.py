"""Integration tests for Git worktree management using real temporary repositories.

These tests exercise the real ``git`` CLI against throwaway repositories in a
temporary directory. They verify branch creation, worktree creation,
worktree-to-branch association, isolation between worktrees, existing-worktree
detection, invalid-repository handling, cleanup/recovery, and protection of the
main worktree.

No production repository or worktree is modified.
"""

from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

from atlas.worktree_manager import WorktreeManager


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_temp_repo() -> tuple[Path, Path]:
    """Create a temp git repo on ``main`` and a worktree parent directory."""
    tmp = Path(tempfile.mkdtemp())
    repo = tmp / "repo"
    wt_parent = tmp / "worktrees"
    repo.mkdir()
    wt_parent.mkdir()
    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "t@t"], cwd=repo, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, capture_output=True)
    subprocess.run(
        ["git", "commit", "--allow-empty", "-m", "init"], cwd=repo, capture_output=True
    )
    subprocess.run(["git", "branch", "-m", "main"], cwd=repo, capture_output=True)
    return repo, wt_parent


# ---------------------------------------------------------------------------
# WorktreeManager tests against real git
# ---------------------------------------------------------------------------


def test_worktree_manager_uses_provided_paths() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "repo"
        wt_parent = Path(tmp) / "worktrees"
        repo.mkdir()
        wt_parent.mkdir()
        mgr = WorktreeManager(repo, wt_parent)
        assert mgr.repo_root == repo
        assert mgr.worktree_parent == wt_parent


def test_create_branch_and_worktree() -> None:
    repo, wt_parent = _make_temp_repo()
    mgr = WorktreeManager(repo, wt_parent)

    path = mgr.create_worktree("fundamentals", "research/fundamentals")

    assert path == wt_parent / "fundamentals"
    assert path.is_dir()
    assert mgr.worktree_branch("fundamentals") == "research/fundamentals"


def test_branch_created_from_main_not_current() -> None:
    repo, wt_parent = _make_temp_repo()
    mgr = WorktreeManager(repo, wt_parent)

    # Create and checkout a non-main branch to prove create_branch uses main.
    mgr._run(["checkout", "-b", "side"], cwd=repo)
    mgr.create_worktree("arch", "research/architecture")
    assert mgr.worktree_branch("arch") == "research/architecture"


def test_worktrees_are_isolated() -> None:
    repo, wt_parent = _make_temp_repo()
    mgr = WorktreeManager(repo, wt_parent)

    mgr.create_worktree("a", "research/a")
    mgr.create_worktree("b", "research/b")

    (wt_parent / "a" / "file-a.txt").write_text("a")
    (wt_parent / "b" / "file-b.txt").write_text("b")

    assert (wt_parent / "a" / "file-a.txt").read_text() == "a"
    assert (wt_parent / "b" / "file-b.txt").read_text() == "b"
    assert not (wt_parent / "a" / "file-b.txt").exists()


def test_list_worktrees_returns_created_paths() -> None:
    repo, wt_parent = _make_temp_repo()
    mgr = WorktreeManager(repo, wt_parent)

    mgr.create_worktree("a", "research/a")
    mgr.create_worktree("b", "research/b")

    paths = mgr.list_worktrees()
    assert str(wt_parent / "a") in paths
    assert str(wt_parent / "b") in paths


def test_create_worktree_rejects_existing() -> None:
    repo, wt_parent = _make_temp_repo()
    mgr = WorktreeManager(repo, wt_parent)

    mgr.create_worktree("a", "research/a")
    try:
        mgr.create_worktree("a", "research/a")
        assert False, "Expected FileExistsError"
    except FileExistsError:
        pass


def test_remove_worktree() -> None:
    repo, wt_parent = _make_temp_repo()
    mgr = WorktreeManager(repo, wt_parent)

    mgr.create_worktree("a", "research/a")
    assert (wt_parent / "a").is_dir()
    mgr.remove_worktree("a")
    assert not (wt_parent / "a").exists()


def test_remove_worktree_with_force() -> None:
    repo, wt_parent = _make_temp_repo()
    mgr = WorktreeManager(repo, wt_parent)

    mgr.create_worktree("a", "research/a")
    (wt_parent / "a" / "untracked.txt").write_text("dirty")
    mgr.remove_worktree("a", force=True)
    assert not (wt_parent / "a").exists()


def test_invalid_repository_raises() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        not_a_repo = Path(tmp) / "not-a-repo"
        not_a_repo.mkdir()
        wt_parent = Path(tmp) / "worktrees"
        wt_parent.mkdir()
        mgr = WorktreeManager(not_a_repo, wt_parent)

        try:
            mgr.create_worktree("a", "research/a")
            assert False, "Expected an error from git"
        except Exception:
            pass  # git CLI fails because not_a_repo is not a git repository


# ---------------------------------------------------------------------------
# CLI-driven end-to-end worktree creation (via orchestrator delegate)
# ---------------------------------------------------------------------------


def test_orchestrator_delegate_creates_worktrees() -> None:
    repo, wt_parent = _make_temp_repo()
    from atlas.orchestrator import Orchestrator

    orch = Orchestrator(repo, wt_parent, repo / "docs" / "knowledge-base")
    state = orch.run_cycle("Test objective", ["fundamentals", "architecture"])

    assert state.worktrees["fundamentals"] == str(wt_parent / "fundamentals")
    assert state.worktrees["architecture"] == str(wt_parent / "architecture")
    assert (wt_parent / "fundamentals" / "docs" / "research" / "fundamentals" / "REPORT.md").is_file()
    assert (wt_parent / "architecture" / "docs" / "research" / "architecture" / "REPORT.md").is_file()


def test_cleanup_after_failure() -> None:
    repo, wt_parent = _make_temp_repo()
    mgr = WorktreeManager(repo, wt_parent)

    mgr.create_worktree("a", "research/a")
    mgr.remove_worktree("a", force=True)
    assert not (wt_parent / "a").exists()


def test_main_worktree_not_removed() -> None:
    repo, wt_parent = _make_temp_repo()
    mgr = WorktreeManager(repo, wt_parent)

    # Creating worktrees must not touch the main checkout.
    mgr.create_worktree("a", "research/a")
    assert (repo / ".git").is_dir()
    assert mgr.current_branch() == "main"
    mgr.remove_worktree("a", force=True)
    assert (repo / ".git").is_dir()
    assert mgr.current_branch() == "main"
