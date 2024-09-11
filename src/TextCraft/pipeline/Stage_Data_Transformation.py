from TextCraft.config.configuration import ConfigurationManager
from TextCraft.components.DataTransformation import DataTransformation
from TextCraft.logging import logger

class DataTransformationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation()
        data_transformation = DataTransformation(config = data_transformation_config)
        data_transformation.convert()





    