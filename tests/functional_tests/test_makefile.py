import subprocess
from pathlib import Path

from tests.fixtures.project_dir import project_dir


def test_linting(project_dir: Path):
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)
    
def test_tests(project_dir: Path): 
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)
    
def test_install(project_dir: Path):
    pass