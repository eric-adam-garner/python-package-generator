from pathlib import Path

from tests.fixtures.project_dir import project_dir


def test_generate_project(project_dir: Path):    
    assert project_dir.exists()
    