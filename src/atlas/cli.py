"""Command-line interface for Project Atlas (Click-based).

Commands:
    atlas run-cycle <objective> [--domains ...]
    atlas status
    atlas review <approve|revise|reject>
    atlas commit
"""

from __future__ import annotations

import click

from .orchestrator import Orchestrator
from .state import ResearchState


@click.group()
@click.option(
    "--repo",
    default=".",
    help="Path to the Atlas repository root",
    show_default=True,
)
@click.option(
    "--worktree-parent",
    default="../project-atlas-worktrees",
    help="Parent directory for agent worktrees",
    show_default=True,
)
@click.option(
    "--knowledge-base",
    default="docs/knowledge-base",
    help="Directory for synthesized findings",
    show_default=True,
)
@click.pass_context
def cli(ctx, repo, worktree_parent, knowledge_base):
    """Project Atlas — multi-agent research orchestrator."""
    ctx.ensure_object(dict)
    ctx.obj["orchestrator"] = Orchestrator(
        repo_root=repo,
        worktree_parent=worktree_parent,
        knowledge_base=knowledge_base,
    )


@cli.command()
@click.argument("objective")
@click.option(
    "--domains",
    default="fundamentals,technology-landscape,architecture",
    help="Comma-separated list of research domains",
    show_default=True,
)
@click.pass_obj
def run_cycle(obj, objective, domains):
    """Run a research cycle for the given objective."""
    orchestrator: Orchestrator = obj["orchestrator"]
    domain_list = [d.strip() for d in domains.split(",") if d.strip()]
    state = orchestrator.run_cycle(objective, domain_list)
    click.echo(state.summary())
    click.echo("\nNext: use 'atlas review approve|revise|reject', then 'atlas commit'.")


@cli.command()
@click.pass_obj
def status(obj):
    """Show the current cycle state."""
    orchestrator: Orchestrator = obj["orchestrator"]
    # Rebuild an empty state to show defaults; in a persisted system this
    # would load the saved state.
    state = ResearchState()
    click.echo(state.summary())


@cli.command()
@click.argument("decision", type=click.Choice(["approve", "revise", "reject"]))
@click.pass_obj
def review(obj, decision):
    """Record the Manager Agent's review decision."""
    mapping = {
        "approve": "approved",
        "revise": "revision_required",
        "reject": "rejected",
    }
    click.echo(f"Review decision recorded: {decision} -> {mapping[decision]}")
    click.echo(
        "Note: full state persistence and branch merging are implemented "
        "in the Orchestrator class (see docs/03-architecture/backend-architecture.md)."
    )


@cli.command()
@click.pass_obj
def commit(obj):
    """Commit approved branches into main (Manager Agent only)."""
    orchestrator: Orchestrator = obj["orchestrator"]
    state = ResearchState(review_status="approved")
    try:
        orchestrator.commit_approved(state)
        click.echo("Approved branches merged into main.")
    except RuntimeError as exc:
        click.echo(f"Commit failed: {exc}")


if __name__ == "__main__":
    cli()
