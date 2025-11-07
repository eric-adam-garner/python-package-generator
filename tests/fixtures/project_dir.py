"""Test fixtures."""

import shutil
import subprocess
from pathlib import Path
from typing import Generator
from uuid import uuid4

import pytest

from tests.utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="function")
def project_dir() -> Generator[Path, None, None]:
    """Generate project repo."""
    test_session_id = generate_test_session_id()
    template_values = {"repo_name": f"test-repo-{test_session_id}"}
    generated_repo_dir: Path = generate_project(template_values, test_session_id)
    try:
        initialize_git_repo(generated_repo_dir)
        subprocess.run(["make", "lint-ci"], cwd=generated_repo_dir, check=False)
        yield generated_repo_dir
    finally:
        shutil.rmtree(generated_repo_dir)


def generate_test_session_id() -> str:
    """Generate unique session id."""
    uuid = str(uuid4())[:6]
    return uuid
