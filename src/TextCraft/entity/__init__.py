from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True)
class DataIngectionConfig:
    root_dir: Path
    source_URL: str
    local_path: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status: Path
    REQUIRED_FILES: list

