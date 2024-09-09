from TextCraft.config.configuration import ConfigurationManager
from TextCraft.components.DataValidation import DataValidation
from TextCraft.logging import logger

class DataValidationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_dataValidation_config()
        data_validation_config = DataValidation(config = data_validation_config)
        data_validation_config.validation_validate()