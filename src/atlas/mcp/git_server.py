"""MCP git server.

Exposes read-only git tools for agents (git_branch, git_status, git_diff).
Commit and push are deliberately NOT exposed to agents — only the Manager
Agent performs Git integration (see docs/09-management/decisions.md).
"""

from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

from .server_base import MCPServer


class GitServer(MCPServer):
    """MCP server for read-only git operations within a repository."""

    def __init__(self, repo_root: str | Path) -> None:
        super().__init__("atlas-git", "0.1.0")
        self.repo_root = Path(repo_root).resolve()
        self.register_tool("git_branch", self.git_branch)
        self.register_tool("git_status", self.git_status)
        self.register_tool("git_diff", self.git_diff)

    # ------------------------------------------------------------------
    # Tool handlers (read-only)
    # ------------------------------------------------------------------
    def git_branch(self) -> dict[str, Any]:
        """Return the name of the currently checked-out branch."""
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            cwd=self.repo_root,
            capture_output=True,
            text=True,
            check=True,
        )
        return {"branch": result.stdout.strip()}

    def git_status(self) -> dict[str, Any]:
        """Return the short status of the working tree."""
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=self.repo_root,
            capture_output=True,
            text=True,
            check=True,
        )
        return {"status": result.stdout.strip() or "clean"}

    def git_diff(self, path: str | None = None) -> dict[str, Any]:
        """Return the unstaged diff, optionally for one path."""
        args = ["git", "diff"]
        if path:
            args.append("--")
            args.append(path)
        result = subprocess.run(
            args,
            cwd=self.repo_root,
            capture_output=True,
            text=True,
            check=True,
        )
        return {"diff": result.stdout.strip()}
