"""Git worktree management for agent isolation.

Each research domain gets its own Git branch and isolated worktree so that
workers never overwrite each other's files and main stays clean until the
Manager Agent approves and merges a branch.

All operations delegate to the ``git`` CLI via subprocess.  No external
Python packages are required.
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Dict, Optional


class WorktreeManager:
    """Create, list, and remove Git worktrees for research domains."""

    def __init__(self, repo_root: Path, worktree_parent: Path) -> None:
        """Initialize with the repository root and the parent dir for worktrees.

        Args:
            repo_root: Path to the main Atlas repository (contains .git).
            worktree_parent: Parent directory where worktrees are created,
                e.g. ``../project-atlas-worktrees``.
        """
        self.repo_root = repo_root.resolve()
        self.worktree_parent = worktree_parent.resolve()
        self.worktree_parent.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Low-level git helpers
    # ------------------------------------------------------------------
    def _run(self, args: list[str], cwd: Path | None = None) -> str:
        """Run a git command and return its stdout.  Raises on failure."""
        result = subprocess.run(
            ["git"] + args,
            cwd=str(cwd or self.repo_root),
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()

    def current_branch(self) -> str:
        """Return the name of the branch currently checked out in the repo."""
        return self._run(["branch", "--show-current"])

    # ------------------------------------------------------------------
    # Worktree operations
    # ------------------------------------------------------------------
    def branch_exists(self, branch: str) -> bool:
        """Return True if ``branch`` already exists in the repository."""
        try:
            self._run(["rev-parse", "--verify", branch])
            return True
        except subprocess.CalledProcessError:
            return False

    def create_branch(self, branch: str, from_branch: str = "main") -> None:
        """Create a new branch from ``from_branch`` (default: main)."""
        self._run(["branch", branch, from_branch], cwd=self.repo_root)

    def create_worktree(self, domain: str, branch: str) -> Path:
        """Create a worktree for ``domain`` on ``branch``.

        Returns the absolute path to the new worktree directory.
        """
        worktree_path = self.worktree_parent / domain
        if worktree_path.exists():
            raise FileExistsError(f"Worktree already exists: {worktree_path}")
        self._run(["worktree", "add", str(worktree_path), branch], cwd=self.repo_root)
        return worktree_path

    def list_worktrees(self) -> list[str]:
        """Return the absolute paths of all registered worktrees."""
        output = self._run(["worktree", "list", "--porcelain"])
        paths: list[str] = []
        for line in output.splitlines():
            if line.startswith("worktree "):
                paths.append(line.split(" ", 1)[1])
        return paths

    def remove_worktree(self, domain: str, force: bool = False) -> None:
        """Remove the worktree for ``domain``.

        Args:
            domain: Domain name (worktree directory name).
            force: If True, remove even if there are uncommitted changes.
        """
        worktree_path = self.worktree_parent / domain
        args = ["worktree", "remove"]
        if force:
            args.append("--force")
        args.append(str(worktree_path))
        self._run(args, cwd=self.repo_root)

    def worktree_branch(self, domain: str) -> Optional[str]:
        """Return the branch name checked out in a worktree, or None."""
        worktree_path = self.worktree_parent / domain
        try:
            return self._run(["branch", "--show-current"], cwd=worktree_path)
        except subprocess.CalledProcessError:
            return None
