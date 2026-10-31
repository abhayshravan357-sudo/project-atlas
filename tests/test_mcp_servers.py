"""Tests for MCP servers."""

from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

from atlas.mcp.filesystem_server import FilesystemServer
from atlas.mcp.git_server import GitServer


def test_filesystem_server_read_write_list() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        server = FilesystemServer(root)

        # write then read
        result = server.write_file("hello.txt", "world")
        assert result["status"] == "written"

        result = server.read_file("hello.txt")
        assert result["content"] == "world"

        # list
        result = server.list_directory(".")
        names = [e["name"] for e in result["entries"]]
        assert "hello.txt" in names


def test_fileserver_blocks_escape() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        server = FilesystemServer(root)
        try:
            server.read_file("../secret.txt")
            assert False, "Expected PermissionError"
        except PermissionError as exc:
            assert "denied" in str(exc)


def test_git_server_branch_and_status() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "repo"
        repo.mkdir()
        subprocess.run(["git", "init"], cwd=repo, check=True, capture_output=True)
        subprocess.run(["git", "config", "user.email", "t@t"], cwd=repo, capture_output=True)
        subprocess.run(["git", "config", "user.name", "T"], cwd=repo, capture_output=True)
        subprocess.run(["git", "commit", "--allow-empty", "-m", "init"], cwd=repo, capture_output=True)
        subprocess.run(["git", "branch", "-m", "main"], cwd=repo, capture_output=True)

        server = GitServer(repo)
        branch = server.git_branch()
        assert branch["branch"] == "main"
        status = server.git_status()
        assert status["status"] == "clean"


def test_mcp_server_jsonrpc_roundtrip() -> None:
    import io
    import sys

    from atlas.mcp.server_base import MCPServer

    server = MCPServer("test", "1.0")
    server.register_tool("echo", lambda text: text)

    request = {"jsonrpc": "2.0", "id": 1, "method": "tools/call", "params": {"name": "echo", "arguments": {"text": "hi"}}}
    response = server._handle_request(request)
    assert response["jsonrpc"] == "2.0"
    assert response["id"] == 1
    assert response["result"] == "hi"
