"""MCP filesystem server.

Exposes read_file, write_file, and list_directory tools.  All file access is
scoped to a single root directory (the agent's assigned worktree) so agents
cannot read or write outside their assigned directory.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any

from .server_base import MCPServer


class FilesystemServer(MCPServer):
    """MCP server for filesystem access, scoped to one root directory."""

    def __init__(self, root: str | Path) -> None:
        super().__init__("atlas-filesystem", "0.1.0")
        self.root = Path(root).resolve()
        self.register_tool("read_file", self.read_file)
        self.register_tool("write_file", self.write_file)
        self.register_tool("list_directory", self.list_directory)

    # ------------------------------------------------------------------
    # Safety
    # ------------------------------------------------------------------
    def _resolve(self, path: str) -> Path:
        """Resolve ``path`` under the root and reject escapes."""
        target = (self.root / path).resolve()
        if self.root not in target.parents and target != self.root:
            raise PermissionError(f"Access outside worktree root denied: {path}")
        return target

    # ------------------------------------------------------------------
    # Tool handlers
    # ------------------------------------------------------------------
    def read_file(self, path: str) -> dict[str, Any]:
        """Read the contents of a file within the worktree root."""
        target = self._resolve(path)
        if not target.is_file():
            return {"error": f"Not a file: {path}"}
        return {"content": target.read_text(encoding="utf-8")}

    def write_file(self, path: str, content: str) -> dict[str, Any]:
        """Write ``content`` to a file within the worktree root."""
        target = self._resolve(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        return {"status": "written", "path": str(target)}

    def list_directory(self, path: str = ".") -> dict[str, Any]:
        """List entries in a directory within the worktree root."""
        target = self._resolve(path)
        if not target.is_dir():
            return {"error": f"Not a directory: {path}"}
        entries = []
        for child in sorted(target.iterdir()):
            entries.append({"name": child.name, "type": "directory" if child.is_dir() else "file"})
        return {"entries": entries}
