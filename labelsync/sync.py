"""
labelsync/sync.py

Main logic for GitHub label synchronization using GitHub CLI.
Intended to be invoked from an external CLI or script.
"""

import tomllib
import tomli_w
import subprocess
from datetime import datetime
from pathlib import Path
from loguru import logger
from labelsync.logger_setup import configure_console_logger


def run_gh_command(cmd: list[str], repo: str, dry_run: bool = False) -> str | None:
    """
    Executes a GitHub CLI command.

    Args:
        cmd (list[str]): Base GitHub CLI command arguments (without 'gh').
        repo (str): Target GitHub repository in the format "owner/repo".
        dry_run (bool): If True, simulates execution without making changes.

    Returns:
        str | None: The standard output from the command, or None if it fails.
    """
    full_cmd = ["gh"] + cmd + ["--repo", repo]
    if dry_run:
        logger.debug(f"[DRY-RUN] Would run: {' '.join(full_cmd)}")
        return ""
    try:
        result = subprocess.run(full_cmd, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        logger.error(f"Command failed: {' '.join(full_cmd)}")
        logger.error(e.stderr)
        return None


def backup_labels(repo: str, dry_run: bool = False) -> None:
    """
    Creates a TOML backup file of all current labels in the GitHub repository.

    Args:
        repo (str): GitHub repository in the format "owner/repo".
        dry_run (bool): If True, skips execution.
    """
    if dry_run:
        logger.info("[DRY-RUN] Skipping label backup.")
        return

    logger.info(f"📦 Backing up current labels from {repo}...")
    output = run_gh_command(["label", "list"], repo)
    if not output:
        logger.warning("Could not fetch label list.")
        return

    labels = []
    for line in output.splitlines():
        parts = line.split("\t")
        name = parts[0]
        color = parts[1]
        description = parts[2] if len(parts) > 2 else ""
        labels.append({"name": name, "color": color, "description": description})

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"backup_labels_{repo.replace('/', '_')}_{timestamp}.toml"

    with open(backup_file, "wb") as f:
        tomli_w.dump({"label": labels}, f)

    logger.success(f"Labels backed up to {backup_file}")


def delete_all_labels(repo: str, dry_run: bool = False) -> None:
    """
    Deletes all existing labels from the given GitHub repository.

    Args:
        repo (str): GitHub repository in the format "owner/repo".
        dry_run (bool): If True, simulates deletion without executing it.
    """
    logger.info(f"🗑️  Fetching existing labels from {repo}...")
    output = run_gh_command(["label", "list"], repo, dry_run)
    if not output:
        logger.warning("Could not retrieve label list.")
        return

    for line in output.splitlines():
        label = line.split("\t")[0]
        logger.info(f"❌ Deleting: {label}")
        run_gh_command(["label", "delete", label, "--yes"], repo, dry_run)


def create_labels_from_toml(file_path: str, repo: str, dry_run: bool = False) -> None:
    """
    Creates GitHub labels from a TOML configuration file.

    Args:
        file_path (str): Path to the TOML file containing label definitions.
        repo (str): GitHub repository in the format "owner/repo".
        dry_run (bool): If True, simulates label creation.
    """
    logger.info(f"📄 Reading labels from: {file_path}")
    with open(file_path, "rb") as f:
        data = tomllib.load(f)

    labels = data.get("label", [])
    for label in labels:
        name = label["name"]
        description = label.get("description", "")
        color = label.get("color", "ffffff")

        logger.info(f"✅ Creating label: {name}")
        run_gh_command([
            "label", "create", name,
            "--description", description,
            "--color", color
        ], repo, dry_run)


def main(args) -> None:
    """
    Main entry point for the label synchronization process.
    Should be called from an external script or CLI.

    Args:
        args (argparse.Namespace): Parsed CLI arguments.
    """
    configure_console_logger(args.log_level)

    if not args.dry_run:
        logger.warning(f"You are about to modify labels in: {args.repo}")
        logger.info(f"Using label definitions from: {args.file}")
        confirm = input("❓ Are you sure you want to proceed? (y/N): ").strip().lower()
        if confirm not in ("y", "yes"):
            logger.warning("Operation cancelled by user.")
            return

    backup_labels(args.repo, dry_run=args.dry_run)

    if not args.skip_delete:
        delete_all_labels(args.repo, dry_run=args.dry_run)
    else:
        logger.info("⏭️  Skipping label deletion (--skip-delete enabled)")

    create_labels_from_toml(args.file, args.repo, dry_run=args.dry_run)

    logger.success("🎉 Label sync complete.")
