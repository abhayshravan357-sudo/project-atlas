"""Command-line interface for Project Atlas.

Minimal entry point for running a research cycle.  A fuller CLI (Click/Typer)
is planned for D-05.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from .orchestrator import Orchestrator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="atlas",
        description="Project Atlas — multi-agent research orchestrator",
    )
    parser.add_argument(
        "objective",
        help="Research objective to investigate",
    )
    parser.add_argument(
        "--domains",
        default="fundamentals,technology-landscape,architecture",
        help="Comma-separated list of research domains",
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="Path to the Atlas repository root",
    )
    parser.add_argument(
        "--worktree-parent",
        default="../project-atlas-worktrees",
        help="Parent directory for agent worktrees",
    )
    parser.add_argument(
        "--knowledge-base",
        default="docs/knowledge-base",
        help="Directory for synthesized findings",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    domains = [d.strip() for d in args.domains.split(",") if d.strip()]

    orchestrator = Orchestrator(
        repo_root=Path(args.repo),
        worktree_parent=Path(args.worktree_parent),
        knowledge_base=Path(args.knowledge_base),
    )

    state = orchestrator.run_cycle(args.objective, domains)
    print(state.summary())
    print("\nNext: run review gate, then commit_approved() if approved.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
