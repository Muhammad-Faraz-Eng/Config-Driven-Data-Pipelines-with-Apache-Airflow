import yaml
from pathlib import Path
from typing import Dict


class ConfigLoader:
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)

    def load(self, filename: str) -> Dict:
        file_path = self.base_path / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Config file not found: {file_path}")
        with open(file_path, "r") as f:
            return yaml.safe_load(f)
