from re import sub
import subprocess
from pathlib import Path
import json


THIS_DIR = Path(__file__).parent
PROJECT_DIR = THIS_DIR.parent

def test_generate_project():
    
    cookie_cutter_config = {
        "default_context": {"repo_name": "test-repo"}
    }
    
    cookie_cutter_config_path = PROJECT_DIR / "cookie-cutter-test-config.json"
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
    
    generated_repo_dir = PROJECT_DIR / "sample" / cookie_cutter_config["default_context"]["repo_name"]
    assert generated_repo_dir.exists()
    
    subprocess.run(["make", "clean"])
