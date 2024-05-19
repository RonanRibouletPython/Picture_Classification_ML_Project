# Modify the return types of the config.yaml file
from dataclasses import dataclass
from pathlib import Path

################################

# Data ingestion config

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

################################

################################

# Model preparation configuration

@dataclass(frozen = True)
class PrepareBaseModelConfig:
    # config.yaml file
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    # params.yaml file
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

################################

