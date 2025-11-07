import json
import subprocess
from copy import deepcopy
from encodings.punycode import T
from pathlib import Path
from re import sub
from typing import Dict

from tests.consts import PROJECT_DIR


def generate_project(template_values_p: Dict[str, str], test_session_id: str) -> Path:
    
    template_values: Dict[str, str] = deepcopy(template_values_p)
    
    cookie_cutter_config = {
        "default_context": template_values
    }
    
    cookie_cutter_config_path = PROJECT_DIR / "sample" / "cookiecutter-test-config-{test_session_id}.json"
    cookie_cutter_config_path.write_text(json.dumps(cookie_cutter_config))
    
    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookie_cutter_config_path)
        ]
    
    subprocess.run(cmd, check=True)
    
    generated_repo_dir: Path = PROJECT_DIR / "sample" / cookie_cutter_config["default_context"]["repo_name"]
    
    return generated_repo_dir

def initialize_git_repo(repo_dir: Path):    
    subprocess.run(["pwd"], cwd=repo_dir, check=True)
    subprocess.run(["git", "init"], cwd=repo_dir, check=True)
    subprocess.run(["git", "add", "--all"], cwd=repo_dir, check=True)
    subprocess.run(["git", "commit", "-m", "initial commit by pytest"], cwd=repo_dir, check=True)
    
