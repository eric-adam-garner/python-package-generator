"""Tests for project repo makefile."""

import subprocess
from pathlib import Path


def test_linting(project_dir: Path):
    """Test linting."""
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)


def test_tests(project_dir: Path):
    """Test default tests."""
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)
