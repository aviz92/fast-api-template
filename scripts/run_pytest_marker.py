import argparse

from custom_python_logger import build_logger
from python_github_plus import GitHubClient

logger = build_logger(__name__)


def run_pytest_marker_workflow(
    branch: str | None,
    marker: str,
    repo_full_name: str = "aviz92/dev-template-repository",
    workflow_name: str = "Pytest by Marker",
) -> None:
    github_client = GitHubClient(repo_full_name=repo_full_name)

    logger.debug("Running Pytest workflow with:" f"Marker: {marker}" f"Branch: {branch}" f"Repo: {repo_full_name}")
    _ = github_client.workflow.trigger(workflow_name=workflow_name, branch_name=branch, inputs={"marker": marker})
    logger.info("Workflow triggered successfully!")


def main() -> None:
    parser = argparse.ArgumentParser(description="Trigger Pytest workflow on GitHub with a marker.")
    parser.add_argument(
        "branch",
        nargs="?",
        help="Branch to run workflow on (defaults to current branch)",
        # default="branch-name",
    )
    parser.add_argument(
        "marker",
        nargs="?",
        help="The marker to run (e.g., unit1)",
        # default="marker-name",
    )
    branch = parser.parse_args().branch
    marker = parser.parse_args().marker

    run_pytest_marker_workflow(
        branch=branch,
        marker=marker,
    )


if __name__ == "__main__":
    main()
