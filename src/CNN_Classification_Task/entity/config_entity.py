# Modify the return types of the config.yaml file
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path