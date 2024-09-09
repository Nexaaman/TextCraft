from TextCraft.entity import (DataIngectionConfig, DataValidationConfig)

from TextCraft.constants import *
from TextCraft.utils.common import read_yaml, create_directories


class ConfigurationManager:
    def __init__(self, config_path = CONFIG_FILE_PATH, params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngectionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngectionConfig(
            root_dir=config.root_dir,
            source_URL = config.source_URL,
            local_path = config.local_path,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config
    
    def get_dataValidation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        get_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            status= config.status,
            REQUIRED_FILES = config.REQUIRED_FILES
        )
        return get_validation_config