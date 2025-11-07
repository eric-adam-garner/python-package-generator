"""Test for generating project repos."""

from pathlib import Path


def test_generate_project(project_dir: Path):
    """Generate project repo."""
    assert project_dir.exists()
