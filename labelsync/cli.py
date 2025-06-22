"""
scripts/cli.py

Entry point for the LabelSync CLI tool.
Parses command-line arguments and delegates to labelsync.sync.main().
"""

import argparse
from labelsync import sync


def main():
    """
    Parse command-line arguments for the LabelSync tool and invoke the label synchronization process.
    
    This function defines and processes CLI arguments for specifying the target GitHub repository, label definition file, and various operational flags, then delegates execution to the label synchronization logic.
    """
    parser = argparse.ArgumentParser(
        description="Sync GitHub labels with a TOML file using GitHub CLI."
    )

    parser.add_argument(
        "--repo",
        required=True,
        help="GitHub repository in the format owner/repo"
    )

    parser.add_argument(
        "--file",
        required=True,
        help="Path to TOML label file"
    )

    parser.add_argument(
        "--skip-delete",
        action="store_true",
        help="Skip deleting existing labels before applying new ones"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview changes without modifying anything"
    )

    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR"],
        help="Console logging level (default: INFO)"
    )

    args = parser.parse_args()
    sync.main(args)


if __name__ == "__main__":
    main()
