"""Tests for the Atlas CLI."""

from __future__ import annotations

from pathlib import Path
import tempfile

from click.testing import CliRunner

from atlas.cli import cli


def _make_temp_repo() -> tuple[Path, Path]:
    """Create a temp git repo and worktree parent dir."""
    tmp = Path(tempfile.mkdtemp())
    repo = tmp / "repo"
    wt_parent = tmp / "worktrees"
    repo.mkdir()
    wt_parent.mkdir()
    # Initialize a git repo on main
    import subprocess

    subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.email", "test@test"],
        cwd=repo,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.name", "Test"],
        cwd=repo,
        check=True,
        capture_output=True,
    )
    subprocess.run(["git", "commit", "--allow-empty", "-m", "init"], cwd=repo, check=True, capture_output=True)
    # Ensure a "main" branch exists (git init may default to "master")
    subprocess.run(
        ["git", "branch", "-m", "main"],
        cwd=repo,
        check=True,
        capture_output=True,
    )
    return repo, wt_parent


def test_run_cycle_prints_summary() -> None:
    repo, wt_parent = _make_temp_repo()
    runner = CliRunner()
    result = runner.invoke(
        cli,
        [
            "--repo",
            str(repo),
            "--worktree-parent",
            str(wt_parent),
            "--knowledge-base",
            str(repo / "docs" / "knowledge-base"),
            "run-cycle",
            "Compare orchestration frameworks",
            "--domains",
            "fundamentals",
        ],
    )
    assert result.exit_code == 0
    assert "Compare orchestration frameworks" in result.output
    assert "fundamentals" in result.output


def test_status_runs() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["status"])
    assert result.exit_code == 0


def test_review_approve() -> None:
    runner = CliRunner()
    result = runner.invoke(cli, ["review", "approve"])
    assert result.exit_code == 0
    assert "approve" in result.output.lower()
