"""Base MCP stdio server.

Implements a minimal JSON-RPC 2.0 server that reads requests from stdin and
writes responses to stdout.  Subclasses register tool handlers and implement
``list_tools`` and ``call_tool``.

This is deliberately small and dependency-free so it can run without the
``mcp`` Python package (see docs/02-technology/technology-stack.md).
"""

from __future__ import annotations

import json
import sys
from typing import Any, Callable, Dict


class MCPServer:
    """A minimal MCP-compatible server over stdio."""

    def __init__(self, name: str, version: str = "0.1.0") -> None:
        self.name = name
        self.version = version
        self._handlers: Dict[str, Callable[..., Any]] = {}

    # ------------------------------------------------------------------
    # Tool registration
    # ------------------------------------------------------------------
    def register_tool(self, name: str, handler: Callable[..., Any]) -> None:
        """Register a tool handler."""
        self._handlers[name] = handler

    def list_tools(self) -> list[dict]:
        """Return the list of available tools (MCP tools/list shape)."""
        return [
            {
                "name": name,
                "description": getattr(handler, "__doc__", "") or "",
                "inputSchema": {"type": "object", "properties": {}},
            }
            for name, handler in self._handlers.items()
        ]

    # ------------------------------------------------------------------
    # JSON-RPC handling
    # ------------------------------------------------------------------
    def _handle_request(self, request: dict) -> dict | None:
        method = request.get("method")
        params = request.get("params", {}) or {}
        request_id = request.get("id")

        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {"tools": {}},
                    "serverInfo": {"name": self.name, "version": self.version},
                },
            }

        if method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": {"tools": self.list_tools()},
            }

        if method == "tools/call":
            tool_name = params.get("name")
            arguments = params.get("arguments", {}) or {}
            if tool_name not in self._handlers:
                return self._error(request_id, -32601, f"Unknown tool: {tool_name}")
            try:
                result = self._handlers[tool_name](**arguments)
                return {"jsonrpc": "2.0", "id": request_id, "result": result}
            except Exception as exc:  # noqa: BLE001
                return self._error(request_id, -32603, str(exc))

        return self._error(request_id, -32601, f"Unknown method: {method}")

    @staticmethod
    def _error(request_id: Any, code: int, message: str) -> dict:
        return {"jsonrpc": "2.0", "id": request_id, "error": {"code": code, "message": message}}

    # ------------------------------------------------------------------
    # Run loop
    # ------------------------------------------------------------------
    def run(self) -> None:
        """Read JSON-RPC requests from stdin and write responses to stdout."""
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                request = json.loads(line)
            except json.JSONDecodeError:
                sys.stdout.write(
                    json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}) + "\n"
                )
                sys.stdout.flush()
                continue
            response = self._handle_request(request)
            if response is not None:
                sys.stdout.write(json.dumps(response) + "\n")
                sys.stdout.flush()
